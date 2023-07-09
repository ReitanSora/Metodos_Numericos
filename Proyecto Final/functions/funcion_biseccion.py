import matplotlib.pyplot as plt
import numpy as np
import math


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
        # valores = np.array([m])
        # valores = np.append(valores, m)

        if fun(m) == 0:
            return m
        elif fun(a) * fun(m) < 0:
            b = m
        else:
            a = m
        # plt.scatter(a, b, c="red")

    # plt.scatter(m, m, label="Resultado final")
    # plt.grid(alpha=0.3, lw=1.75, ls="--")
    # plt.yticks(range(0, 11, 1))
    # plt.xticks(range(0, 11, 1))
    # plt.annotate("[{}]".format(m), xy=(m+0.25, m-0.25))
    # plt.title("Representación de la Función de Bisección", c="red")
    # plt.legend(loc="upper left")
    # plt.xlabel("Valor de 'x'", c="grey")
    # plt.ylabel("Resultado de la ecuación", c="grey")
    # plt.show()

    return (a + b) / 2


# def menu_principal():
#     menu='''
#     Bienvenido al calculo de raices con el método de Bisección para ecuaciones cuadráticas
#     A continuación selecciona una de las opciones para continuar el proceso:

#         [1] = Ingreso de datos
#         [2] = Salir
#         '''
#     print(menu)

#     while True:
#         try:
#             opcion = int(input("Seleccione una opción: "))

#         except ValueError:
#             opcion=0

#         if opcion==1:
#             print("Ax^2 + Bx + C")
#             try:
#                 a = int(input("Ingrese el valor para A: "))
#                 b = int(input("Ingrese el valor para B: "))
#                 c = int(input("Ingrese el valor para C: "))
#                 signo1= input("Ingrese el primer signo: ")
#                 signo2= input("Ingrese el segundo signo: ")
#                 rango_a = int(input("Ingrese desde que número desea calcular"))
#                 rango_b = int(input("Ingrese hasta que número desea calcular"))

#             except ValueError:
#                 menu_principal()

#             if (signo1 == "+") and (signo2 == "+"):
#                 f = lambda x: a*(pow(x,2)) + b*x + c
#             elif (signo1 == "+") and (signo2 == "-"):
#                 f = lambda x: a*(pow(x,2)) + b*x - c
#             elif (signo1 == "-") and (signo2 == "+"):
#                 f = lambda x: a*(pow(x,2)) - b*x + c
#             elif (signo1 == "-") and (signo2 == "-"):
#                 f = lambda x: a*(pow(x,2)) - b*x - c
#             else:
#                 print("* * * * * *Ingrese datos correctos * * * * * *")

#             biseccion(f, rango_a, rango_b, 1e-6)
#             menu_principal()

#         elif opcion == 2:
#             exit(1)
#         else:
#             print("* * * * * * Ingrese una opción correcta * * * * * *")

# if __name__=="__main__":
#     menu_principal()
