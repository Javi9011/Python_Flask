from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)


@app.route("/grupo25/<string:variable1>", methods=['GET'])
def estaEsUnaFuncionQueRetornaUnMensaje(variable1):
    mensajeJson = {}
    mensajeJson["id_del_grupo"] = 25
    mensajeJson["idVariable"] = variable1
    return jsonify(mensajeJson)

@app.route("/grupo25", methods=['POST'])
def methodPostTest():
    response = {
        "key1": "value1",
        "key2": "value2"
    }
    return response

@app.route("/grupo25", methods=['PUT'])
def methodPutTest():
    return {
        "method": "PUT"
    }

@app.route("/grupo25", methods=['DELETE'])
def methodDeleteTest():
    response = {
        "method": "DELETE"
    }
    return response

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])