# Definir las dimensiones de la matriz
filas = 3
columnas = 4

# Inicializar la matriz con ceros
matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(0)
    matriz.append(fila)

# Rellenar la matriz con valores
valor = 1
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = valor
        valor += 1

# Imprimir la matriz
for fila in matriz:
    print(fila)
