###################################################
## Módulo Utilidades para el Exámen              ##
## Este módulo contiene las funciones que se     ##
## necesitan para la realización examen          ##
## Este módulo no puede ser modificado           ##
###################################################


# Función que crea una matriz a partir de los parámetros
# que se le envían, donde f es el número de filas, c es
# el número de columnas

def crearmatriz(f, c):
    m = list()
    for i in range(f):
        filas = ["-"] * c
        m.append(filas)
    return m

# Función que muestra por pantalla la matriz enviada

def visualizarmatriz(m):
    for f in m:
        for e in f:
            print(e, end="\t")
        print() 


# Función que crea calcula la nueva posición del jugador
# a partir de la posición. Se le pasa m que es la matriz,
# p que es la posición actual, o que es la orientación y 
# s que es la cantidad de saltos

def mover(m, p, o, s):
    if o == "C":
        longitud = len(m[0])
        cambio = p[1]
    else:
        longitud = len(m)
        cambio = p[0]
    incremento = +1
    for i in range(s):
        if cambio == (longitud - 1):
            incremento = -1
        elif cambio == 0:
            incremento = +1
        cambio += incremento
    if o == "C":
        return [p[0], cambio]
    else:
        return [cambio, p[1]]
   
if __name__ == '__main__':
    m = crearmatriz(5,4)
    visualizarmatriz(m)
    for i in range(10):
        print(mover(m, [1,1], "F", i))
    for i in range(10):
        print(mover(m, [1,1], "C", i))
