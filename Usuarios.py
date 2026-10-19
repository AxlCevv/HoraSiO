from abc import ABC, abstractmethod


# ABSTRACCIÓN: base común que no se instancia directamente; define lo compartido por todos los roles.
class Usuario(ABC):
    # CONSTRUCTOR: recibe los datos comunes y los conserva en atributos internos.
    def __init__(self, id, nombre, apellido, correo, contrasena, rol):
        self._id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self._contrasena = contrasena
        self.rol = rol

    # ENCAPSULAMIENTO Y PROPIEDADES: los getters/setters controlan el acceso a los atributos.
    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor.strip()

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El apellido no puede estar vacío")
        self._apellido = valor.strip()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not valor or "@" not in valor:
            raise ValueError("Ingresa un correo válido")
        self._correo = valor.strip().lower()

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El rol no puede estar vacío")
        self._rol = valor.strip()

    # MÉTODO: autentica comparando correo y contraseña sin exponer el atributo interno.
    def iniciarSesion(self, correo, contrasena):
        return (
            self.correo.casefold() == correo.strip().casefold()
            and self._contrasena == contrasena
        )

    def cambiarContrasena(self, nueva_contrasena):
        if len(nueva_contrasena) < 4:
            raise ValueError("La contraseña debe tener al menos 4 caracteres")
        self._contrasena = nueva_contrasena

    # SOBRECARGA FLEXIBLE: los argumentos opcionales permiten actualizar uno o varios datos.
    # Python no define varias versiones del mismo método; aquí se admiten distintas llamadas.
    def actualizarDatos(self, nombre=None, apellido=None, correo=None):
        if nombre is not None:
            self.nombre = nombre
        if apellido is not None:
            self.apellido = apellido
        if correo is not None:
            self.correo = correo

    def cerrarSesion(self):
        print("Sesión cerrada")

    # POLIMORFISMO ABSTRACTO: cada clase derivada debe proporcionar su propia implementación.
    @abstractmethod
    def mostrarPanel(self):
        raise NotImplementedError