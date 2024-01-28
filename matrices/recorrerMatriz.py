# Generamos la matriz de la ciudad
matriz = []
for i in range(10):  # Filas
    fila = []
    for j in range(7):  # Columnas
        fila.append("SANO")
    matriz.append(fila)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end=" ")
    print()
