import random


class Examen:
    def __init__(self, tema):
        self.tema = tema
        self.Preguntas = dict()

    def InsertarPregunta(self, pregunta, respuesta, puntuacion, tema='Python'):

        # Comprobaciones de puntuacion
        if puntuacion < 0:
            puntuacion = 0
        elif puntuacion > 10:
            puntuacion = 10

        preguntas_tema = self.Preguntas.get(tema, [])
        preguntas_tema.append((pregunta, respuesta, puntuacion))
        self.Preguntas[tema] = preguntas_tema

    def __str__(self):
        cadena = ''
        # Por cada tema
        for tema, preguntas in self.Preguntas.items():
            cadena += f'\nTema: {tema}'

            # Por cada pregunta
            for pregunta in preguntas:
                cadena += f'\n\tPregunta: {pregunta[0]}\n\tRespuesta: {pregunta[1]}\n\tPuntuacion: {pregunta[2]}\n'
        return cadena

    def GenerarExamen(self, tema, numero_preguntas):
        # Si el tema tiene suficientes preguntas
        if len(self.Preguntas.get(tema, [])) >= numero_preguntas:

            preguntas_respondidas = []
            puntuacion = 0
            puntacion_maxima = 0
            while len(preguntas_respondidas) < numero_preguntas:
                numero_aleatorio = random.randint(0, len(self.Preguntas[tema]) - 1)
                pregunta = self.Preguntas[tema][numero_aleatorio]

                if pregunta not in preguntas_respondidas:  # Si no es repetida
                    if input(f'{pregunta[0]}: ') == str(pregunta[1]):
                        puntuacion += pregunta[2]  # Si se responde bien
                    puntacion_maxima += pregunta[2]
                    preguntas_respondidas.append(pregunta)
            print(
                f'Total preguntas: {numero_preguntas}\nPuntuacion maxima posible: {puntacion_maxima}\nPuntuacion obtenida: {puntuacion}')

        else:
            print('El tema no existe o no tiene suficientes preguntas')


opciones = "\n1.-Crear Examen\n2.-Introducir Pregunta\n3.-Imprimir preguntas\n4.-Generar Examen\n5.-Salir\n"
examen = None
o = int(input(opciones))
while o != 6:
    if o == 1:
        nombre_modulo = input('Introduce el nombre del modulo: ')
        examen = Examen(nombre_modulo)
    elif o == 2:
        if examen is not None:
            tema = input('Introduce el Tema de la pregunta (ENTER para por defecto): ')
            pregunta = input('Introduce la pregunta: ')
            respuesta = input('Introduce la respuesta: ')
            puntuacion = int(input('Introduce la puntuacion de la pregunta: '))

            if tema != '':
                examen.InsertarPregunta(pregunta, respuesta, puntuacion, tema)
            else:  # Si el tema esta vacio usamos el otro constructor
                examen.InsertarPregunta(pregunta, respuesta, puntuacion)
        else:
            print('Debe crear un examen primero')
    elif o == 3:
        if examen is not None:
            print(examen)
        else:
            print('Debe crear un examen primero')
    elif o == 4:
        tema = str(input('Introduce el Tema del examen: '))
        numero_preguntas = int(input('Introduce el numero de preguntas: '))
        examen.GenerarExamen(tema, numero_preguntas)

    o = int(input(opciones))

print("Sesion finalizada.")
