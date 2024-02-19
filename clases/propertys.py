class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def del_nombre(self):
        del self._nombre

    nombre = property(get_nombre, set_nombre, del_nombre)

    def get_edad(self):
        return self._edad

    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad no puede ser negativa")

    def del_edad(self):
        del self._edad

    edad = property(get_edad, set_edad, del_edad)


# Crear una instancia de Persona
persona = Persona("Juan", 30)

# Obtener el nombre y la edad
print("Nombre:", persona.nombre)
print("Edad:", persona.edad)

# Cambiar el nombre y la edad
persona.nombre = "María"
persona.edad = 25

print("Nuevo nombre:", persona.nombre)
print("Nueva edad:", persona.edad)

# Eliminar el nombre y la edad
del persona.nombre
del persona.edad
