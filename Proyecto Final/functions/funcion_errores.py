
def calculo_errores(valor_verdadero: float):

    valor_aproximado = round(valor_verdadero, 1)

    error_absoluto = abs(valor_aproximado-valor_verdadero)
    error_relativo = error_absoluto/valor_aproximado

    return valor_aproximado, error_absoluto, error_relativo
