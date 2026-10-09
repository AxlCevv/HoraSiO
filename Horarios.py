class FranjaHoraria:
    def __init__(self, dia, horaInicio, horaFin):
        self.dia = dia
        self.horaInicio = horaInicio
        self.horaFin = horaFin


class PreAsignacion:
    def __init__(self, id, materia, aula, paralelo, docente, franja):
        self.id = id
        self.materia = materia
        self.aula = aula
        self.paralelo = paralelo
        self.docente = docente
        self.franja = franja

    def mostrar(self):
        print(f"[{self.franja.dia} {self.franja.horaInicio}-{self.franja.horaFin}] "
              f"Materia: {self.materia.nombre} | Aula: {self.aula.numero} | "
              f"Paralelo: {self.paralelo.nombre} | Docente: {self.docente.nombre}")


class Horario:
    def __init__(self, id, periodo):
        self.id = id
        self.periodo = periodo
        self.preasignaciones = []

    def agregarAsignacion(self, nueva):
        if self.validar(nueva):
            self.preasignaciones.append(nueva)
            print("✔ Asignación registrada exitosamente")
            return True
        print("✖ Error: Existe una colisión de horarios")
        return False

    def validar(self, nueva):
        for actual in self.preasignaciones:
            mismo_dia = actual.franja.dia == nueva.franja.dia
            misma_hora = (nueva.franja.horaInicio < actual.franja.horaFin and
                          nueva.franja.horaFin > actual.franja.horaInicio)

            if mismo_dia and misma_hora:
                mismo_docente = actual.docente.id == nueva.docente.id
                mismo_paralelo = actual.paralelo.id == nueva.paralelo.id
                misma_aula = actual.aula.id == nueva.aula.id

                if mismo_docente or mismo_paralelo or misma_aula:
                    return False
        return True

    def visualizar(self):
        for pre in self.preasignaciones:
            pre.mostrar()
