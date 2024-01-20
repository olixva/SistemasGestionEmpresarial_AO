def cadenas_mas_largas(lista):
    mas_largo = 0
    resultado = []

    for cadena in lista:
        if len(cadena) > mas_largo:
            resultado = [cadena]
            mas_largo = len(cadena)
        elif mas_largo == len(cadena):
            resultado.append(cadena)
    return resultado


print(cadenas_mas_largas(["Ana", "Pepe", "Ana", "Juan", "Paz"]))
