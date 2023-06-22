'''
Tema: Algoritmos de ordenamiento(iterativos y recursivos)
#Grupo #3
#Integrantes:
#- Stiven Pilca           CI: 1750450262
#- Tulcanza Juan          CI: 1755962485
#Carrera: Ingeniería en Sistemas de la información
#Paralelo: SI4 - 002
#Fecha de entrega: 21/06/2023
'''

import heapq


# ordenamiento burbuja
def burbuja(arreglo):
    n = len(arreglo)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arreglo[j + 1] < arreglo[j]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]


# ordenamiento inserccion
def inserccion(arreglo):
    n = len(arreglo)
    for i in range(1, n):
        aux = arreglo[i]
        j = i - 1
        while j >= 0 and arreglo[j] > aux:
            arreglo[j + 1] = arreglo[j]
            j -= 1
        arreglo[j + 1] = aux


# ordenamiento seleccion
def seleccion(arreglo):
    n = len(arreglo)
    for i in range(n - 1):
        aux = i
        for j in range(i + 1, n):
            if arreglo[j] < arreglo[aux]:
                aux = j
        arreglo[i], arreglo[aux] = arreglo[aux], arreglo[i]


# ordenamiento shellSort
def shellSort(arreglo):
    n = len(arreglo)
    m = n // 2
    while m > 0:
        for i in range(m, n):
            aux = arreglo[i]
            j = i
            while j >= m and arreglo[j - m] > aux:
                arreglo[j] = arreglo[j - m]
                j -= m
            arreglo[j] = aux
        m //= 2


# ordenamiento quickSort
def quickSort(arreglo, izquierda=0, derecha=None):
    if derecha is None:
        derecha = len(arreglo) - 1
    if izquierda < derecha:
        n = arreglo[izquierda]  # tomamos primer elemento como pivote
        i = izquierda  # i realiza la búsqueda de izquierda a derecha
        j = derecha  # j realiza la búsqueda de derecha a izquierda
        aux = 0

        while i < j:  # mientras no se crucen las búsquedas
            while arreglo[i] <= n and i < j:
                i += 1  # busca elemento mayor que pivote
            while arreglo[j] > n:
                j -= 1  # busca elemento menor que pivote
            if i < j:  # si no se han cruzado
                aux = arreglo[i]  # los intercambia
                arreglo[i] = arreglo[j]
                arreglo[j] = aux

        # se coloca el pivote en su lugar de forma que tendremos
        arreglo[izquierda] = arreglo[j]
        arreglo[j] = n  # los menores a su izquierda y los mayores a su derecha

        quickSort(arreglo, izquierda, j - 1)  # ordenamos subarray izquierdo
        quickSort(arreglo, j + 1, derecha)  # ordenamos subarray derecho


# ordenamiento heapSort
def heapSort(arr):
    heapq.heapify(arr)
    result = []
    while arr:
        result.append(heapq.heappop(arr))
    return result


# ordenamiento MergeSort
def mergeSort(arreglo, izquierda, derecha):
    if izquierda < derecha:
        m = (izquierda + derecha) // 2
        mergeSort(arreglo, izquierda, m)
        mergeSort(arreglo, m + 1, derecha)
        mergeS(arreglo, izquierda, m, derecha)


def mergeS(arreglo, izquierda, m, derecha):
    i, j, k = izquierda, m + 1, izquierda
    aux = [0] * len(arreglo)  # array auxiliar
    for idx in range(izquierda, derecha + 1):
        aux[idx] = arreglo[idx]
    while i <= m and j <= derecha:
        if aux[i] <= aux[j]:
            arreglo[k] = aux[i]
            i += 1
        else:
            arreglo[k] = aux[j]
            j += 1
        k += 1
    while i <= m:
        arreglo[k] = aux[i]
        i += 1
        k += 1

# ordenamiento Shellsort recursivo
def shellsort_recursivo(arr):
    n = len(arr)  # Obtiene la longitud del arreglo
    gap = n // 2  # Calcula el tamaño inicial del espacio entre los elementos a comparar

    def shell_insertion_sort(arr, gap):
        # Implementa una variante del algoritmo de ordenamiento por inserción que trabaja con un espacio (gap) entre elementos
        for i in range(gap, n):
            temp = arr[i]  # Almacena el valor del elemento actual
            j = i
            while j >= gap and arr[j - gap] > temp:
                # Desplaza los elementos hacia la derecha mientras sean mayores que el valor actual
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp  # Coloca el valor actual en su posición correcta

    def shell_sort_helper(arr, gap):
        if gap > 0:
            shell_sort_helper(arr, gap // 2)  # Realiza la llamada recursiva con un nuevo tamaño de gap
            shell_insertion_sort(arr, gap)  # Aplica el algoritmo de ordenamiento por inserción con el gap actual

    shell_sort_helper(arr, gap)  # Inicia el ordenamiento recursivo