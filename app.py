import db
import RedisManager

def favorite_loop():
    n = "a"
    allFavorites = []
    print("ESCOLHA DE FAVORITOS. Coloque 0 para terminar de escolher \n")
    while n != "0":
        n = str(input("Escolha mais um favorito: "))
        if n != "0":
            allFavorites.append(n)
    
    return allFavorites

def insert_input(escolha):
    mydict = {}
    if escolha == "1":
        #Compras
        mydict = {
            "usuario": {
                "nome": str(input("Nome do usuario:\n")),
                "sobrenome": str(input("Sobrenome do usuario:\n")),
                "cpf": str(input("CPF do usuario:\n")),
                "endereco": {
                    "cep": str(input("CEP do usuario\n"))
                },
                "favoritos": favorite_loop()
            },
            "produtos": {
                "nome": str(input("Nome do produto: \n")),
                "descricao": str(input("Descrição do produto: \n")),
                "preco": str(input("Preço do produto: \n")),
                "vendedor": {
                    "nome": str(input("Nome do vendedor: ")),
                    "sobrenome": str(input("Sobrenome do vendedor: "))
                },
                "favoritos": favorite_loop()
            }
        }
    elif escolha == "2":
        #Produtos
        mydict = {
            "nome": str(input("Nome do produto: \n")),
            "descricao": str(input("Descrição do produto: \n")),
            "preco": str(input("Preço do produto: \n")),
            "vendedor": {
                "nome": str(input("Nome do vendedor: ")),
                "sobrenome": str(input("Sobrenome do vendedor: "))
            },
            "favoritos": favorite_loop()
        }
    elif escolha == "3":
        #Usuarios
        mydict = {
            "nome": str(input("Nome do usuario: \n")),
            "sobrenome": str(input("Sobrenome do usuario: \n")),
            "cpf": str(input("CPF do usuario: \n")),
            "endereco": {
                "cep": str(input("CEP do usuario:  \n"))
            },
            "favoritos": favorite_loop()
            
        }
    elif escolha == "4":
        #Vendedor
        mydict = {
            "nome": str(input("Nome do vendedor: ")),
            "sobrenome": str(input("Sobrenome do vendedor: "))
        }

    return mydict
    

n = "comece"
escolha = "nada"
while (n != "parar"):
    print(
        "Selecione uma coleção \n 1- Compras \n 2- Produtos \n 3- Usuarios \n 4- Vendedor \n\n Escreva 'parar' para sair"
    )
    n = str(input())
    if n == 'parar':
        continue
    else:
        escolha = n

    print(
        "O que deseja fazer? \n 1- Inserir documento novo \n 2- Verificar documento por coluna \n 3- Verificar todos os documentos \n 4- Apagar documento \n 5- Atualizar documento \n 'voltar' para retornar ao menu principal \n Se deseja mandar algo para o REDIS, vá na opção 2"
    )
    n = input()
    if n == "voltar":
        continue
    elif n == "1":
        dict = insert_input(escolha)
        db.insert(escolha, dict)
    elif n == "2":
        coluna = input("Qual coluna você quer? \n")
        procura = input("O que você busca? \n")

        selected = db.findQuery(escolha, coluna, procura)

        opcao = int(input("\n Deseja mandar para o REDIS? \n 0 - Não \n 1 - Sim"))

        if(opcao == 1):
            RedisManager.setDb(escolha, selected)


    elif n == "3":
        db.findSort(escolha)
    elif n == "4":
        coluna = input("Qual coluna você quer buscar para apagar? \n")
        procura = input("O que você busca apagar? \n")    
        db.deleteQuery(coluna, procura, escolha)
    elif n == "5":
        id = input("Qual o id? \n")
        dict = insert_input(escolha)
        db.updateQuery(id, dict, escolha)