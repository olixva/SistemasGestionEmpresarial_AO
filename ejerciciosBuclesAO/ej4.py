numero = int(input(" Introduce un numero entero positivo "))

# Recorremos los numeros desde el 0 hasta el numero introducido 
# si es par lo sumamos a la variable suma
suma = 0
for i in range(0, numero+1, 2):
    suma += i

print(suma)