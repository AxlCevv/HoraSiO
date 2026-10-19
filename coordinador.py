from horarios import PreAsignacion
from estudiante import Estudiante
from usuarios import Usuario

# HERENCIA: Coordinador comparte el estado y comportamiento común de Usuario.
class Coordinador(Usuario):
    # CONSTRUCTOR: super() establece los datos comunes con el rol Coordinador.
    def __init__(self, id, nombre, apellido, correo, contrasena):
        super().__init__(id, nombre, apellido, correo, contrasena, "Coordinador")

    # POLIMORFISMO: implementación concreta del método abstracto de Usuario.
    def mostrarPanel(self):
        print(f"Panel de coordinador: {self.nombre} {self.apellido}")

    # SOBRECARGA FLEXIBLE: recibe un objeto Estudiante existente o sus datos separados.
    def registrarEstudiante(self, *datos):
        if len(datos) == 2 and isinstance(datos[0], Estudiante):
            estudiante, sistema = datos
        elif len(datos) == 7:
            id, nombre, apellido, correo, contrasena, paralelo, sistema = datos
            estudiante = Estudiante(
                id, nombre, apellido, correo, contrasena, paralelo
            )
        else:
            raise TypeError(
                "Usa (estudiante, sistema) o "
                "(id, nombre, apellido, correo, contraseña, paralelo, sistema)"
            )

        sistema.usuarios.append(estudiante)
        print("Estudiante registrado correctamente")
        return estudiante

    def crearAsignacion(self, materia, aula, paralelo, docente, franja, horario):
        preasignacion = PreAsignacion(
            len(horario.preasignaciones) + 1,
            materia,
            aula,
            paralelo,
            docente,
            franja,
        )
        return horario.agregarAsignacion(preasignacion)

