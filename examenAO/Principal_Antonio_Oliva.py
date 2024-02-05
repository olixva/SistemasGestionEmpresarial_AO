# Examen 05/02/2024 Antonio Oliva Carceles
from Examen_Utilidades import crearmatriz, visualizarmatriz, mover
import random


# Funcion de introducir jugadores
def IntroducirJugadores():
    # Pedimos el numero de jugadores hasta que sea par
    numero_jugadores = int(input("Introduce el numero de jugadores (PAR): "))
    while numero_jugadores % 2 != 0:
        print("El numero de jugadores debe ser PAR, intentelo de nuevo")
        numero_jugadores = int(input("Introduce el numero de jugadores (PAR): "))

    # Creamos los equipos y sus tamanos
    equipo_1 = {}
    equipo_2 = {}
    tamano_equipo = numero_jugadores / 2

    # Vamos agregando aleatoriamente a un equipo hasta que este lleno
    indice = 1
    while indice < numero_jugadores + 1 and len(equipo_1) < tamano_equipo and len(equipo_2) < tamano_equipo:
        nombre_jugador = input("Introduce el nombre del jugador: ")
        equipo_jugador = random.randint(0, 1)

        if equipo_jugador == 0:
            equipo_1[indice] = nombre_jugador
        else:
            equipo_2[indice] = nombre_jugador
        indice += 1

    # Cuando un equipo esta lleno llenamos el otro
    equipo_rellenar = equipo_1 if len(equipo_1) < tamano_equipo else equipo_2
    for i in range((numero_jugadores + 1) - indice):
        nombre_jugador = input("Introduce el nombre del jugador: ")
        equipo_rellenar[indice] = nombre_jugador
        indice += 1

    return [equipo_1, equipo_2]


def MostrarEquipos(equipos):
    # Mostramos los equipos
    print("Equipos participantes\n---------------------")

    for equipo in equipos:
        print(f"\nEquipo {equipos.index(equipo)}: ", end="")
        i = 0
        for key, value in equipo.items():
            print(f"{key}. {value}", end="")
            i += 1
            if i != len(equipo): print(" - ", end="")  # Si no estamos en el ultimo mostramos guion separador (-)
    print("\n")


def JugadoresTablero(tablero):
    posiciones = {}
    i = 1
    while i < (len(tablero)) + 1:  # Calculamos el numero de jugadores (+1) porque empieza en 1
        # Generamos una posicion aleatoria para el jugador
        fila_aleatoria = random.randint(0, len(tablero) - 1)
        columna_aleatoria = random.randint(0, len(tablero) - 1)

        # Lo metemos si no esta ocupada
        if tablero[fila_aleatoria][columna_aleatoria] == '-':
            tablero[fila_aleatoria][columna_aleatoria] = i
            posiciones[i] = [fila_aleatoria, columna_aleatoria]
            i += 1

    return posiciones


def Jugar(equipos, tablero, posicion_jugadores):
    i = 1
    while i < len(posicion_jugadores) + 1:
        jugador = i
        posicion = posicion_jugadores[jugador]

        orientacion = input(f"Jugador {jugador}, desea mover por filas (F) o columnas (C): ")
        numero_salto = random.randint(1, len(equipos[0]) * 2)

        # Guardamos la posicion nueva
        nueva_posicion = mover(tablero, posicion, orientacion, numero_salto)

        # Si esta vacio nos movemos
        if (tablero[nueva_posicion[0]][nueva_posicion[1]] == "-"):

            tablero[posicion[0]][posicion[1]] = "-"
            tablero[nueva_posicion[0]][nueva_posicion[1]] = jugador

        # Si no esta vacio y no es en el que estamos ya, lo elimina
        elif (tablero[nueva_posicion[0]][nueva_posicion[1]] != "-"
              and tablero[nueva_posicion[0]][nueva_posicion[1]] != jugador):

            posicion_jugadores.pop(tablero[nueva_posicion[0]][nueva_posicion[1]])
            tablero[posicion[0]][posicion[1]] = "-"
            tablero[nueva_posicion[0]][nueva_posicion[1]] = jugador

        visualizarmatriz(tablero)
        i += 1


def ObtenerGanador(equipos, posicion_jugadores):
    jugadores_vivos_1 = 0
    jugadores_vivos_2 = 0

    # Contamos los jugadores vivos de cada equipo
    for jugador in posicion_jugadores.keys():
        if jugador in equipos[0]:
            jugadores_vivos_1 += 1
        else:
            jugadores_vivos_2 += 1

    ganador = ""
    if jugadores_vivos_1 > jugadores_vivos_2:
        ganador = "El equipo 1 ha ganado"
    elif jugadores_vivos_2 > jugadores_vivos_1:
        ganador = "El equipo 2 ha ganado"
    else:
        ganador = "Han quedado empate"

    return f"{ganador} \nHan sobrevibido {jugadores_vivos_1} del equipo 1 y {jugadores_vivos_2} del equipo 2."


# Pedimos los jugadores
equipos = IntroducirJugadores()

# Los mostramos
MostrarEquipos(equipos)

# Generemos el tablero mandandole el numero de jugadores
numero_jugadores = len(equipos[0]) * 2
tablero = crearmatriz(numero_jugadores, numero_jugadores)

# Generamos y mostramos las pociciones de los jugadores
posicion_jugadores = JugadoresTablero(tablero)
visualizarmatriz(tablero)

# Llamamos a Jugar
Jugar(equipos, tablero, posicion_jugadores)

# Mostramos el equipo ganador
print(ObtenerGanador(equipos, posicion_jugadores))
