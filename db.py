import pymongo
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import json
from RedisManager import MongoEncoder

user = "antonho"
password = "12345"

client = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@cluster0.9c8yf38.mongodb.net/?retryWrites=true&w=majority")
db = client.test

global mydb
mydb = client.MercadoLivre

def printDict(objectToPrint):

    temp = json.dumps((objectToPrint), cls=MongoEncoder, indent=4)

    print(temp)

def getCol(db, escolha):
    mycol = db.usuarios
    if(escolha == "1"):
        mycol = db.compras
    elif(escolha == "2"):
        mycol = db.produtos
    elif(escolha == "3"):
        mycol = db.usuarios
    elif(escolha == "4"):
        mycol = db.vendedor
    return mycol

def insert(escolha, dict):
    #Insert
    global mydb
    mycol = getCol(mydb, escolha)

    print("INSERÇÃO...")
    x = mycol.insert_one(dict)
    print(x.inserted_id)

def findSort(escolha):
    #Sort
    global mydb
    mycol = getCol(mydb, escolha)
    print("\nBUSCANDO...") 
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        printDict(x)

def findQuery(escolha, coluna, procura):
    #Query
    global mydb
    mycol = getCol(mydb, escolha)
    print("\nPROCURANDO...")
    myquery = { coluna: procura }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        printDict(x)
        return x


def updateQuery(id, values, escolha):
    global mydb
    mycol = getCol(mydb, escolha)
    print("\nATUALIZANDO...") 
    newvalues = { "$set": values }
    
    mycol.update_one({"_id": ObjectId(id) }, newvalues)

def deleteQuery(coluna, procura, escolha):
    #Query
    global mydb
    mycol = getCol(mydb, escolha)
    print("\nDELETANDO...")
    myquery = { coluna: procura }
    mycol.delete_one(myquery)






