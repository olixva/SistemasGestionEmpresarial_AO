class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass


class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hacer_sonido(self):
        return "Guau!"


class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def hacer_sonido(self):
        return "¡Miau!"


perro = Perro("Bobby", "Labrador")
gato = Gato("Tom", "Negro")

print("Perro:", perro.nombre, "de raza", perro.raza, "-", perro.hacer_sonido())
print("Gato:", gato.nombre, "de color", gato.color, "-", gato.hacer_sonido())
