class SalaCine:
    def __init__(self, CNumero_Sala, CAforo_Maximo, CPelicula=""):
        self.CNumero_Sala = CNumero_Sala
        self.CAforo_Maximo = CAforo_Maximo
        self.CPelicula = CPelicula
        self.CAforo_Actual = 0

    def __getCAforo_Actual(self):
        return self.CAforo_Actual

    def __setCAforo_Actual(self, CAforo_Actual):
        if CAforo_Actual >= 0 and CAforo_Actual <= self.CAforo_Maximo:
            self.CAforo_Actual = CAforo_Actual
            return ("Aforo actualizado correctamente")
        else:
            return ("El aforo tiene que ser entre 0 y " + str(self.CAforo_Maximo))

    Aforo = property(__getCAforo_Actual, __setCAforo_Actual)

    def MostrarSala(self):
        return ("Sala: " + str(self.CNumero_Sala) + " - Pelicula: " + str(self.CPelicula) + " - Aforo Maximo: " + str(
            self.CAforo_Maximo) + " - Aforo Actual: " + str(self.Aforo))


class Cine:
    def __init__(self, CNombre_Cine, CNumero_Salas):
        self.CNombre_Cine = CNombre_Cine
        self.CNumero_Salas = CNumero_Salas
        self.CSalas_Cine = {}
        for i in range(1, CNumero_Salas + 1):
            self.CSalas_Cine[i] = SalaCine(i, 10)

    def __str__(self):
        cadena = "Cine: " + self.CNombre_Cine
        cadena += "\nNumero de salas: " + str(self.CNumero_Salas)
        for i in range(1, self.CNumero_Salas + 1):
            cadena += "\n\t" + self.CSalas_Cine[i].MostrarSala()
        return cadena

    def Poner_Pelicula(self, numero_sala, pelicula):
        if numero_sala in self.CSalas_Cine:
            self.CSalas_Cine.get(numero_sala).CPelicula = pelicula
            return ("Pelicula puesta correctamente")
        else:
            return ("Numero de sala no valido")

    def Fin_Pelicula(self, numero_sala):
        if numero_sala in self.CSalas_Cine:
            self.CSalas_Cine.get(numero_sala).Aforo = self.CSalas_Cine.get(numero_sala).CAforo_Maximo
            return ("Fin de pelicula correcto")
        else:
            return ("Numero de sala no valido")

    def Comprar_Entrada(self, pelicula, cantidad, sala):
        if self.CSalas_Cine[sala].CPelicula == pelicula and self.CSalas_Cine[sala].Aforo >= cantidad:
            self.CSalas_Cine[sala].Aforo -= cantidad
            return ("Venta de Entradas Correcto")
        else:
            i = 1
            while i <= len(self.CSalas_Cine):
                if (self.CSalas_Cine[i].CPelicula == pelicula and self.CSalas_Cine[i].Aforo >= cantidad):
                    return ("En la Sala " + str(i) + " hay suficientes entradas disponibles")
                i += 1
            return ("No hay entradas suficientes en ninguna sala")

    def Cartelera_Cine(self):
        nombreCine = "Cartelera cine " + self.CNombre_Cine
        guiones = ""
        for i in range(len(nombreCine)):
            guiones += "-"
        Peliculas = {}
        for i in range(1, len(self.CSalas_Cine)):
            if (self.CSalas_Cine[i].CPelicula not in Peliculas):
                Peliculas[self.CSalas_Cine[i].CPelicula] = []
            Peliculas[self.CSalas_Cine[i].CPelicula].append(self.CSalas_Cine[i].CNumero_Sala)
        peliculas = ""
        for i in Peliculas:
            peliculas += i + ": "
            for j in range(len(Peliculas[i]) + 1):
                peliculas += str(j) + " "
            peliculas += "\n"
        return nombreCine + "\n" + guiones + "\n\n" + peliculas


if (__name__ == "__main__"):
    i = 0
    nombre = str(input("Nombre del cine: "))
    num_salas = int(input("Numero de salas: "))
    cine1 = Cine(nombre, num_salas)
    while i != 6:
        i = int(input(
            "\n1.-Pelicula\n2.-Fin Pelicula\n3.-Mostrar Cartelera\n4.-Comprar Entrada\n5.-Mostrar Todo\n6.-Salir\n"))
        if i == 1:
            pelicula = str(input("Introduce la pelicula: "))
            sala = int(input("Numero de sala: "))
            print(cine1.Poner_Pelicula(sala, pelicula))
        if i == 2:
            sala = int(input("Numero de sala: "))
            print(cine1.Fin_Pelicula(sala))
        if i == 3:
            print(cine1.Cartelera_Cine())
        if i == 4:
            pelicula = str(input("Introduce la pelicula: "))
            sala = int(input("Numero de sala: "))
            entradas = int(input("Numero de entradas: "))
            print(cine1.Comprar_Entrada(pelicula, entradas, sala))
        if i == 5:
            print(cine1)
        if i == 6:
            print("Sesion finalizada.")
