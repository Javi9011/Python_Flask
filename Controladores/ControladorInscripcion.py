from Modelos.Estudiante import Estudiante
from Modelos.Inscripcion import Inscripcion
from Modelos.Materia import Materia
from Repositorios.RepositorioEstudiante import RepositorioEstudiante
from Repositorios.RepositorioInscripcion import RepositorioInscripcion
from Repositorios.RepositorioMateria import RepositorioMateria


class ControladorInscripcion():
    def __init__(self):
        print("Entra al constructor de la clase controlador Inscripcion")
        self.repositorioInscripcion = RepositorioInscripcion()
        self.repositorioEstudiante = RepositorioEstudiante()
        self.repositorioMateria = RepositorioMateria()

    def crearInscripcion(self, bodyRequest, idEstudiante, idMateria):
        print("Creando inscripcion...")
        inscripcionNueva = Inscripcion(bodyRequest)
        estudianteActual = Estudiante(self.repositorioEstudiante.findById(idEstudiante))
        materiaActual = Materia(self.repositorioMateria.findById(idMateria))

        inscripcionNueva.estudiante = estudianteActual
        inscripcionNueva.materia = materiaActual
        print("Inscripcion a crear en BD: ", inscripcionNueva.__dict__)

        return self.repositorioInscripcion.save(inscripcionNueva)
