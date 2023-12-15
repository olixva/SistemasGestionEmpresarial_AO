import random

print("Piense en un número super golfo del 0 al 100 ")
input("Presione ENTER para comenzar")

limite_inferior = 0
limite_superior = 100
intentos = 0
respuesta = ''

while respuesta != 'i':
    #Generamos el número aleatorio
    numero_a_adivinar = random.randint(limite_inferior, limite_superior)
    print("¿Es el",{numero_a_adivinar},"? (m - mayor, n - menor, i - igual)")
    respuesta = input()

    if respuesta == 'm':
        # Cambiamos el límite inferior si el número es mayor
        limite_inferior = numero_a_adivinar + 1
    elif respuesta.lower() == 'n':
        # Cambiamos el límite superior si el número es menor
        limite_superior = numero_a_adivinar - 1

    intentos += 1

print("¡Soy una maquina (xd), lo he acertado en nada mas y nada menos que ",intentos, "intentos!")
