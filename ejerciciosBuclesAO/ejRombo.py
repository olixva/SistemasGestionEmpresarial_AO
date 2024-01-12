# Pedir al usuario que ingrese el nivel deseado
nivel = int(input("Ingrese un número entre 2 y 40 para el nivel del rombo: "))

# Imprimir el rombo, no es como lo pedia el ejercicio pero es lo unico que he podido hacer
for i in range(0, nivel ):
        espacios = nivel - i
        asteriscos = 2 * i - 1
        linea = (' ' * espacios) + ('X' * asteriscos)
        print(linea)
        
for i in range(nivel, 0, -1):
        espacios = nivel - i
        asteriscos = 2 * i - 1
        linea = (' ' * espacios) + ('X' * asteriscos)
        print(linea)
        
        
