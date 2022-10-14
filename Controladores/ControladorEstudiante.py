from Modelos.Estudiante import Estudiante
class ControladorEstudiante():
    def __init__(self):
        print("Entra al constructor de la clase controlador")

    def createEstudiante(self):
        print("logica del estudiante")
        return True

    def index(self):
        print("Listar todos los estudiantes")

    def create(self,elEstudiante):
        print("Crear un estudiante")

    def show(self,id):
        print("Mostrando un estudiante con id ", id)

    def update(self, id, elEstudiante):
        print("Actualizando estudiante con id ", id)

    def delete(self, id):
        print("Elimiando estudiante con id ", id)