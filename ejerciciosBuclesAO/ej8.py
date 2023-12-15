diasMes = int(input("Numero de dias del mes: "))
diaSemana = int(input("Día 1 es (0 lunes, 6 domingo): "))

# Impresion de cabecera
print("L\tM\tX\tJ\tV\tS\tD")

# Imprimimos espacios en blanco hasta el dia de la semana indicado
for i in range(diaSemana):
    print("\t", end="")

# Imprimimos los dias del mes, si el dia es domingo, hacemos un salto de linea
for i in range(1, diasMes+1):
    print(i, end="\t")
    if (i+diaSemana) % 7 == 0: # Si i+diaSemana es multiplo de 7, es domingo
        print()

