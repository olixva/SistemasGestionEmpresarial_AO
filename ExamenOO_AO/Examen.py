class Vagon:
    def __init__(self, NumeroV, Capacidad=4):
        self.NumeroV = NumeroV
        self.Capacidad = Capacidad
        self.Pasajeros = dict()

    def AsientosLibresVagon(self):
        ocupados = 0
        for asientos in self.Pasajeros.values():  # Recorremos los numeros de asientos ocupados
            ocupados += asientos

        return self.Capacidad - ocupados

    def AsignarAsientosVagon(self, dni, numeroAsientos):
        if self.AsientosLibresVagon() >= numeroAsientos:
            # Recuperamos los asientos que ya tiene, 0 si no tiene aun
            asientosPasajero = self.Pasajeros.get(dni, 0) + numeroAsientos
            self.Pasajeros[dni] = asientosPasajero
            return True
        else:
            return False

    def PasajerosVagon(self):
        cadena = f'Vagon numero: {self.NumeroV} - Capacidad: {self.Capacidad} - Libres: {self.AsientosLibresVagon()}'

        if len(self.Pasajeros) > 0:  # Si tiene pasajeros los agregamos
            cadena += f'\nPasajeros:'
            for pasajero, asientos in self.Pasajeros.items():
                cadena += f'\n\t\t{pasajero}: Asientos {asientos}'

        return cadena


class Tren:

    def __init__(self, Nombre, Nvagones=2):
        self.Nombre = Nombre
        self.NVagones = Nvagones
        self.Vagones = ['Locomotora']

        # Agregamos los vagones a la lista
        for i in range(1, Nvagones + 1):
            self.Vagones.append(Vagon(i))

    def ComprarBilletes(self, dni, nAsientos):
        cadena = ''
        indice = 1  # Comprobamos si tiene billetes ya
        while indice <= self.NVagones and dni not in self.Vagones[indice].Pasajeros:
            indice += 1

        if indice <= self.NVagones:  # Ya tiene billetes comprados

            if self.Vagones[indice].AsignarAsientosVagon(dni, nAsientos):  # Si puede comprar en el mismo vagon
                cadena = f'Tren {self.Nombre}. Vagon: {indice}. Asientos: {nAsientos}'  # Devolvemos el ticket
            else:  # Si no puede
                cadena += 'No hay asientos en el mismo vagon'
        else:  # Si no tiene billetes comprados

            indice = 1
            while indice <= self.NVagones and self.Vagones[indice].AsientosLibresVagon() < nAsientos:
                indice += 1

            if indice <= self.NVagones:  # Si hay libres
                self.Vagones[indice].AsignarAsientosVagon(dni, nAsientos)  # Asignamos los asientos
                cadena = f'Tren {self.Nombre}. Vagon: {indice}. Asientos: {nAsientos}'  # Devolvemos el ticket
            else:  # Si no hay
                cadena += 'No hay asientos en el mismo vagon'
        return cadena

    def __str__(self):
        cadena = f'Tren: {self.Nombre}'
        for i in range(1, len(self.Vagones)):
            cadena += '\n' + self.Vagones[i].PasajerosVagon()
        return cadena


tren = None
opciones = '\n1. Crear Tren\n2. Comprar Billetes\n3. Visualizar Tren\n4. Salir\n'

opcion = input(opciones + 'Introduce una opcion: ')
while opcion != '4':
    if opcion == '1':
        nombre = input("Introduce el nombre del tren: ")
        tren = Tren(nombre)
    elif opcion == '2':
        dni = input("Introduce tu DNI: ")
        cantidadBilletes = int(input("Introduce la cantidad de billetes: "))
        print(tren.ComprarBilletes(dni, cantidadBilletes))
    elif opcion == '3':
        print(tren)

    opcion = input(opciones + 'Introduce una opcion: ')
