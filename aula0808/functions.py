def exibirMenu():
    print("== MENU DE OPÇÕES ==\n\n1. Criar Vetor\n2. Preencher Vetor\n3. Exibir Vetor\n4. Exibir quantos valores x tem no vetor\n5. Sair")  
  
def preencherVetor(vetor):
     for i in range (0, len(vetor)):
          vetor[i] = int(input("Valor: ")) 

def exibirVetor(vetor):
    print("[", end="")
    for i in range (0, len(vetor)):
        print(vetor[i], end="")
        if( i < len(vetor) -1):
            print(", ", end="")
    print("]")

def quantosValores(vetor,x):
    total = 0
    for i in range(0, len(vetor)):
        if(vetor[i] == x):
            total += 1
    print(f"Existem {total} números", x)