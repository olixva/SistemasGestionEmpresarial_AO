#Pedimos la figura de la que se quiere calcular la superficie
figura = -1;

while figura != "4":
    figura = input("""
    Cálculo de superficies:
    1.- Cuadrados
    2.- Triángulos
    3.- Círculos
    4.- Salir
    Elija opción (1-4): """)
    
    if figura == "1":
        lado = float(input("Introduzca el lado del cuadrado: "))
        print("La superficie del cuadrado es", lado**2, "cm2")
    elif figura == "2":
        base = float(input("Introduzca la base del triángulo: "))
        altura = float(input("Introduzca la altura del triángulo: "))
        print("La superficie del triángulo es", base*altura/2, "cm2")
    elif figura == "3":
        radio = float(input("Introduzca el radio del círculo: "))
        print("La superficie del círculo es", 3.1416*radio**2, "cm2")
    elif figura == "4":
        break
    else:
        print("Opción incorrecta")

