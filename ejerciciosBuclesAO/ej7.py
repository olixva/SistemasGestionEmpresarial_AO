numero = -1
mayor = 0

#Pedimos un numero entero o decimal hasta que sea 0
while numero != 0:
    numero = float(input("Introduzca un número (cero para terminar): "))
    if numero > mayor:
        mayor = numero

print("Mayor:", mayor)