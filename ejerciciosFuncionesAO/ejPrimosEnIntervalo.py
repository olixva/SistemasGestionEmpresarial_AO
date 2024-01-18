numero = int(input("Introduce el numero "))


def es_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


print(f"Numeros primos [2-{numero}]:")
# Agregamos los numeros a una lista de primos
primos = list()
for i in range(2, numero):
    if es_primo(i):
        primos.append(i)

# Recorremos la lista, en caso de que sea el penultimo elemento agregamos un "y"
for i, primo in enumerate(primos):
    if i == len(primos) - 1:
        print(primos[i], end="")
    elif i == len(primos) - 2:
        print(primos[i], end=" y ")
    else:
        print(primos[i], end=", ")
