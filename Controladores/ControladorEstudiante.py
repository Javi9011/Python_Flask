from Repositorios.RepositorioEstudiante import RepositorioEstudiante
from Modelos.Estudiante import Estudiante
class ControladorEstudiante():
    def __init__(self):
        print("Entra al constructor de la clase controlador")
        self.repositorioEstudiante=RepositorioEstudiante()
    def createEstudiante(self, bodyRequest):
        print("Creando el estudiante")
        nuevoEstudiante = Estudiante(bodyRequest)
        print("Estudiante a crear en la BD: ", nuevoEstudiante.__dict__)
        self.repositorioEstudiante.save(nuevoEstudiante)
        return True

    def listar(self):
        print("Listar todos los estudiantes")
        unEstudiante={
            "_id":"abc123",
            "cedula":"1076622148",
            "nombre":"Nelson",
            "apellido":"Amaya"
        }

    def show(self,id):
        print("Mostrando un estudiante con id ", id)
        elEstudiante={
            "id":id,
            "cedula":"1076622148",
            "nombre":"Nelson",
            "apellido":"Amaya"
        }
        return elEstudiante

    def update(self, id, elEstudiante,infoEstudiante):
        print("Actualizando estudiante con id ", id)
        elEstudiante = Estudiante(infoEstudiante)
        return elEstudiante.__dict__

    def delete(self, id):
        print("Elimiando estudiante con id ", id)
        return {"delete_count":1}