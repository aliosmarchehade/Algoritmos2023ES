import functions, random, os

while(True):
    functions.exibirMenu()
    op = int(input("Selecione uma opção: "))
    

    if(op == 1):
        x = int(input("Informe um tamanho para o vetor: ")) 
        vetor = [0] * x
    
    elif(op == 2):
        functions.preencherVetor(vetor)
    elif(op == 3):
        functions.exibirVetor(vetor)
    elif(op == 4):
        x = int(input("Qual valor pesquisar? "))
        functions.quantosValores(vetor, x)
    elif(op == 5):
        break
          