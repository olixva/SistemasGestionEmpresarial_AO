class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def __str__(self):
        return f"Nombre: {self.nombre} \n DNI: {self.dni}"

    def __copy__(self):
        copia = Persona(self.dni, self.nombre)
        return copia;


pepe = Persona('Pepe', 4564)
print(pepe)
