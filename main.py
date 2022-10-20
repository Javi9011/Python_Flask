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
def actualizarEstudiante():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorEstudiante.actualizarEstudiante(requestBody)
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





def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])