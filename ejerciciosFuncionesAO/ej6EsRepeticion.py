def es_repetición(cadena):
    longitud = len(cadena)

    # Verificar si la longitud es par y las dos subcadenas son iguales
    if longitud % 2 == 0 and cadena[:longitud // 2] == cadena[longitud // 2:]:
        return True
    else:
        return False


# Ejemplo de uso
print(es_repetición('abab'))
print(es_repetición('ababab'))
