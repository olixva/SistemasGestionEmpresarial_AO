class Aula:
    def __init__(self, ciclo='DAM', curso=1):
        self.ciclo = ciclo
        self.curso = curso
        self.listadoAlumnos = list()

    def InsertarAlumno(self, alumno):
        mensaje = ''
        if len(self.listadoAlumnos) < 30:
            self.listadoAlumnos.append(alumno)
            mensaje = 'Correcto'
        else:
            mensaje = 'Aula llena'

        return mensaje

    def __str__(self):
        alumnos = ''
        for i, alumno in enumerate(self.listadoAlumnos):
            if i < len(self.listadoAlumnos) - 1:
                alumnos += alumno.nombre + ', '
        else:
            alumnos += alumno.nombre

        return f"Ciclo: {self.ciclo} \nCurso: {self.curso} \nAlumnos: {alumnos}"

    def ExisteAlumno(self, nombre):
        encontrado = False
        indice = 0
        while encontrado is False and indice < len(self.listadoAlumnos):
            if self.listadoAlumnos[indice].nombre == nombre:
                encontrado = True
            indice += 1
        return encontrado

    def AlumnosMenores(self):
        rangos = dict()
        for alumno in self.listadoAlumnos:
            if alumno.edad < 18:
                lista = rangos.get("menores", [])
                lista.append(alumno.nombre)
                rangos["menores"] = lista
            else:
                rango = alumno.edad // 10
                lista = rangos.get(rango, [])
                lista.append(alumno.nombre)
                rangos[rango] = lista

        return rangos
