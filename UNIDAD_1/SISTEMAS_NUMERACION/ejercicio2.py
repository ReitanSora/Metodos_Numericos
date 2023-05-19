#DE DECIMAL A BINARIO

decimal= 27025
binario=0
i=0

while(decimal>0):
    residuo=decimal%2
    binario+= residuo *(10**i)
    decimal //=2
    i+=1

print("El valor de decimal a binario es: "+str(binario))