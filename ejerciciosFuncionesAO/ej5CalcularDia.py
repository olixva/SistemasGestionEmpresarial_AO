def es_bisiesto(agno):
    return (agno % 4 == 0 and agno % 100 != 0) or (agno % 400 == 0)


def dia_agno(dia, mes, agno):
    dias_por_mes = {
        1: 31,  # Enero
        2: 28,  # Febrero (considerando años no bisiestos)
        3: 31,  # Marzo
        4: 30,  # Abril
        5: 31,  # Mayo
        6: 30,  # Junio
        7: 31,  # Julio
        8: 31,  # Agosto
        9: 30,  # Septiembre
        10: 31,  # Octubre
        11: 30,  # Noviembre
        12: 31  # Diciembre
    }

    # Si el ano es bisiesto sumamos un dia a Febrero
    if es_bisiesto(agno):
        dias_por_mes[2] += 1

    resultado = 0
    for i in range(1, mes + 1):
        resultado += dias_por_mes[i]

    # Restamos los dias restantes para acabar el mes actual
    resultado -= dias_por_mes.get(mes) - dia

    return resultado


print(dia_agno(31, 12, 2024))
