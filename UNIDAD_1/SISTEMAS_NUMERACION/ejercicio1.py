# DE BINARIO A DECIMAL

binario = 101111
decimal = 0
i = 0

while (binario > 0):
    digito = binario % 10
    binario = int(binario/10)
    decimal = decimal + digito*(2**i)
    i += 1

print("El número en decimal es: "+str(decimal))
