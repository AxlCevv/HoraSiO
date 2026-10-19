from usuarios import Usuario


# HERENCIA: Administrador reutiliza los atributos y métodos definidos en Usuario.
class Administrador(Usuario):
    # CONSTRUCTOR: super() inicializa la parte común heredada.
    def __init__(self, id, nombre, apellido, correo, contrasena):
        super().__init__(id, nombre, apellido, correo, contrasena, "Administrador")

    # POLIMORFISMO: implementación propia del método abstracto mostrarPanel.
    def mostrarPanel(self):
        print(f"Panel de {self.rol}: gestión de usuarios y roles.")

    def delegarRolCoordinador(self, usuario, sistema):
        nuevo_coordinador = sistema.delegarRolCoordinador(usuario)
        if nuevo_coordinador:
            print("Rol de Coordinador delegado correctamente")
        else:
            print("No se pudo delegar el rol.")

    # SOBRECARGA FLEXIBLE: campo es opcional para elegir el criterio de búsqueda.
    def buscarUsuario(self, usuarios, criterio, campo="correo"):
        if campo not in ("correo", "nombre", "apellido", "id"):
            raise ValueError("Campo de búsqueda no válido")

        for usuario in usuarios:
            valor = getattr(usuario, campo)
            if str(valor).casefold() == str(criterio).casefold():
                return usuario
        return None

