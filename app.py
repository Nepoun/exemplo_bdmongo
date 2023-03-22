import db

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
                }
            },
            "produtos": {
                "nome": str(input("Nome do produto: \n")),
                "descricao": str(input("Descrição do produto: \n")),
                "preco": str(input("Preço do produto: \n")),
                "vendedor": {
                    "nome": str(input("Nome do vendedor: ")),
                    "sobrenome": str(input("Sobrenome do vendedor: "))
                }
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
            }
        }
    elif escolha == "3":
        #Usuarios
        mydict = {
            "nome": str(input("Nome do usuario: \n")),
            "sobrenome": str(input("Sobrenome do usuario: \n")),
            "cpf": str(input("CPF do usuario: \n")),
            "endereco": {
                "cep": str(input("CEP do usuario:  \n"))
            }
        }
    elif escolha == "4":
        #Vendedor
        mydict = {
            "nome": str(input("Nome do vendedor: ")),
            "sobrenome": str(input("Sobrenome do vendedor: "))
        }

    db.insert(escolha, mydict)
    

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
        "O que deseja fazer? \n 1- Inserir algo novo \n 2- Verificar algum campo \n 3- Verificar todos os documentos \n 4- Apagar documento \n 5- Atualizar documento \n 'voltar' para retornar ao menu principal"
    )
    n = input()
    if n == "voltar":
        continue
    elif n== "1":
        insert_input(escolha)
