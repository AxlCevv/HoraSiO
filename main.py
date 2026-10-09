from gestion import SistemaGestion
from horarios import FranjaHoraria

sistema = SistemaGestion()


def solicitar_credenciales():
    print("\n--- Iniciar Sesión ---")
    correo = input("Correo electrónico: ")
    contrasena = input("Contraseña: ")
    usuario = sistema.autenticar(correo, contrasena)
    if usuario:
        print(f"\nBienvenido/a {usuario.nombre} {usuario.apellido} [{usuario.rol}]")
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
            for u in sistema.usuarios:
                print(f"ID: {u.id} | Nombre: {u.nombre} {u.apellido} | Rol actual: {u.rol}")
            
            try:
                uid = int(input("Ingrese el ID del usuario a convertir en Coordinador: "))
                usuario_target = next((u for u in sistema.usuarios if u.id == uid), None)
                if usuario_target:
                    admin.delegarRolCoordinador(usuario_target, sistema)
                else:
                    print("Usuario no encontrado.")
            except ValueError:
                print("ID no válido.")

        elif opcion == "2":
            print("\n--- Usuarios Registrados ---")
            for u in sistema.usuarios:
                print(f"[{u.rol}] ID: {u.id} - {u.nombre} {u.apellido} ({u.correo})")

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
            for idx, m in enumerate(sistema.materias, 1):
                print(f"{idx}. {m.nombre} ({m.codigo})")
            m_idx = int(input("Seleccione Materia #: ")) - 1

            print("Aulas disponibles:")
            for idx, a in enumerate(sistema.aulas, 1):
                print(f"{idx}. {a.numero} - Capacidad: {a.capacidad}")
            a_idx = int(input("Seleccione Aula #: ")) - 1

            print("Paralelos disponibles:")
            for idx, p in enumerate(sistema.paralelos, 1):
                print(f"{idx}. Paralelo {p.nombre} ({p.nivel})")
            p_idx = int(input("Seleccione Paralelo #: ")) - 1

            docentes = [u for u in sistema.usuarios if u.rol == "Docente"]
            print("Docentes disponibles:")
            for idx, d in enumerate(docentes, 1):
                print(f"{idx}. {d.nombre} {d.apellido}")
            d_idx = int(input("Seleccione Docente #: ")) - 1

            dia = input("Día (Ej. Lunes): ")
            inicio = input("Hora Inicio (HH:MM, Ej. 08:00): ")
            fin = input("Hora Fin (HH:MM, Ej. 10:00): ")

            franja = FranjaHoraria(dia, inicio, fin)
            coordinador.crearAsignacion(
                sistema.materias[m_idx],
                sistema.aulas[a_idx],
                sistema.paralelos[p_idx],
                docentes[d_idx],
                franja,
                sistema.horario_actual
            )

        elif opcion == "2":
            print("\n--- Registrar Estudiante ---")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            contrasena = input("Contraseña: ")

            print("Seleccione el paralelo para el estudiante:")
            for idx, p in enumerate(sistema.paralelos, 1):
                print(f"{idx}. Paralelo {p.nombre}")
            p_idx = int(input("Opción: ")) - 1

            coordinador.registrarEstudiante(
                len(sistema.usuarios) + 1,
                nombre,
                apellido,
                correo,
                contrasena,
                sistema.paralelos[p_idx],
                sistema
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