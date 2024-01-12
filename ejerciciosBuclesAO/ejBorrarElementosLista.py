#Eliminar los elementos negativos de una lista de números enteros.
L = [1, -5, 3, 0, -9]

for x in L:
    if x < 0:
        del L[L.index(x)]
        
print(L)