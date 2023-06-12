#HEXADECIMAL A DECIMAL
def hexadecimal_a_decimal(hexadecimal):
    decimal = int(hexadecimal, 16)
    return decimal

hexadecimal = input("Ingrese un número hexadecimal: ")
decimal = hexadecimal_a_decimal(hexadecimal)
print("El número decimal correspondiente es:", decimal)