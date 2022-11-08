from Modelos.Materia import Materia
from Modelos.Departamento import Departamento
from Repositorios.RepositorioDepartamento import RepositorioDepartamento
from Repositorios.RepositorioMateria import RepositorioMateria


class ControladorMateria():
    def __init__(self):
        print("Entra al constructor de la clase controlador Materia")
        self.repositorioMateria = RepositorioMateria()
        self.repositorioDepartamento = RepositorioDepartamento()

    def createMateria(self, bodyRequest):
        print("Creando Materia...")
        nuevaMateria= Materia(bodyRequest)
        print("Materia a crear en la BD...",nuevaMateria)
        self.repositorioMateria.save(nuevaMateria)
        return True

    def buscarTodasLasMaterias(self):
        print("Buscando todas las materias...")
        return self.repositorioMateria.findAll()

    def buscarMateriaID(self, idObject):
        print("Buscando materia con id: ",idObject)
        materia = Materia(self.repositorioMateria.findById(idObject))
        return materia.__dict__


    def asignarDepartamento(self, idMateria, idDepartamento):
        materiaActual=Materia(self.repositorioMateria.findById(idMateria))
        departamentoActual=Departamento(self.repositorioDepartamento.findById(idDepartamento))
        print("Departamento encontrado: ",departamentoActual.__dict__)
        print("Materia encontrada: ",materiaActual.__dict__)
        materiaActual.departamento = departamentoActual
        print("Materia actualizada:", materiaActual.__dict__)
        return self.repositorioMateria.save(materiaActual)