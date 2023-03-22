import pymongo
from pymongo.server_api import ServerApi

user = "antonho"
password = "mZWF2JwetHeuSwED"

client = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@cluster0.9c8yf38.mongodb.net/?retryWrites=true&w=majority")
db = client.test

global mydb
mydb = client.MercadoLivre

def getCol(db, escolha):
    if(escolha == "1"):
        mycol = mydb.compras
    elif(escolha == "2"):
        mycol = mydb.produtos
    elif(escolha == "3"):
        mycol = mydb.usuarios
    elif(escolha == "4"):
        mycol = mydb.vendedor
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
        print(x)

def findQuery(escolha, coluna, procura):
    #Query
    global mydb
    mycol = getCol(mydb, escolha)
    print("\n####QUERY####")
    myquery = { coluna: procura }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

def updateQuery(id, values, escolha):
    global mydb
    mycol = getCol(mydb, escolha)
    print("\nATUALIZANDO...") 
    newvalues = { "$set" : values }
    
    mydoc = mycol.update_one({"_id": id }, newvalues)






