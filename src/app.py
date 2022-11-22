from flask import Flask, request, Response
from flask_pymongo import PyMongo, ObjectId
import os
from dotenv import load_dotenv
from bson import json_util
import datetime


load_dotenv()
app = Flask(__name__)

#Conexion a la bd de mongo
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo = PyMongo(app)

#Ruta para crear una nueva calidad
@app.route('/quality', methods=['POST'])
def createQuality():
    data = request.json['data']

    if data:
        mongo.db.quality.insert_one({
            'data': data,
            'date': datetime.datetime.now()
        })
        response = {
            'data': data,
            'message': 'Data saved successfully',
            'statusCode': 200
        }
        return response, 200
    else:
        return {'message': 'Data not saved'}, 500

#Ruta para obtener todas las calidades
@app.route('/quality', methods=['GET'])
def getQuality():
    data = mongo.db.quality.find()
    response = json_util.dumps(data)
    return Response(response, mimetype='application/json')
    

#Ruta para obtener una calidad por id
@app.route('/quality/<id>', methods=['GET'])
def getQualityById(id):
    data = mongo.db.quality.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(data)
    return Response(response, mimetype='application/json')

#manejador de errores
@app.errorhandler(404)
def not_found(error=None):
    response = {
        'message': 'Resource not found' + request.url,
        'status': 404
    }
    return response


if __name__ == '__main__':
    app.run(debug=True)