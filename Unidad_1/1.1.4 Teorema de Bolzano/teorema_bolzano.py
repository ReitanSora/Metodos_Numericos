def bolzano(f, a, b, epsilon=0.0001, max_iter=100):
    """
    Aplica el teorema de Bolzano para encontrar una aproximación de una raíz de la función f en el intervalo [a, b].

    Args:
        f (function): La función para la cual queremos encontrar la raíz.
        a (float): El extremo izquierdo del intervalo.
        b (float): El extremo derecho del intervalo.
        epsilon (float): La tolerancia de error aceptada para la aproximación de la raíz (opcional, valor predeterminado: 0.0001).
        max_iter (int): El número máximo de iteraciones permitidas (opcional, valor predeterminado: 100).

    Returns:
        float: Una aproximación de la raíz de la función f en el intervalo [a, b], o None si no se encontró ninguna raíz.
    """
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        print("La función no cumple con las condiciones del teorema de Bolzano en el intervalo dado.")
        return None

    x = (a + b) / 2
    fx = f(x)
    iteration = 0

    while abs(fx) > epsilon and iteration < max_iter:
        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

        x = (a + b) / 2
        fx = f(x)
        iteration += 1

    if abs(fx) <= epsilon:
        return x
    else:
        print("Se alcanzó el número máximo de iteraciones sin convergencia.")
        return None

# Ejemplo de uso:
def f(x):
    return eval(input("Ingrese la función f(x): "))

a = float(input("Ingrese el extremo izquierdo del intervalo [a, b]: "))
b = float(input("Ingrese el extremo derecho del intervalo [a, b]: "))

root = bolzano(f, a, b)

if root is not None:
    print("Aproximación de la raíz:", root)
else:
    print("No se encontró ninguna raíz en el intervalo dado.")

