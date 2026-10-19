# HoraSIO - Sistema de Gestión de Horarios Académicos

Avance de proyecto en Python con Programación Orientada a Objetos.

## Archivos

- main.py: menú, conexión de dependencias y punto de entrada.
- usuarios.py: clase abstracta base con propiedades, métodos y datos encapsulados.
- administrador.py: clase Administrador, derivada de Usuario.
- coordinador.py: clase Coordinador, derivada de Usuario.
- docente.py: clase Docente, derivada de Usuario.
- estudiante.py: clase Estudiante, derivada de Usuario.
- interfaces.py: contrato IPersistencia.
- gestion.py: sistema de gestión y autenticación.
- persistencia.py: respaldo manual de datos a JSON.
- entidades.py: paralelo, materia y aula.
- horarios.py: horarios, asignaciones y validación de colisiones.

## Conceptos de POO

- Encapsulamiento y propiedades: Usuario guarda atributos internos con _ y valida los datos mediante propiedades.
- Constructores: cada rol llama a super().__init__() para inicializar la parte común.
- Métodos: inicio de sesión, cambio de contraseña, registro y consulta de horarios.
- Sobrecarga flexible: Coordinador.registrarEstudiante acepta un objeto Estudiante o sus datos; Usuario.actualizarDatos acepta uno o más campos opcionales. Python simula la sobrecarga de esta manera.
- Herencia: Administrador, Coordinador, Docente y Estudiante heredan de Usuario.
- Polimorfismo abstracto: Usuario declara mostrarPanel como abstracto; cada rol lo implementa y main invoca el mismo método.
- Polimorfismo con interfaz: SistemaGestion recibe una implementación que cumple el contrato IPersistencia y la usa mediante guardar_datos.
- Inyección de dependencias: main.py crea GestorPersistencia y lo entrega al constructor de SistemaGestion.

## Persistencia

La opción 2 del menú exporta un respaldo JSON con usuarios (sin contraseñas), materias, aulas, paralelos y asignaciones de horario. Este avance permite guardar/exportar el estado; todavía no carga el archivo JSON al iniciar el programa.

## Usuarios de prueba

- Administrador: admin@horasio.com / 1234
- Coordinador: coord@horasio.com / 1234
- Docente: docente@horasio.com / 1234
- Estudiante: estudiante@horasio.com / 1234

Ejecuta python main.py desde la carpeta del proyecto.

