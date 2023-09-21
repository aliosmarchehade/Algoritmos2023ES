import bib , os

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
        bib.inserirDados(nome)
    
    if(op == 2):
        bib.listarDados(nome)

    if(op == 3):
        procurar = input("Informe um nome à ser procurado: ")
        bib.buscarDados(nome,procurar)

    if(op == 4):
        bib.somaSalarios(nome)

    if(op > 4):
        break

# linha = arquivo.readlines()


# for i in range (0, len(linha)):

#     dados = linha[i].replace("\n", "")
#     dados = dados.split(",")
#     print(f"Nome: {dados[0]}")
#     print(f"Email: {dados[1]}")
#     print(f"Fone: {dados[2]}")
#     print(f"Salário: {dados[3]}")

#     print(linha[i].replace("\n" , "")) 

# arquivo.close()
