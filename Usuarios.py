class Usuario:
    def __init__(self, id, nombre, apellido, correo, contrasena, rol):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol

    def iniciarSesion(self, correo, contrasena):
        return self.correo == correo and self.contrasena == contrasena

    def cerrarSesion(self):
        print("Sesión cerrada")


class Administrador(Usuario):
    def __init__(self, id, nombre, apellido, correo, contrasena):
        super().__init__(id, nombre, apellido, correo, contrasena, "Administrador")

    def delegarRolCoordinador(self, usuario, sistema):
        usuario.rol = "Coordinador"
        print("Rol de Coordinador delegado correctamente")


class Coordinador(Usuario):
    def __init__(self, id, nombre, apellido, correo, contrasena):
        super().__init__(id, nombre, apellido, correo, contrasena, "Coordinador")

    def registrarEstudiante(self, id, nombre, apellido, correo, contrasena, paralelo, sistema):
        estudiante = Estudiante(id, nombre, apellido, correo, contrasena, paralelo)
        sistema.usuarios.append(estudiante)
        print("Estudiante registrado correctamente")
        return estudiante

    def crearAsignacion(self, materia, aula, paralelo, docente, franja, horario):
        from horarios import PreAsignacion
        pre = PreAsignacion(len(horario.preasignaciones) + 1, materia, aula, paralelo, docente, franja)
        return horario.agregarAsignacion(pre)


class Docente(Usuario):
    def __init__(self, id, nombre, apellido, correo, contrasena):
        super().__init__(id, nombre, apellido, correo, contrasena, "Docente")

    def visualizarHorario(self, horarios):
        for horario in horarios:
            for pre in horario.preasignaciones:
                if pre.docente.id == self.id:
                    pre.mostrar()


class Estudiante(Usuario):
    def __init__(self, id, nombre, apellido, correo, contrasena, paralelo):
        super().__init__(id, nombre, apellido, correo, contrasena, "Estudiante")
        self.paralelo = paralelo

    def visualizarHorario(self, horarios):
        for horario in horarios:
            for pre in horario.preasignaciones:
                if pre.paralelo.id == self.paralelo.id:
                    pre.mostrar()
