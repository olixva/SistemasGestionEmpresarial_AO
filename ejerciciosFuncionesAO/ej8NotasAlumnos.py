alumnosExamen = ['Ana Pi', 'Pau Lopez', 'Luis Sol', 'Mar Vega', 'Paz Mir']
notasExamen = [10, 5.5, 2.0, 8.5, 7.0]


def agregar_estudiante(nombre, nota):
    alumnosExamen.append(nombre)
    notasExamen.append(nota)


def muestra_nota_de_alumno(alumnos, notas, alumno_buscado):
    for i in range(len(alumnos)):
        if alumnos[i] == alumno_buscado:
            print(alumno_buscado, notas[i])
            return
    print(f"El alumno {alumno_buscado} no pertenece al grupo")


def obtener_alumnos_aprobados(alumnos, notas):
    aprobados = []
    for i in range(len(alumnos)):
        if notas[i] > 5:
            aprobados.append(alumnos[i])
    return aprobados


def obtener_numero_aprobados(notas):
    aprobados = 0
    for i in range(len(notas)):
        if notas[i] > 5:
            aprobados += 1
    return aprobados


def obtener_alumnos_mejor_nota(alumnos, notas):
    nota_maxima = max(notas)
    alumnos_mejor_nota = []
    for i in range(len(alumnos)):
        if notas[i] == nota_maxima:
            alumnos_mejor_nota.append(alumnos[i])
    return alumnos_mejor_nota


def obtener_alumnos_sobre_media(alumnos, notas):
    nota_media = (sum(notas) / len(notas))
    alumnos_sobre_media = []
    for i in range(len(alumnos)):
        if notas[i] >= nota_media:
            alumnos_sobre_media.append(alumnos[i])
    return alumnos_sobre_media


def obtener_nota_de_alumno(alumnos, notas, alumno_buscado):
    for i in range(len(alumnos)):
        if alumnos[i] == alumno_buscado:
            return notas[i]
    return


def menu_principal():
    estudiantes = []

    opcion = -1
    while opcion != 8:
        print("\nMenú:")
        print("1) Añadir estudiante y calificación")
        print("2) Mostrar lista de estudiantes con sus calificaciones")
        print("3) Mostrar estudiantes aprobados")
        print("4) Número de aprobados")
        print("5) Estudiantes con máxima nota")
        print("6) Estudiantes con nota mayor o igual a la media")
        print("7) Nota estudiante")
        print("8) Finalizar ejecución del programa")

        opcion = input("Seleccione una opción (1-8): ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            nota = float(input("Ingrese la nota del estudiante: "))
            agregar_estudiante(nombre, nota)

        elif opcion == "2":
            for alumno in alumnosExamen:
                muestra_nota_de_alumno(alumnosExamen, notasExamen, alumno)

        elif opcion == "3":
            print(obtener_alumnos_aprobados(alumnosExamen, notasExamen))

        elif opcion == "4":
            print("Número de aprobados:", obtener_numero_aprobados(notasExamen))

        elif opcion == "5":
            print("Estudiantes con máxima nota:")
            print(obtener_alumnos_mejor_nota(alumnosExamen, notasExamen))

        elif opcion == "6":
            print("Estudiantes con nota mayor o igual a la media:")
            print(obtener_alumnos_sobre_media(alumnosExamen, notasExamen))

        elif opcion == "7":
            nombre_estudiante = input("Ingrese el nombre del estudiante: ")
            muestra_nota_de_alumno(alumnosExamen, notasExamen, nombre_estudiante)

        elif opcion == "8":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 8.")


menu_principal()
