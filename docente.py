from usuarios import Usuario


# HERENCIA: Docente reutiliza la clase base Usuario.
class Docente(Usuario):
    # CONSTRUCTOR: super() inicializa los atributos comunes del usuario.
    def __init__(self, id, nombre, apellido, correo, contrasena):
        super().__init__(id, nombre, apellido, correo, contrasena, "Docente")

    # POLIMORFISMO: Docente implementa mostrarPanel de forma propia.
    def mostrarPanel(self):
        print(f"Panel de docente: {self.nombre} {self.apellido}")

    def visualizarHorario(self, horarios):
        for horario in horarios:
            for pre in horario.preasignaciones:
                if pre.docente.id == self.id:
                    pre.mostrar()

