#
# 

filas = int(input("Ingrese el número de filas:"))
columnas = int(input("Ingrese el número de columnas:"))

# Creamos la matriz 
matriz = []

# Pedimos los datos de la matriz
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        matriz[i].append(int(input("Ingrese el valor de la posición {i},{j}: ")))
        
# Imprimimos la matriz
print(matriz)