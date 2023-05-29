# Literal a) Representacion 32 bits no normalizados

total_values = 2**23 - 1  # Total de combinaciones posibles para los bits de la mantisa (2^23 - 1)
normalized_values = 2**23 - 2  # Número de valores normalizados (2^23 - 2)

# calcular el numero no normalizado 
non_normalized_values = total_values - normalized_values
print("Número de valores no normalizados:", non_normalized_values) # imprime el valor no normalizado
# Literal b) En un computador de 32 bits se puede representar de forma exacta

value_int = 2**27 + 1 # variable de tipo int
value_float = float(2**27 + 1) # variable de tipo float

# representacion exacta de las 2 variables
print("Valor exacto en tipo int:", value_int)
print("Valor aproximado en tipo float:", value_float)

# Literal c) Represente en el estándar IEEE 754 de doble precisión el valor 12.5. Exprese el resultado en hexadecimal
import struct #

value = 12.5
bytes_representation = struct.pack('!d', value) # Convertir 12.5 a su representación en IEEE 754 de doble precisión
hex_representation = bytes_representation.hex() # Convertir los bits a hexadecimal

print("Representación hexadecimal:", hex_representation)