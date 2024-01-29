import random


# Funcion que infecta si es posible a 4 personas y devuelve el numero de personas que ha infectado
def Infectar(ciudad, fila_infectado, columna_infectado, dia):
    infectados = 0

    # ARRIBA
    if fila_infectado - 1 >= 0 and ciudad[fila_infectado - 1][columna_infectado] == "SANO":
        ciudad[fila_infectado - 1][columna_infectado] = f"I-{dia} "
        infectados += 1
    # DERECHA
    if columna_infectado + 1 <= len(ciudad[0]) - 1 and ciudad[fila_infectado][columna_infectado + 1] == "SANO":
        ciudad[fila_infectado][columna_infectado + 1] = f"I-{dia} "
        infectados += 1
    # ABAJO
    if fila_infectado + 1 <= len(ciudad) - 1 and ciudad[fila_infectado + 1][columna_infectado] == "SANO":
        ciudad[fila_infectado + 1][columna_infectado] = f"I-{dia} "
        infectados += 1
    # IZQUIERDA
    if columna_infectado - 1 >= 0 and ciudad[fila_infectado][columna_infectado - 1] == "SANO":
        ciudad[fila_infectado][columna_infectado - 1] = f"I-{dia} "
        infectados += 1

    return infectados


def Contagiar(ciudad):
    dia = 0
    contagiados = 1
    personas_totales = len(ciudad) * len(ciudad[0])

    while contagiados < personas_totales:
        MostarCiudad(ciudad, dia)
        dia += 1

        fila = 0
        while fila < len(ciudad) and contagiados < personas_totales:

            columna = 0
            while columna < len(ciudad[0]) and contagiados < personas_totales:

                if ciudad[fila][columna] != "SANO" and ciudad[fila][columna] != f"I-{dia} ":
                    contagiados += Infectar(ciudad, fila, columna, dia)
                columna += 1
            fila += 1

    MostarCiudad(ciudad, dia)
    return dia


def MostarCiudad(ciudad, dia):
    print(f"\nDia {dia}:")

    for i in range(len(ciudad)):
        print(end="\n\t\t")
        for j in range(len(ciudad[0])):
            print(ciudad[i][j], end="\t")


def GenerarCiudad(n_filas, nColumnas):
    # Generamos la matriz de la ciudad
    ciudad = []
    for i in range(n_filas):
        fila = []
        for j in range(nColumnas):
            fila.append("SANO")
        ciudad.append(fila)

    # Insertamos el infectado
    fila_infectado = random.randint(0, n_filas - 1)
    columna_infectado = random.randint(0, nColumnas - 1)
    ciudad[fila_infectado][columna_infectado] = "I-0 "

    return ciudad


n_filas = int(input("Introduce el numero de filas: "))
n_columnas = int(input("Introduce el numero de columnas: "))
ciudad_juego = GenerarCiudad(n_filas, n_columnas)
print(f"\nDias totales:  {Contagiar(ciudad_juego)}")
