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

def metodo_biseccion(fun, a, b, eps=None, steps=100):
    # no se puede aplicar el metodo de biseccion
    if fun(a) * fun(b) >= 0:
        # print("No se puede aplicar el método de bisección")
        return None

    # calcular numero de pasos en base a epsilon
    if eps is not None:
        steps = math.ceil(math.log((b - a) / eps) / math.log(2))

    # metodo de biseccion
    for n in range(steps + 1):
        m = (a + b) / 2

        if fun(m) == 0:
            return m
        elif fun(a) * fun(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2
