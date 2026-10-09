from usuarios import Administrador, Coordinador, Docente, Estudiante
from entidades import Paralelo, Materia, Aula
from horarios import Horario
from persistencia import GestorPersistencia


class SistemaGestion:
    def __init__(self):
        self.usuarios = []
        self.materias = []
        self.aulas = []
        self.paralelos = []
        self.horario_actual = Horario(1, "2026-2027")
        self.persistencia = GestorPersistencia()
        self._cargar_datos_iniciales()

    def _cargar_datos_iniciales(self):
        p1 = Paralelo(1, "A", "Segundo Nivel")
        p2 = Paralelo(2, "B", "Segundo Nivel")
        self.paralelos.extend([p1, p2])

        m1 = Materia(1, "Programación POO", "POO-202")
        m2 = Materia(2, "Bases de Datos", "BD-203")
        self.materias.extend([m1, m2])

        a1 = Aula(1, "Lab 1", 30, "Bloque A")
        a2 = Aula(2, "Aula 102", 40, "Bloque B")
        self.aulas.extend([a1, a2])

        admin = Administrador(1, "Alex", "Mora", "admin@horasio.com", "1234")
        coord = Coordinador(2, "Carla", "Vera", "coord@horasio.com", "1234")
        docente = Docente(3, "Luis", "Paz", "docente@horasio.com", "1234")
        estudiante = Estudiante(4, "Sofia", "Loor", "estudiante@horasio.com", "1234", p1)

        self.usuarios.extend([admin, coord, docente, estudiante])

    def autenticar(self, correo, contrasena):
        for u in self.usuarios:
            if u.iniciarSesion(correo, contrasena):
                return u
        return None

    def guardar_estado(self):
        self.persistencia.guardar_datos(self)