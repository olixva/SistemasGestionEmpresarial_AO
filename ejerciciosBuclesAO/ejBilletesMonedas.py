cantidad_euros = int(input("Introduzca una cantidad en euros: "))

# Creamos lo que sera el resultado final
billetes_monedas = {
    500: 0,
    200: 0,
    100: 0,
    50: 0,
    20: 0,
    10: 0,
    5: 0,
    2: 0,
    1: 0
}

# Calcular la cantidad de cada billete y monedas
for valor, cantidad_billete_moneda in billetes_monedas.items():
    # Accedemos al valor de la clave "valor" y le asignamos la cantidad de billetes o monedas
    # si la cantidad de euros es mayor se asigna 0
    billetes_monedas[valor] = cantidad_euros // valor 
    # Una vez asignado el valor, se calcula el resto de la division y se reasigna a cantidad_euros
    cantidad_euros %= valor

# Imprimimos los resultados
for valor, cantidad in billetes_monedas.items():
    if cantidad > 0:
        if valor >= 5:
            print(cantidad, "billetes de" ,valor, "€")
        else:
            print(cantidad, "monedas de" ,valor, "€")
