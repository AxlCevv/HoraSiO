from administrador import Administrador
from coordinador import Coordinador
from docente import Docente
from estudiante import Estudiante
from entidades import Paralelo, Materia, Aula
from horarios import Horario
from interfaces import IPersistencia
from persistencia import GestorPersistencia


class SistemaGestion:
    def _init_(self, persistencia: IPersistencia | None = None):
        self.usuarios = []
        self.materias = []
        self.aulas = []
        self.paralelos = []
        self.horario_actual = Horario(1, "2026-2027")

        # INYECCIÓN DE DEPENDENCIAS: usa el gestor recibido; si no se pasa uno, crea el predeterminado.
        self.persistencia = persistencia if persistencia is not None else GestorPersistencia()
        self._cargar_datos_iniciales()

    def _cargar_datos_iniciales(self):
        paralelo = Paralelo(1, "A", "Segundo Nivel")
        self.paralelos.append(paralelo)

        materia = Materia(1, "Programación POO", "POO-202")
        self.materias.append(materia)

        aula = Aula(1, "Lab 1", 30, "Bloque A")
        self.aulas.append(aula)

        # Cada constructor crea su subtipo, todos derivados de Usuario.
        self.usuarios.extend(
            [
                Administrador(1, "Alex", "Mora", "admin@horasio.com", "1234"),
                Coordinador(2, "Carla", "Vera", "coord@horasio.com", "1234"),
                Docente(3, "Luis", "Paz", "docente@horasio.com", "1234"),
                Estudiante(4, "Sofia", "Loor", "estudiante@horasio.com", "1234", paralelo),
            ]
        )

    def autenticar(self, correo, contrasena):
        for usuario in self.usuarios:
            if usuario.iniciarSesion(correo, contrasena):
                return usuario
        return None

    def delegarRolCoordinador(self, usuario):
        """Reemplaza el objeto por un Coordinador para que rol y tipo coincidan."""
        for indice, registrado in enumerate(self.usuarios):
            if registrado.id == usuario.id:
                if isinstance(registrado, Coordinador):
                    return registrado

                # Se conserva la credencial al crear una instancia del subtipo Coordinador.
                nuevo = Coordinador(
                    registrado.id,
                    registrado.nombre,
                    registrado.apellido,
                    registrado.correo,
                    registrado._contrasena,
                )
                self.usuarios[indice] = nuevo
                return nuevo
        return None

    def guardar_estado(self):
        # POLIMORFISMO DE INTERFAZ: cualquier IPersistencia puede guardar el estado.
        self.persistencia.guardar_datos(self)