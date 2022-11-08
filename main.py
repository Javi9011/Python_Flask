from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorEstudiante import ControladorEstudiante
from Controladores.ControladorDepartamento import ControladorDepartamento
from Controladores.ControladorInscripcion import ControladorInscripcion
from Controladores.ControladorMateria import ControladorMateria

controladorEstudiante = ControladorEstudiante()
controladorDepartamento = ControladorDepartamento()
controladorInscripcion = ControladorInscripcion()
controladorMateria = ControladorMateria()

app = Flask(__name__)
cors = CORS(app)




@app.route("/estudiantes", methods=['POST'])
def crearEstudiante():
    requestBody = request.get_json()
    print("body request", requestBody)
    result = controladorEstudiante.createEstudiante(requestBody)
    if result:
        return {"result": "El estudiante se creo correctamente"}
    else:
        return {"result": "Error"}

@app.route("/estudiantes/<string:idObject>", methods=['GET'])
def buscarEstudiante(idObject):
        result = controladorEstudiante.buscarEstudiante(idObject)
        if result is None:
            return {"resultado": "No se encuentra el Estudiante en base de datos!"}
        else:
            return jsonify(result)

@app.route("/estudiantes", methods=['GET'])
def buscarTodosLosEstudiantes():
    result = controladorEstudiante.buscarTodosLosEstudiantes()
    if not result:
        return {"resultado": "No se encuentran items en la base de datos!"}
    else:
        return jsonify(result)


@app.route("/estudiantes", methods=['PUT'])
def actualizarElEstudiante():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorEstudiante.actualizarEstudiante(id, requestBody)
    if result:
        return {"resultado": "Estudiante actualizado!"}
    else:
        return {"resultado": "Error al actualizar el Estudiante!"}

@app.route("/estudiantes/<string:idObject>", methods=['DELETE'])
def eliminarEstudiante(idObject):
    result = controladorEstudiante.eliminarEstudiante(idObject)
    if result:
        return {"resultado": "Estudiante eliminado!"}
    else:
        return {"resultado": "Error al eliminar el Estudiante!"}

@app.route("/departamento", methods=['POST'])
def crearDepartamento():
    requestBody=request.get_json()
    print("body request", requestBody)
    result = controladorDepartamento.createDepartamento(requestBody)
    if result:
        return {"result": "El departamento se creo correctamente"}
    else:
        return {"result": "Error"}

@app.route("/departamento", methods=['GET'])
def buscarTodosDeptos():
    result=controladorDepartamento.buscarTodosLosDepartamentos()
    if not result:
        return {"resultado": "No se encuentran items en la base de datos!"}
    else:
        return jsonify(result)

@app.route("/departamento/<string:idObject>", methods=['GET'])
def buscarById(idObject):
    result = controladorDepartamento.buscarPorId(idObject)
    if result is None:
        return {"resultado": "No se encuentra el departamento en base de datos!"}
    else:
        return jsonify(result)

@app.route("/materia", methods=['POST'])
def crearMateria():
    requestBody=request.get_json()
    print("body Request",requestBody)
    result = controladorMateria.createMateria(requestBody)
    if result:
        return {"result": "La materia se creo correctamente"}
    else:
        return {"result": "Error"}

@app.route("/materia", methods=['GET'])
def buscarTodas():
    result = controladorMateria.buscarTodasLasMaterias()
    if not result:
        return {"resultado": "No se encuentran items en la base de datos!"}
    else:
        return jsonify(result)

@app.route("/materia/<string:idObject>", methods=['GET'])
def buscarMateria(idObject):
    result = controladorMateria.buscarMateriaID(idObject)
    if result is None:
        return {"resultado": "No se encuentra el departamento en base de datos!"}
    else:
        return jsonify(result)

@app.route("/materia/<string:idMateria>/departamento/<string:idDepartamento>", methods=['PUT'])
def asignarDeptoAMateria(idMateria,idDepartamento):
    result=controladorMateria.asignarDepartamento(idMateria,idDepartamento)
    return jsonify(result)

@app.route("/inscripciones/estudiante/<string:idEstudiante>/materia/<string:idMateria>", methods=['POST'])
def crearNewInscripcion(idEstudiante,idMateria):
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorInscripcion.crearInscripcion(requestBody, idEstudiante, idMateria)
    return jsonify(result)




def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])