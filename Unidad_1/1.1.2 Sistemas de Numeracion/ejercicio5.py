#DE DECIMAL A BINARIO

def decimal_a_binario(decimal):
    binario = ''
    
    if decimal == 0:
        binario = '0'
    
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2
    
    return binario

decimal = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(decimal)
print(f"El número binario correspondiente es: {binario}")