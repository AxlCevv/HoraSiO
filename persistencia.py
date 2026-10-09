import json
import os

class GestorPersistencia:
    def __init__(self, archivo="datos_horasio.json"):
        self.archivo = archivo

    def guardar_datos(self, sistema):
        datos = {
            "usuarios": [{"id": u.id, "nombre": u.nombre, "rol": u.rol} for u in sistema.usuarios],
            "materias": [{"id": m.id, "nombre": m.nombre} for m in sistema.materias],
            "aulas": [{"id": a.id, "numero": a.numero} for a in sistema.aulas]
        }
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4)
            print("Datos respaldados en formato JSON correctamente.")
        except Exception as e:
            print(f"Error al guardar datos: {e}")