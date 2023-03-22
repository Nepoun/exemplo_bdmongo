import pymongo
from pymongo.server_api import ServerApi

user = "antonho"
password = "mZWF2JwetHeuSwED"

client = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@cluster0.9c8yf38.mongodb.net/?retryWrites=true&w=majority")
db = client.test

global mydb
mydb = client.MercadoLivre

def insert(escolha, dict):
    #Insert
    global mydb
    mycol = mydb.usuarios

    if(escolha == "1"):
        mycol = mydb.compras
    elif(escolha == "2"):
        mycol = mydb.produtos
    elif(escolha == "3"):
        mycol = mydb.usuarios
    elif(escolha == "4"):
        mycol = mydb.vendedor

    print("INSERÇÃO...")
    x = mycol.insert_one(dict)
    print(x.inserted_id)

def findSort():
    #Sort
    global mydb
    mycol = mydb.usuarios
    print("\nBUSCANDO...") 
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        print(x)

def findQuery(coluna, procura):
    #Query
    global mydb
    mycol = mydb.usuarios
    print("\n####QUERY####")
    myquery = { coluna: procura }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

def updateQuery(id, values):
    global mydb
    mycol = mydb.usuarios
    print("\nATUALIZANDO...") 
    newvalues = { "$set" : values }
    
    mydoc = mycol.update_one({"_id": id }, newvalues)

    for x in mydoc.find():
        print(x)






