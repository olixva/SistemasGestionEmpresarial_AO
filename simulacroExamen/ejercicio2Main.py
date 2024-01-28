from ejercicio2ModuloSlicing import Recortes


def MostrarMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="\t")
        print()


matriz_original = [[1, 2, 3], [4, 5], [6, 7], [8, 9, 10]]
tupla_resultado = Recortes(matriz_original)

print("Matriz Original")
MostrarMatriz(matriz_original)

print("Matriz Recortada")
MostrarMatriz(tupla_resultado[0])

print("Matriz Sobrante")
MostrarMatriz(tupla_resultado[1])
