import random

def pedirNum():
    a = int(input("Informe um número inteiro: "))
    return a

def exibirMenu():
    print(f"Selecione uma das opções de exercício: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 ou 19: ")
   
   
def gerarAleatorios(num):
    b = random.randint(1, num)
    return b

def gerarPar(min,max):
    b = random.randint(min, max)
    while (b % 2 != 0):
        b = random.randint(min, max)
    return b

def gerarImpar(min,max):
    b = random.randint(min, max)
    while (b % 2 == 0):
        b = random.randint(min, max)
    return b

def mes(num):
    if (num == 1): 
        return "Janeiro"
    elif (num == 2):
        return "Fevereiro"
    elif (num == 3):
        return "Março"
    elif (num == 4):
        return "Abril"
    elif (num == 5):
        return "Maio"
    elif (num == 6):
        return "Junho"
    elif (num == 7):
        return "Julho"
    elif (num == 8):
        return "Agosto"
    elif (num == 9):
        return "Setembro"
    elif (num == 10):
        return "Outubro"
    elif (num == 11):
        return "Novembro"
    elif (num == 12):
        return "Dezembro"
    else:
        return "Mês Inválido!"
    
def quadrado(x):
   
    return x**2

def retangulo(base, altura):

    return base * altura

def triangulo (base, altura):

    return (base * altura) / 2

def trapezio (baseMaior, baseMenor, altura):

    return ((baseMaior + baseMenor) * altura) / 2
    
def fatorial(fat):
    if fat == 1:
        return 1
    else:
        res = fat * fatorial(fat-1)
        return res
    
def vetorMaior(vetorM):
    vetor = [0] * vetorM 
    maiorNumero = 0
    for i in range(0, len(vetor), 1):
        vetor[i] = random.randint(1,100)
    for i in range(0, len(vetor), 1):
        if(vetor[i] > maiorNumero):
            maiorNumero = vetor[i]
        
    print(f"Os valores do vetor foram: {vetor}")
    return maiorNumero


def vetorMenor(vetorMin):
    vetor = [0] * vetorMin
    menorNumero = 100
    for i in range(0, len(vetor), 1):
        vetor[i] = random.randint(1,100)
    for i in range(0, len(vetor), 1):
        if(vetor[i] < menorNumero):
            menorNumero = vetor[i]
        
    print(f"Os valores do vetor foram: {vetor}")
    return menorNumero
