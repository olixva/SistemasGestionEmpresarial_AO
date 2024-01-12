import random

#Creamos 100 numeros aleatorios entre 0 y 99 y los guardamos en un array
numeros = []
for i in range(100):
    numero = random.randint(0,99)
    numeros.append(numero)

#Ahora comprobamos cuántos números están comprendidos en los intervalos [0-19], [20-39], [40-59], [60-79] y [80-99]
intervalos = [0,0,0,0,0]
for numero in numeros:
    if numero < 20:
        intervalos[0] += 1
    elif numero < 40:
        intervalos[1] += 1
    elif numero < 60:
        intervalos[2] += 1
    elif numero < 80:
        intervalos[3] += 1
    else:
        intervalos[4] += 1
        
#Imprimimos los numeros que hay en cada intervalo y el total
print("Intervalo [0-19]:", intervalos[0])
print("Intervalo [20-39]:", intervalos[1])
print("Intervalo [40-59]:", intervalos[2])
print("Intervalo [60-79]:", intervalos[3])
print("Intervalo [80-99]:", intervalos[4])
print("Total:", sum(intervalos))

