numero = int(input("Introduce el numero a calcular (0-400) "))


def calcularFactorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado


for i in range(0, numero + 1):
    print(i, "! =", str(calcularFactorial(i)))
