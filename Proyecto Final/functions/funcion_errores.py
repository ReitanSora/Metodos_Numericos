# a = 0.5 * pow(10, 2)
# a1 = 0.51 * pow(10, 2)


def errores(valor_verdadero, valor_aproximado):

    valor_verdadero *= pow(10, 2)
    valor_aproximado *= pow(10, 2)

    error_absoluto = abs(valor_aproximado-valor_verdadero)
    error_relativo = error_absoluto/valor_aproximado

    return error_absoluto, error_relativo
