'''
Tema: Métodos Numéricos
#Grupo #
#Integrantes:

•	Kevin Josue Amaguaña Rivadeneira
•	Priscila Veronica Chisag Pillajo
•	Andy RIcardo Galarza Morales
•	Stiven Anthony Pilca Sánchez

#Carrera: Ingeniería en Sistemas de la información
#Paralelo: SI4 - 002
'''


# función para convertir de binario a decimal
def binario_decimal(numero_binario: int) -> int:
    i = int()
    decimal = int()

    while (numero_binario > 0):
        digito = numero_binario % 10
        numero_binario = int(numero_binario/10)
        decimal = decimal + digito*(2**i)
        i += 1

    return decimal

# funcion para convertir de decimal a binario


def decimal_binario(numero_decimal: int) -> int:
    binario = int()
    i = int()

    while (numero_decimal > 0):
        residuo = numero_decimal % 2
        numero_decimal = int(numero_decimal/2)
        binario = binario + residuo * (10**i)
        i += 1

    return binario
