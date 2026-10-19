import json
from interfaces import IPersistencia

# IMPLEMENTACIÓN DE INTERFAZ: esta clase satisface el contrato IPersistencia.
class GestorPersistencia:
    def __init__(self, archivo="datos_horasio.json"):
        self.archivo = archivo

    # MÉTODO DE PERSISTENCIA: exporta un respaldo de datos del sistema a JSON.
    def guardar_datos(self, sistema):
        datos = {
            "usuarios": [
                {
                    "id": usuario.id,
                    "nombre": usuario.nombre,
                    "apellido": usuario.apellido,
                    "correo": usuario.correo,
                    "rol": usuario.rol,
                }
                for usuario in sistema.usuarios
            ],
            "materias": [
                {"id": materia.id, "nombre": materia.nombre, "codigo": materia.codigo}
                for materia in sistema.materias
            ],
            "aulas": [
                {
                    "id": aula.id,
                    "numero": aula.numero,
                    "capacidad": aula.capacidad,
                    "ubicacion": aula.ubicacion,
                }
                for aula in sistema.aulas
            ],
            "paralelos": [
                {"id": paralelo.id, "nombre": paralelo.nombre, "nivel": paralelo.nivel}
                for paralelo in sistema.paralelos
            ],
            "horario": {
                "id": sistema.horario_actual.id,
                "periodo": sistema.horario_actual.periodo,
                "asignaciones": [
                    {
                        "id": asignacion.id,
                        "materia_id": asignacion.materia.id,
                        "aula_id": asignacion.aula.id,
                        "paralelo_id": asignacion.paralelo.id,
                        "docente_id": asignacion.docente.id,
                        "dia": asignacion.franja.dia,
                        "hora_inicio": asignacion.franja.horaInicio,
                        "hora_fin": asignacion.franja.horaFin,
                    }
                    for asignacion in sistema.horario_actual.preasignaciones
                ],
            },
        }

        try:
            with open(self.archivo, "w", encoding="utf-8") as archivo_json:
                json.dump(datos, archivo_json, indent=4, ensure_ascii=False)
            print(f"Datos respaldados en {self.archivo}")
        except OSError as error:
            print(f"Error al guardar datos: {error}")
