'''
Tema: Métodos Numéricos
Grupo 6
Integrantes:

•	Kevin Josue Amaguaña Rivadeneira
•	Priscila Veronica Chisag Pillajo
•	Andy Ricardo Galarza Morales
•	Stiven Anthony Pilca Sánchez

Carrera: Ingeniería en Sistemas de la información
Paralelo: SI4 - 002
'''


# Metodo para buscar el primer 1 y colocar una coma después de ese 1
def busqueda_puesta_punto(numero_binario: str):
    posicion = int(numero_binario.find("1"))

    resultado = numero_binario[:posicion+1]+"."+numero_binario[posicion+1:]

    return resultado


# Metodo para quitar la coma
def quitar_punto(numero_binario: str):
    posicion = int(numero_binario.find("."))
    num_exponente = int(len(numero_binario[1:posicion]))
    posicion = int(numero_binario.find("."))
    resultado = numero_binario[:posicion]+numero_binario[posicion+1:]

    return resultado, num_exponente


# Metodo para quitar el primer 1
def quitar_uno(numero_binario):
    posicion = int(numero_binario.find("1"))
    resultado = numero_binario[:posicion]+numero_binario[posicion+1:]

    return resultado


# Metodo para calcular el signo desde un numero decimal
def signo(num_decimal):
    signo_binario = "0" if num_decimal >= 0 else "1"

    return signo_binario


# Metodo para calcular el exponente de los 2 tipos de precisiones
def exponente(tipo_pre: int, numero_exponente: int):
    # Proceso para calcular el exponente en un tipo de precision u otro
    exp_binario = 127 + numero_exponente if tipo_pre == 1 else 1023 + numero_exponente
    texto_final = str(bin(exp_binario)[2:])
    if tipo_pre==1:
        if len(texto_final)<8:
            falta= 8-len(texto_final)
            texto_final = "0"*falta+texto_final
    else:
        if len(texto_final)<11:
            falta= 11-len(texto_final)
            texto_final = "0"*falta+texto_final

    return texto_final


# Metodo para calcular la mantisa de los 2 tipos de precisiones
def mantisa(numero_binario: str, tipo_precision: int):
    digitos_i = int(len(numero_binario))

    # Proceso para calcular si faltan o sobran digitos
    num = 24 - digitos_i if tipo_precision == 1 else 53 - digitos_i

    # Proceso para calcular la mantissa en un tipo de precision u otro
    if num >= 0:
        mant_sp = str(numero_binario)+"."+"0"*num
        mant_p, exponente = quitar_punto(mant_sp)
        mant_f = quitar_uno(mant_p)
    else:
        slicing = slice(0, num)

        mant_sp = str(numero_binario)
        mant_sp = mant_sp[slicing]
        mant_f = quitar_uno(mant_sp)

    return mant_f


# Metodo que une las cadenas de texto signo, exponente y mantisa para transformarlas a hexadecimal, sirve para los dos tipos de precisiones
def bin_a_hex(num_s_bin, num_e_bin, num_m_bin, tipo_pre):
    cadena_binario = num_s_bin+num_e_bin+num_m_bin
    contador = int()
    resultado = str()

    # Proceso para calcular el numero hexadecimal para un tipo de precision u otro
    if tipo_pre == 1:
        while (contador < 32):
            binario = cadena_binario[contador:contador+4]
            decimal = int(binario, 2)
            hexa = hex(int(decimal))
            resultado = resultado+hexa[2:]
            contador += 4
    else:
        while (contador < 64):
            binario = cadena_binario[contador:contador+4]
            decimal = int(binario, 2)
            hexa = hex(int(decimal))
            resultado = resultado+hexa[2:]
            contador += 4

    return resultado


# Metodo para representar un numero binario normalizado y transformado a hexadecimal
def norma_bin_hexa(numero_signo, numero_binario):
    num_digitos = len(numero_binario)

    # Proceso para aumentar ceros o quitar digitos de ser necesario
    if num_digitos <= 31:
        num_falta = 31-num_digitos
        num_bin_f = numero_signo+"0"*num_falta+str(numero_binario)

        numero_hexadecimal = bin_hexa(num_bin_f)
    else:
        num_sobra = int(num_digitos)-31
        slicing = slice(0, -num_sobra)
        numero_binario = str(numero_binario)[slicing]
        num_bin_f = numero_signo+str(numero_binario)

        numero_hexadecimal = bin_hexa(num_bin_f)

    return numero_hexadecimal


# Metodo usado solamente para transformar un numero binario normalizado a hexadecimal
def bin_hexa(num_bin_f):
    num_resultado = str()
    contador = int()
    while (contador < 32):
        binario = num_bin_f[contador:contador+4]
        decimal = int(binario, 2)
        num_hexa = hex(decimal)
        num_resultado = num_resultado+num_hexa[2:]
        contador += 4

    return num_resultado


def flotante(numero_decimal, tipo_precision):

    parte_entera, parte_decimal = str(numero_decimal).split(".")
    parte_entera = int(parte_entera)
    parte_entera = bin(parte_entera).lstrip("0b")
    parte_decimal = int(parte_decimal)/pow(10, (len(parte_decimal)))

    auxiliar, auxiliar1, auxiliar2 = str(), str(), str()
    rango = 30 if tipo_precision == 1 else 50

    for i in range(rango):
        parte_decimal *= 2
        auxiliar1, auxiliar2 = str(parte_decimal).split(".")
        auxiliar += auxiliar1
        parte_decimal = int(auxiliar2)/pow(10, (len(auxiliar2)))

    parte_decimal = auxiliar

    return parte_entera, parte_decimal


def binario_normalizado(numero_decimal: float):
    numero_signo = signo(numero_decimal)
    numero_decimal = abs(numero_decimal)
    parte_entera, parte_decimal = str(numero_decimal).split(".")
    parte_entera = int(parte_entera)
    parte_entera = bin(parte_entera).lstrip("0b")

    parte_entera = norma_bin_hexa(numero_signo, parte_entera)

    return parte_entera


def ingreso_decimal(numero_decimal, tipo_precision):

    if numero_decimal >= 0:
        parte_entera, parte_decimal = flotante(numero_decimal, tipo_precision)
        numero_binario = parte_entera+"."+parte_decimal
        numero_binario, numero_exponente = quitar_punto(numero_binario)

        numero_binario_normalizado = binario_normalizado(numero_decimal)

        signo_binario = signo(numero_decimal)
        exponente_binario = exponente(tipo_precision, numero_exponente)
        mantisa_binario = mantisa(numero_binario, tipo_precision)
        hexadecimal = bin_a_hex(
            signo_binario, exponente_binario, mantisa_binario, tipo_precision)
        
        return (signo_binario, exponente_binario, mantisa_binario, hexadecimal, numero_binario_normalizado)
    else:
        signo_binario = signo(numero_decimal)
        numero_binario_normalizado = binario_normalizado(numero_decimal)
        numero_decimal = abs(numero_decimal)

        parte_entera, parte_decimal = flotante(numero_decimal, tipo_precision)
        numero_binario = parte_entera+"."+parte_decimal
        numero_binario, numero_exponente = quitar_punto(numero_binario)

        exponente_binario = exponente(tipo_precision, numero_exponente)
        mantisa_binario = mantisa(numero_binario, tipo_precision)
        hexadecimal = bin_a_hex(
            signo_binario, exponente_binario, mantisa_binario, tipo_precision)
        return (signo_binario, exponente_binario, mantisa_binario, hexadecimal, numero_binario_normalizado)
