from typing import Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from gestion import SistemaGestion

# INTERFAZ: cualquier estrategia de persistencia debe ofrecer guardar_datos.
class IPersistencia(Protocol):
    def guardar_datos(self, sistema: "SistemaGestion") -> None:
        ...
