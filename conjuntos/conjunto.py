curso1=set(["Juan", "Pedro", "Antonio"])
curso2=set(["Luis", "María", "Lola"])
curso3=set(["Manolo", "Lucía", "Enrique"])

instituto=[curso1, curso2, curso3]

equipo=set(["Juan", "Antonio"])

#Opcion con for (menos eficiente porque recorre todo el conjunto)
pertenece=False
for curso in instituto:
    if equipo.issubset(curso):
        print("Todo el equipo pertenece a una clase")
        pertenece=True
i=0

#Opcion con while (mas eficiente porque para cuando encuentra el elemento)
while i < len(instituto) and not equipo.issubset(instituto[i]):
        i+1

if i < len(instituto):
    print("pertenece")
else:
    print("No pertence")
