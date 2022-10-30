from Modelos.Departamento import Departamento


class ControladorDepartamento():
    def __init__(self):
        print("Entra al constructor de la clase controlador")

    def createDepartamento(self, bodyRequest):
        print("Creando el departamento...")
        nuevoDepartamento = Departamento(bodyRequest)
        print("Departamento a crear en la BD: ", nuevoDepartamento.__dict__)
        self.repositorioDepartamento.save(nuevoDepartamento)
        return True