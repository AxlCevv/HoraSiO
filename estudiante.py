from usuarios import Usuario

# HERENCIA: Estudiante es un Usuario y agrega el dato específico de su paralelo.
class Estudiante(Usuario):
    # CONSTRUCTOR: inicializa los datos comunes con super() y añade paralelo.
    def __init__(self, id, nombre, apellido, correo, contrasena, paralelo):
        super().__init__(id, nombre, apellido, correo, contrasena, "Estudiante")
        self._paralelo = paralelo

    @property
    def paralelo(self):
        return self._paralelo

    # POLIMORFISMO: Estudiante implementa el mismo método abstracto con su panel.
    def mostrarPanel(self):
        print(f"Panel de estudiante: {self.nombre} {self.apellido}")

    def visualizarHorario(self, horarios):
        for horario in horarios:
            for pre in horario.preasignaciones:
                if pre.paralelo.id == self.paralelo.id:
                    pre.mostrar()

