from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorEstudiante import ControladorEstudiante

app = Flask(__name__)
cors = CORS(app)

controladorEstudiante = ControladorEstudiante()


@app.route("/estudiantes", methods=['POST'])
def crearEstudiante():
    requestBody = request.get_json()
    print("body request",requestBody)
    result = controladorEstudiante.createEstudiante()
    if(result):
        return {"result":"El estudiante se creo correctamente"}
    else:
        return {"result":"Error"}
@app.route("/estudiantes", methods=['GET'])
def getEstudiantes():
    json=controladorEstudiante.listar()
    return jsonify(json)

@app.route("/estudiantes</string:id>", methods=['GET'])
def getEstudiante():
    json=controladorEstudiante.show()
    return jsonify(json)

@app.route("/estudiantes</string:id>", methods=['PUT'])
def modificarEstudiante():
    data = request.get_json()
    json=controladorEstudiante.update(id,data)
    return jsonify(json)

@app.route("/estudiantes</string:id>", methods=['DELETE'])
def eliminarEstudiante(id):
    json=controladorEstudiante.delete(id)
    return jsonify(json)





def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])