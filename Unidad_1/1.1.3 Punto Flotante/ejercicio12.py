
# Metodo para buscar el primer 1 y colocar una coma después de ese 1
def busqueda_puesta_punto(numero_binario: str):
    posicion = int(numero_binario.find("1"))

    resultado = numero_binario[:posicion+1]+"."+numero_binario[posicion+1:]

    return resultado


# Metodo para quitar la coma
def quitar_punto(numero_binario: str):
    posicion = int(numero_binario.find("."))
    num_exponente = int(len(numero_binario[1:posicion]))
    # numero_decimal = str(numero_decimal)
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

    return texto_final


# Metodo para calcular la mantisa de los 2 tipos de precisiones
def mantisa(numero_binario: str, tipo_precision: int):
    digitos_i = int(len(numero_binario))

    # Proceso para calcular si faltan o sobran digitos
    num = 24 - digitos_i if tipo_precision == 1 else 53 - digitos_i

    # Proceso para calcular la mantissa en un tipo de precision u otro
    if num >= 0:
        mant_sp = str(numero_binario)+"."+"0"*num
        mant_p = quitar_punto(mant_sp)
        mant_f = quitar_uno(mant_p)
    else:
        slicing = slice(0, num)

        mant_sp = str(numero_binario)
        mant_sp = mant_sp[slicing]
        mant_f = quitar_uno(mant_sp)

    return mant_f


# Metodo para representar un numero binario, sin normalizar, normalizado y transformado a hexadecimal
# def norma_bin_hexa(num_dec, num_bin):
#     num_digitos = len(str(num_bin))
#     num_resultado = ""
#     contador = 0

#     # Mostrar numero original
#     print("\nVariable int\n")
#     print("     Numero en binario: "+str(num_bin))

#     num_signo = signo(num_dec)

#     # Proceso para aumentar ceros o quitar digitos de ser necesario
#     if num_digitos <= 31:
#         num_falta = 31-num_digitos
#         num_bin_f = num_signo+"0"*num_falta+str(num_bin)

#         bin_hexa(num_bin_f, contador, num_resultado)
#     else:
#         num_sobra = int(num_digitos)-31
#         slicing = slice(0, -num_sobra)
#         num_bin = str(num_bin)[slicing]
#         num_bin_f = num_signo+str(num_bin)

#         bin_hexa(num_bin_f, contador, num_resultado)


# Metodo usado solamente para transformar un numero binario normalizado a hexadecimal
# def bin_hexa(num_bin_f, contador, num_resultado):
#     print("     Numero normalizado: "+num_bin_f)
#     while (contador < 32):
#         binario = num_bin_f[contador:contador+4]
#         decimal = binario_a_decimal(int(binario))
#         num_hexa = hex(decimal)
#         num_resultado = num_resultado+num_hexa[2:]
#         contador += 4
#     print("     Numero en hexadecimal: "+num_resultado)


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


def ingreso_decimal():
    numero_decimal = input("Ingrese su número: ")
    numero_decimal = float(numero_decimal.replace(",", "."))
    tipo_precision = menu_secundario()

    if numero_decimal >= 0:
        parte_entera, parte_decimal = flotante(numero_decimal, tipo_precision)
        numero_binario = parte_entera+"."+parte_decimal
        numero_binario, numero_exponente = quitar_punto(numero_binario)
        signo_binario = signo(numero_decimal)
        exponente_binario = exponente(tipo_precision, numero_exponente)
        mantisa_binario = mantisa(numero_binario, tipo_precision)
        hexadecimal = bin_a_hex(
            signo_binario, exponente_binario, mantisa_binario, tipo_precision)
        print("Signo: {}\nExponente: {}\nMantisa: {}\nHexadecimal: {}".format
              (signo_binario, exponente_binario, mantisa_binario, hexadecimal))
    else:
        signo_binario = signo(numero_decimal)
        numero_decimal = abs(numero_decimal)
        parte_entera, parte_decimal = flotante(numero_decimal, tipo_precision)
        numero_binario = parte_entera+"."+parte_decimal
        numero_binario, numero_exponente = quitar_punto(numero_binario)
        exponente_binario = exponente(tipo_precision, numero_exponente)
        mantisa_binario = mantisa(numero_binario, tipo_precision)
        hexadecimal = bin_a_hex(
            signo_binario, exponente_binario, mantisa_binario, tipo_precision)
        print("Signo: {}\nExponente: {}\nMantisa: {}\nHexadecimal: {}".format
              (signo_binario, exponente_binario, mantisa_binario, hexadecimal))


def menu_final():
    menu = '''
    ¿Desea ingresar un nuevo número?

        [1] = Si
        [2] = No
            '''

    print(menu)

    while True:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            menu_principal()
        elif opcion == 2:
            exit(1)
        else:
            print("Ingrese una de las opciones disponibles")


def menu_secundario():
    menu = '''
    A continuación, las precisiones que puede usar:

        [1] = Precisión simple
        [2] = Precisión doble
                '''
    print(menu)

    while True:
        opcion = int(input("Seleccione una opción. "))
        if opcion == 1:
            return opcion
        elif opcion == 2:
            return opcion
        else:
            print("Ingrese una de las opciones disponibles")


def menu_principal():
    menu = '''
    Bienvenido a la calculadora del formato IEEE 754 desde binario y decimal a hexadecimal
    A continuación selecciona una de las opciones para continuar el proceso:
            
        [1] = Ingreso de dato decimal
        [2] = Ingreso de dato binario
        [3] = Ingreso de dato decimal con exponente
        [4] = Salir'''

    print(menu)

    while True:
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            ingreso_decimal()
            menu_final()
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            exit(1)
        else:
            print("Ingrese una de las opciones presentadas")


if __name__ == "__main__":
    # Llamada a menu principal
    menu_principal()
