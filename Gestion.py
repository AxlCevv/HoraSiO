from usuarios import Administrador, Coordinador, Docente, Estudiante
from entidades import Paralelo, Materia, Aula
from horarios import Horario
from persistencia import GestorPersistencia

class SistemaGestion:
    def _init_(self):
        self.usuarios = []
        self.materias = []
        self.aulas = []
        self.paralelos = []
        self.horario_actual = Horario(1, "2026-2027")
        self.persistencia = GestorPersistencia()
        self._cargar_datos_iniciales()

    def _cargar_datos_iniciales(self):
        p1 = Paralelo(1, "A", "Segundo Nivel")
        self.paralelos.append(p1)

        m1 = Materia(1, "Programación POO", "POO-202")
        self.materias.append(m1)

        a1 = Aula(1, "Lab 1", 30, "Bloque A")
        self.aulas.append(a1)

        self.usuarios.extend([
            Administrador(1, "Alex", "Mora", "admin@horasio.com", "1234"),
            Coordinador(2, "Carla", "Vera", "coord@horasio.com", "1234"),
            Docente(3, "Luis", "Paz", "docente@horasio.com", "1234"),
            Estudiante(4, "Sofia", "Loor", "estudiante@horasio.com", "1234", p1)
        ])

    def autenticar(self, correo, contrasena):
        for u in self.usuarios:
            if u.iniciarSesion(correo, contrasena):
                return u
        return None

    def guardar_estado(self):
        self.persistencia.guardar_datos(self)