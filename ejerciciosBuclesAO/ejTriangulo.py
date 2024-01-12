# Pedir al usuario que ingrese el nivel deseado
nivel = int(input("Ingrese un número entre 2 y 40 para el nivel del triángulo: "))

# Imprimir el triángulo
for i in range(1, nivel + 1):
        espacios = nivel - i
        asteriscos = 2 * i - 1
        linea = (' ' * espacios) + ('X' * asteriscos)
        print(linea)
