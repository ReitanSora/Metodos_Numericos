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


def calculo_errores(valor_verdadero: float):

    valor_aproximado = round(valor_verdadero, 1)

    error_absoluto = abs(valor_aproximado-valor_verdadero)
    error_relativo = error_absoluto/valor_aproximado

    return valor_aproximado, error_absoluto, error_relativo
