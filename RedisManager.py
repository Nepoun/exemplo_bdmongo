import pymongo
import redis
import json
from bson import ObjectId
import db;
import ast;

r = redis.Redis(
  host='redis-11117.c274.us-east-1-3.ec2.cloud.redislabs.com',
  port=11117,
  password='123456')

class MongoEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

def iniciarRedis():
    nome = input("Digite nome")

    client = db.findQuery(1, "nome", nome)

    clientToString = json.dumps((client), cls=MongoEncoder)

    r.set('usuarios', clientToString)

    print("Cliente inserido no REDIS com sucesso")

    redisUser = str(r.get('usuarios'))
    _clientToString = redisUser[2:-1]
    _stringToObj = json.loads(_clientToString)

    print("\n Cadastrar novo favorito")

    newFavObj = {
        "id" : str(input("Digite um id: \n")),
        "favName" : str(input("Digite um nome: \n")),
        "preco" : str(input("digite um preço: \n"))
    }

    _stringToObj["favoritos"].append(newFavObj)

    _objToString = json.dumps((_stringToObj), cls=MongoEncoder)

    r.delete('usuarios')
    r.set('usuarios', _objToString)

    objectToUpdate = json.loads(r.get('usuarios'))

    del objectToUpdate["_id"]

    db.updateQuery(str(client["_id"]), objectToUpdate, 1)

    print("Favorito novo cadastrado")