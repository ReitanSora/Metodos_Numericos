# double A;
# float B;
# int C;

# A = pow(2,28) + 5;
# B = (float) A;
# C = (int) A;

def decimal_a_binario(decimal):
    binario = 0
    i = 0

    while (decimal > 0):
        residuo = decimal % 2
        decimal = int(decimal/2)
        binario = binario + residuo * pow(10, i)
        i += 1

    return binario


def binario_a_decimal(binario):
    decimal = 0
    i = 0

    while (binario > 0):
        digito = binario % 10
        binario = int(binario/10)
        decimal = decimal + digito*pow(2, i)
        i += 1

    return decimal


def busqueda_puesta_punto(num_binario):
    texto_num = str(num_binario)
    posicion = int(texto_num.find("1"))

    resultado = texto_num[:posicion+1]+","+texto_num[posicion+1:]

    return resultado


def quitar_punto(texto):
    posicion = int(texto.find(","))
    resultado = texto[:posicion]+texto[posicion+1:]

    return resultado


def quitar_uno(numero):
    posicion = int(numero.find("1"))
    resultado = numero[:posicion]+numero[posicion+1:]

    return resultado


def signo(num_decimal):
    signo_binario = ""

    if num_decimal >= 0:
        signo_binario = "0"
    else:
        signo_binario = "1"

    return signo_binario


def exponente(num_binario, tipo_pre):
    texto_proceso = busqueda_puesta_punto(num_binario)
    posicion = int(texto_proceso.find(","))
    num_exponente = int(len(texto_proceso[posicion+1:]))

    if tipo_pre == 1:
        exp_binario = 127 + num_exponente
    else:
        exp_binario = 1023 + num_exponente

    texto_final = str(decimal_a_binario(exp_binario))

    return texto_final


def mantissa(num_binario, tipo_pre):
    digitos_i = int(len(str(num_binario)))

    if tipo_pre == 1:
        num = 24-digitos_i
    else:
        num = 53-digitos_i

    if num >= 0:
        mant_sp = str(num_binario)+","+"0"*num
        mant_p = quitar_punto(mant_sp)
        mant_f = quitar_uno(mant_p)
    else:
        slicing = slice(0, num)

        mant_sp = str(num_binario)
        mant_sp = mant_sp[slicing]
        mant_f = quitar_uno(mant_sp)

    return mant_f


def norma_bin_hexa(num_dec, num_bin):
    num_digitos = len(str(num_bin))
    num_resultado = ""
    contador = 0

    print("\nVariable int\n")
    print("     Numero en binario: "+str(num_bin))

    if num_dec >= 0:
        num_signo = "0"
    else:
        num_signo = "1"

    if num_digitos <= 31:
        num_falta = 31-num_digitos
        num_bin_f = num_signo+"0"*num_falta+str(num_bin)

        bin_hexa(num_bin_f, contador, num_resultado)
    else:
        num_sobra = int(num_digitos)-31
        slicing = slice(0, -num_sobra)
        num_bin = str(num_bin)[slicing]
        num_bin_f = num_signo+str(num_bin)

        bin_hexa(num_bin_f, contador, num_resultado)


def bin_hexa(num_bin_f, contador, num_resultado):
    print("     Numero normalizado: "+num_bin_f)
    while (contador < 32):
        binario = num_bin_f[contador:contador+4]
        decimal = binario_a_decimal(int(binario))
        num_hexa = hex(decimal)
        num_resultado = num_resultado+num_hexa[2:]
        contador += 4
    print("     Numero en hexadecimal: "+num_resultado)


def bin_a_hex(num_s_bin, num_e_bin, num_m_bin, tipo_pre):
    cadena_binario = num_s_bin+num_e_bin+num_m_bin
    contador = 0
    resultado = ""

    if tipo_pre == 1:
        while (contador < 32):
            binario = cadena_binario[contador:contador+4]
            decimal = binario_a_decimal(int(binario))
            hexa = hex(decimal)
            resultado = resultado+hexa[2:]
            contador += 4
    else:
        while (contador < 64):
            binario = cadena_binario[contador:contador+4]
            decimal = binario_a_decimal(int(binario))
            hexa = hex(decimal)
            resultado = resultado+hexa[2:]
            contador += 4

    return resultado


def prints(num_dec, num_bin, tipo_pre):
    tipo = "Doble" if tipo_pre == 2 else "Simple"
    variable = "double" if tipo_pre == 2 else "float"

    print("\nPresicion " + tipo+"-Variable " + variable+"\n")
    print("     Signo: " + signo(num_dec))
    print("     Exponente: "+exponente(num_bin, tipo_pre))
    print("     Mantissa: "+mantissa(num_bin, tipo_pre))
    print("     La representación en binario es: "+signo(num_dec) +
          " "+exponente(num_bin, tipo_pre)+" "+mantissa(num_bin, tipo_pre))
    print("     La representación en hexadecimal es: " + bin_a_hex(signo(num_dec),
          exponente(num_bin, tipo_pre), mantissa(num_bin, tipo_pre), tipo_pre))


# VARIABLES
A = pow(2, 28) + 5
A_binario = decimal_a_binario(A)

# PRINTS
print("\nValores iniciales\n")
print("     Decimal: "+str(A))
print("     Binario: "+str(A_binario))

prints(A, A_binario, 2)
prints(A, A_binario, 1)
norma_bin_hexa(A, A_binario)
