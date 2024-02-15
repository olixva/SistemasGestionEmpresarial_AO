from simulacroExamenOO.Aula import Aula
from simulacroExamenOO.Alumno import Alumno


def menu():
    opciones()
    aula = None
    opcion = input("Introduce una opcion: ")
    while opcion != '8':

        if opcion == '1':
            nombre = input("Introduce nombre del alumno: ")
            edad = int(input("Introduce edad del alumno: "))
            alumno = Alumno(nombre, edad)
        elif opcion == '2':
            aula = Aula()
            print("Aula creada correctamente")
        elif opcion == '3':
            alumno = Alumno("Juan")
            print(aula.InsertarAlumno(alumno))
        elif opcion == '4':
            if aula is None:
                print("Debes crear un aula primero.")
            else:
                print(aula)
        elif opcion == '5':
            if aula is None:
                print("Debes crear un aula primero.")
            else:
                nombre = input("Introduce nombre del alumno: ")
                existe = aula.ExisteAlumno(nombre)
                if existe:
                    print("El alumno existe en el aula.")
                else:
                    print("El alumno no existe en el aula.")
        elif opcion == '6':
            if aula is None:
                print("Debes crear un aula primero.")
        elif opcion == '7':
            if aula is None:
                print("Debes crear un aula primero.")
            else:
                print(aula.AlumnosMenores())
        elif opcion == '8':
            print("Saliendo del programa...")
        else:
            print("Opción no válida. Introduce un número del 1 al 8.")

        opciones()
        opcion = input("Introduce una opción: ")


def opciones():
    print("Menú")
    print("1. Crear Alumno")
    print("2. Crear Aula")
    print("3. Insertar Alumno en Aula")
    print("4. Mostrar todos los alumnos del Aula")
    print("5. Comprobar si existe Alumno en Aula")
    print("6. Insertar Alumnos en Aula sin repetidos")
    print("7. Mostrar Alumnos Menores y por Rango de Edad")
    print("8. Salir")


menu()
