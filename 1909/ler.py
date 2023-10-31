import escrever , os

nome = input("Informe um nome pro arquivo: ")

while(True):
    print("== Menu == ")
    print("1. Inserir dados (no arquivo)")
    print("2. Listar dados (todos)")
    print("3. Buscar dados (pelo nome)")
    print("4. Soma salários (no arquivo)")
    op = int(input("Selecione uma opção: "))

    os.system("cls")
    if(op == 1):
        escrever.inserirDados(nome)
    
    if(op == 2):
        escrever.listarDados(nome)

    if(op == 3):
        procurar = input("Informe um nome à ser procurado: ")
        escrever.buscarDados(nome,procurar)

    if(op == 4):
        escrever.somaSalarios(nome)

    if(op > 4):
        break
