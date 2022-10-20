from Repositorios.RepositorioEstudiante import RepositorioEstudiante
from Modelos.Estudiante import Estudiante
class ControladorEstudiante():
    def __init__(self):
        print("Entra al constructor de la clase controlador")
        self.repositorioEstudiante=RepositorioEstudiante()
    def createEstudiante(self, bodyRequest):
        print("Creando el estudiante...")
        nuevoEstudiante = Estudiante(bodyRequest)
        print("Estudiante a crear en la BD: ", nuevoEstudiante.__dict__)
        self.repositorioEstudiante.save(nuevoEstudiante)
        return True

    def buscarEstudiante(self, idObject):
        print("Buscando el estudiante....", idObject)
        estudiante = Estudiante(self.repositorioEstudiante.findById(idObject))
        return estudiante.__dict__

    def buscarTodosLosEstudiantes(self):
        print("Buscando todos los estudiantes en base de datos....")
        return self.repositorioEstudiante.findAll()

    def actualizarEstudiante(self, estudiante):
        estudianteActual = Estudiante(self.repositorioEstudiante.findById(estudiante["idObject"]))
        print("Actualizando el estudiante....", estudianteActual)
        estudianteActual.nombre = estudiante["nombre"]
        estudianteActual.apellido = estudiante["apellido"]
        estudianteActual.cedula = estudiante["cedula"]
        self.repositorioEstudiante.save(estudianteActual)
        return True

    def eliminarEstudiante(self, idObject):
        print("Eliminando el estudiante....", idObject)
        self.repositorioEstudiante.delete(idObject)
        return True

