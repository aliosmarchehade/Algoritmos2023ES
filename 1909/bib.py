def menu():
    print("== Menu == ")
    print("1. Inserir dados (no arquivo)")
    print("2. Listar dados (todos)")
    print("3. Buscar dados (pelo nome)")
    print("4. Soma salários (no arquivo)")
    op = int(input("Selecione uma opção: "))

def inserirDados(nome):

    arquivo = open("nomes.txt", "a")

    nome = input("Informe seu nome completo: ")
    arquivo.write(nome + ",")

    email = input("Informe seu e-mail: ")
    arquivo.write(email)
    arquivo.write(",")

    salario = input("Informe seu salário: ")
    arquivo.write(salario)
    arquivo.write(",")

    dtnasc = input("Informe sua data de nascimento: ")
    arquivo.write(dtnasc)

    arquivo.write("\n")

    arquivo.close()

def listarDados(nome):

    arquivo = open("nomes.txt", "r")
    linha = arquivo.readlines()


    for i in range (0, len(linha)):

        dados = linha[i].replace("\n", "")
        dados = dados.split(",")
        print(f"Nome: {dados[0]}")
        print(f"Email: {dados[1]}")
        print(f"Salário: {dados[2]}")
        print(f"Data de nascimento: {dados[3]}")

        print(linha[i].replace("\n" , "")) 

    arquivo.close()

def buscarDados(nome, procurar):
    arquivo = open(nome + ".txt", "r")
    linha = arquivo.readlines()
    for i in range(0, len(linha)):
        dados = linha[i].split(";")
        if(procurar in dados[0]):
            print(f"O nome {procurar} está listado!")

    arquivo.close()

def somaSalarios(nome):
    arquivo = open(nome + ".txt", "r")
    linha = arquivo.readlines()
    salario = 0
    for i in range(0, len(linha)):
        dados = linha[i].split(";")
        dados[2] = int(dados[2])
        salario += dados[2]
    arquivo.close()