# Modulo con funcion de recortes
import sys


def Recortes(matriz):
    filas = len(matriz)

    # Obtenemos el numero de columnas mas pequeno
    columnas_min = sys.maxsize
    for fila in matriz:
        if len(fila) < columnas_min:
            columnas_min = len(fila)

    # Cogemos el mas pequeno para determinar el tamano de la matriz
    tamano_matriz = columnas_min if columnas_min < filas else filas

    matriz_recorte = []
    matriz_sobrante = []
    # Recorremos la matriz y la recortamos
    for f in range(len(matriz)):
        fila_recorte = []
        fila_sobrante = []
        for c in range(len(matriz[f])):

            if c < tamano_matriz:
                fila_recorte.append(matriz[f][c])
            else:
                fila_sobrante.append(matriz[f][c])

        if len(fila_recorte) > 0 and f < tamano_matriz:  # Si la fila esta dentro del rango del recorte la insertamos en la matriz de recorte
            matriz_recorte.append(fila_recorte)
        else:
            fila_sobrante = fila_recorte + fila_sobrante  # Si no, la concatenamos con el recorte que ya teniamos de columnas
        if len(fila_sobrante) > 0: matriz_sobrante.append(fila_sobrante)
        # Y la insertamos en la matriz de sobrantes si no esta vacia la fila

    return (matriz_recorte, matriz_sobrante)
