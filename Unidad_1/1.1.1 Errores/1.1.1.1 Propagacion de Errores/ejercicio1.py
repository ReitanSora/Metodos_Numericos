import matplotlib.pyplot as plt
import numpy as np


# Funcion de la expresion base para representarla
def e(x):
    return pow(np.e, x)/((pow(np.e, x))-1)


# Funcion para el calculo de la expresion
def propagacion_errores():
    exponente = int(
        input("Ingrese un número mayor a 250 para realizar el cálculo: "))
    if exponente > 250:
        ceros = int(len(str(exponente)))-1
        exponente_modificado = exponente/pow(10, ceros)

        for i in range(0, ceros):
            numerador = (pow(np.e, exponente_modificado)**10)
            denominador = (pow(np.e, exponente_modificado)**10)
            numerador = numerador**10
            denominador = denominador**10

        respuesta = numerador/(denominador-1)
        print("La respuesta es: {}".format(respuesta))

        # Codigo para la representacion de la tabla
        x = np.linspace(exponente-5, exponente+5)
        plt.scatter(exponente, respuesta, c="red", label="Punto de respuesta")
        plt.plot(x, e(x), label="Función e^x/(e^x)-1", c="black")
        plt.grid(alpha=0.3, lw=1.75, ls="--")
        plt.yticks(range(-1, 4, 1))
        plt.xticks(range(exponente-5, exponente+6, 1))
        plt.annotate("[{},{}]".format(exponente, respuesta),
                     xy=(exponente+0.25, respuesta+0.25))
        # Etiquetas e informacion de la tabla
        plt.title("Representación de la Función e^x/(e^x)-1\nen el rango [{},{}]".format(
            exponente-5, exponente+5), c="red")
        plt.legend(loc="upper left")
        plt.xlabel("Valor de 'x'", c="grey")
        plt.ylabel("Resultado de la ecuación", c="grey")
        plt.show()
    else:
        print("Ingrese un número correcto")


if __name__ == "__main__":
    propagacion_errores()
