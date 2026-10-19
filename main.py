from gestion import SistemaGestion
from horarios import FranjaHoraria
from persistencia import GestorPersistencia


# INYECCIÓN DE DEPENDENCIAS: main conecta una implementación concreta de persistencia al sistema.
sistema = SistemaGestion(GestorPersistencia())


def solicitar_credenciales():
    print("\n--- Iniciar Sesión ---")
    correo = input("Correo electrónico: ")
    contrasena = input("Contraseña: ")
    usuario = sistema.autenticar(correo, contrasena)
    if usuario:
        print(f"\nBienvenido/a {usuario.nombre} {usuario.apellido} [{usuario.rol}]")
        # POLIMORFISMO ABSTRACTO: se invoca el mismo método y actúa la clase concreta del usuario.
        usuario.mostrarPanel()
    else:
        print("\nCredenciales inválidas.")
    return usuario


def menu_administrador(admin):
    while True:
        print("\n--- MENÚ ADMINISTRADOR ---")
        print("1. Delegar rol de Coordinador a un usuario")
        print("2. Ver listado de usuarios registrados")
        print("3. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nUsuarios del sistema:")
            for usuario in sistema.usuarios:
                print(
                    f"ID: {usuario.id} | Nombre: {usuario.nombre} "
                    f"{usuario.apellido} | Rol actual: {usuario.rol}"
                )

            try:
                uid = int(input("Ingrese el ID del usuario a convertir en Coordinador: "))
                usuario_objetivo = next(
                    (usuario for usuario in sistema.usuarios if usuario.id == uid),
                    None,
                )
                if usuario_objetivo:
                    admin.delegarRolCoordinador(usuario_objetivo, sistema)
                else:
                    print("Usuario no encontrado.")
            except ValueError:
                print("ID no válido.")

        elif opcion == "2":
            print("\n--- Usuarios Registrados ---")
            for usuario in sistema.usuarios:
                print(
                    f"[{usuario.rol}] ID: {usuario.id} - "
                    f"{usuario.nombre} {usuario.apellido} ({usuario.correo})"
                )

        elif opcion == "3":
            admin.cerrarSesion()
            break


def menu_coordinador(coordinador):
    while True:
        print("\n--- MENÚ COORDINADOR ---")
        print("1. Asignar clase (Crear Horario con validación de colisiones)")
        print("2. Registrar nuevo estudiante")
        print("3. Visualizar Horario General")
        print("4. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Asignar Clase ---")
            print("Materias disponibles:")
            for idx, materia in enumerate(sistema.materias, 1):
                print(f"{idx}. {materia.nombre} ({materia.codigo})")
            materia_idx = int(input("Seleccione Materia #: ")) - 1

            print("Aulas disponibles:")
            for idx, aula in enumerate(sistema.aulas, 1):
                print(f"{idx}. {aula.numero} - Capacidad: {aula.capacidad}")
            aula_idx = int(input("Seleccione Aula #: ")) - 1

            print("Paralelos disponibles:")
            for idx, paralelo in enumerate(sistema.paralelos, 1):
                print(f"{idx}. Paralelo {paralelo.nombre} ({paralelo.nivel})")
            paralelo_idx = int(input("Seleccione Paralelo #: ")) - 1

            docentes = [usuario for usuario in sistema.usuarios if usuario.rol == "Docente"]
            print("Docentes disponibles:")
            for idx, docente in enumerate(docentes, 1):
                print(f"{idx}. {docente.nombre} {docente.apellido}")
            docente_idx = int(input("Seleccione Docente #: ")) - 1

            dia = input("Día (Ej. Lunes): ")
            inicio = input("Hora Inicio (HH:MM, Ej. 08:00): ")
            fin = input("Hora Fin (HH:MM, Ej. 10:00): ")

            franja = FranjaHoraria(dia, inicio, fin)
            coordinador.crearAsignacion(
                sistema.materias[materia_idx],
                sistema.aulas[aula_idx],
                sistema.paralelos[paralelo_idx],
                docentes[docente_idx],
                franja,
                sistema.horario_actual,
            )

        elif opcion == "2":
            print("\n--- Registrar Estudiante ---")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            contrasena = input("Contraseña: ")

            print("Seleccione el paralelo para el estudiante:")
            for idx, paralelo in enumerate(sistema.paralelos, 1):
                print(f"{idx}. Paralelo {paralelo.nombre}")
            paralelo_idx = int(input("Opción: ")) - 1

            coordinador.registrarEstudiante(
                len(sistema.usuarios) + 1,
                nombre,
                apellido,
                correo,
                contrasena,
                sistema.paralelos[paralelo_idx],
                sistema,
            )

        elif opcion == "3":
            sistema.horario_actual.visualizar()

        elif opcion == "4":
            coordinador.cerrarSesion()
            break


def menu_docente(docente):
    while True:
        print("\n--- MENÚ DOCENTE ---")
        print("1. Visualizar mi horario de clases")
        print("2. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            docente.visualizarHorario([sistema.horario_actual])
        elif opcion == "2":
            docente.cerrarSesion()
            break


def menu_estudiante(estudiante):
    while True:
        print("\n--- MENÚ ESTUDIANTE ---")
        print("1. Visualizar mi horario de clases")
        print("2. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            estudiante.visualizarHorario([sistema.horario_actual])
        elif opcion == "2":
            estudiante.cerrarSesion()
            break


def ejecutar():
    while True:
        print("\n================ HoraSIO ================")
        print("1. Iniciar Sesión")
        print("2. Respaldar Datos (Exportar JSON)")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario = solicitar_credenciales()
            if usuario:
                if usuario.rol == "Administrador":
                    menu_administrador(usuario)
                elif usuario.rol == "Coordinador":
                    menu_coordinador(usuario)
                elif usuario.rol == "Docente":
                    menu_docente(usuario)
                elif usuario.rol == "Estudiante":
                    menu_estudiante(usuario)
        elif opcion == "2":
            sistema.guardar_estado()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break


if __name__ == "__main__":
    ejecutar()

