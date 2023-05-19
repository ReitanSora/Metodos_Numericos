octal=42
decimal=0
i=0

while(octal>0):
    digito= octal%10
    decimal+= digito*(8**i)
    octal //=10
    i+=1


print("El valor de octal a decimal es: "+str(decimal))