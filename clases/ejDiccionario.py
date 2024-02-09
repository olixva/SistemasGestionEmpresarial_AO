class Diccionario():
    def __int__(self, nombre, editorial, nivel):
        self.nombre = nombre
        self.editorial = editorial
        self.nivel = nivel
        self.dic = dict()

    def IntroducirPalabra(self, palabra):
        if palabra in self.dic:
            return "Palabra ya en la lista"
        else:
            self.dic[palabra] = list()
            return "Introducida"

    def IntroducirAcepciones(self, palabra, significado):
        if palabra in self.dic:
            self.dic[palabra].append(significado)
            return "Acepcion agregada"
        else:
            return "No existe la palabra"

    def Consulta(self):
        pass

    def Palabras(self):
        pass


diccionario = Diccionario("Diccionario 1", "Editorial 1", "Nivel 1")
opcion = int(input("Teclee una opcion: "))
while opcion != 0:
    if opcion == 1:
        p = input("Palabra: ")
        print(diccionario.IntroducirPalabra(p))
    elif opcion == 2:
        p = input("Palabra: ")
        a = input("Acepcion: ")
        print(diccionario.IntroducirAcepciones(p, a))
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    opcion = int(input("Teclee una opcion: "))
