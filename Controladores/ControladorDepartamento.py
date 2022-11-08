from Modelos.Departamento import Departamento
from Repositorios.RepositorioDepartamento import RepositorioDepartamento


class ControladorDepartamento():
    def __init__(self):
        print("Entra al constructor de la clase controlador")
        self.repositorioDepartamento=RepositorioDepartamento()

    def createDepartamento(self, bodyRequest):
        print("Creando el departamento...")
        nuevoDepartamento = Departamento(bodyRequest)
        print("Departamento a crear en la BD: ", nuevoDepartamento.__dict__)
        self.repositorioDepartamento.save(nuevoDepartamento)
        return True

    def buscarTodosLosDepartamentos(self):
        print("Buscando departamentos en la BD...")
        return self.repositorioDepartamento.findAll()

    def buscarPorId(self, idObject):
        print("Buscando el departamento...",idObject)
        depto= Departamento(self.repositorioDepartamento.findById(idObject))
        return depto.__dict__

