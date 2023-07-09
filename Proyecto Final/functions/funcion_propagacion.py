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

import numpy as np


# Funcion de la expresion base para representarla
def e(x):
    return pow(np.e, x)/((pow(np.e, x))-1)


# Funcion para el calculo de la expresion
def propagacion_errores(exponente):
    if exponente > 250:
        ceros = len(str(exponente))-1
        exponente_modificado = int(exponente)/pow(10, ceros)

        for i in range(0, ceros):
            numerador = (pow(np.e, exponente_modificado)**10)
            denominador = (pow(np.e, exponente_modificado)**10)
            numerador = numerador**10
            denominador = denominador**10

        respuesta = numerador/(denominador-1)

        return respuesta
    else:
        return None

