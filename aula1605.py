# 1- Para cada conjunto de valores abaixo, escreva o código necessário para criar vetores:

# a) 9  18  41  65  88  121

vetor = [9 , 18 , 41 , 65 , 88 , 121]
print(vetor)

# b) Rafael   Ayslan   Daniela   Frank

vetor = ["Rafael" , "Ayslan" , "Daniela" , "Frank"]
print(vetor)

# c) 3290,90   128,50   85,90   789,31

vetor = [3290.90 , 128.50 , 85.90 , 789.31]
print(vetor)

# d) Um vetor com tamanho 5 e preenchido com números fornecidos também pelo usuário.

vetor = [0] * 5

vetor[0] = int(input("Informe um valor: "))
vetor[1] = int(input("Informe um valor: "))
vetor[2] = int(input("Informe um valor: "))
vetor[3] = int(input("Informe um valor: "))
vetor[4] = int(input("Informe um valor: "))
print(vetor)


# 2- Considerando o vetor criado no exercício 1.d:

# a) Apresente na tela todos os valores do vetor.

print(vetor)

# b) Apresente na tela todos os valores do vetor em ordem invertida (de trás para frente).

vetor.reverse()
print(vetor)

# c) Apresente na tela o dobro de todos os valores do vetor

print(vetor[0] * 2 , vetor[1] * 2 , vetor[2] * 2 ,  vetor[3] * 2 , vetor[4] * 2) 

# d) Apresente na tela a metade de todos os valores do vetor.

print(vetor[0] / 2 , vetor[1] / 2 , vetor[2] / 2 ,  vetor[3] / 2 , vetor[4] / 2) 


# 3- Crie um vetor de strings para armazenar quatro dados do usuário: nome completo, endereço, telefone e email.

# a) Apresente na tela, de maneira organizada, todos os dados do usuário, exemplo:
#Nome completo: 	Rafael Zottesso
#Endereço: 		    Rua ABC, 123
#Telefone: 		    (99) 99999-9999
#E-mail: 			rafael.zottesso@ifpr.edu.br


vetor = [0] * 4

vetor[0] = str(input("Informe seu nome Completo: "))
vetor[1] = str(input("Informe seu Endereço: "))
vetor[2] = str(input("Informe seu Telefone: "))
vetor[3] = str(input("Informe seu Email: "))

print (f"Nome completo: \t {vetor[0]} \nEndereço: \t {vetor[1]} \nTelefone: \t {vetor[2]} \nEmail: \t\t {vetor[3]}")


# 4- Crie um vetor com 4 números decimais (ponto-flutuante) de modo que o usuário do programa vá digitar esses valores.

vetor = [0] * 4

vetor[0] = float(input("Informe um número: "))
vetor[1] = float(input("Informe um número: "))
vetor[2] = float(input("Informe um número: "))
vetor[3] = float(input("Informe um número: "))

# a) Apresente na tela a soma de todos os valores.

print(f"\nA soma dos números é: {vetor[0] + vetor[1] + vetor[2] + vetor[3]}")

# b) Apresente a média dos números 

print(f"A média dos números é: {(vetor[0] + vetor[1] + vetor[2] + vetor[3]) / 4}")

# c) Apresente na tela o produto (multiplicação) de todos os valores.

print(f"O produto dos números é: {vetor[0] * vetor[1] * vetor[2] * vetor[3]}")

# d) Apresente na tela somente quantos valores são maiores do que 1000

soma = 0
if(vetor[0] > 1000):
    soma = soma + 1

if(vetor[1] > 1000):
    soma = soma + 1

if(vetor[2] > 1000):
    soma = soma + 1

if(vetor[3] > 1000):
    soma = soma + 1

print(f"{soma} número(s) são maiores que 1.000!!")

# e) Apresente na tela a quantidade de valores que são maiores do que zero.

soma = 0
if(vetor[0] > 0):
    soma = soma + 1

if(vetor[1] > 0):
    soma = soma + 1

if(vetor[2] > 0):
    soma = soma + 1

if(vetor[3] > 0):
    soma = soma + 1

print(f"{soma} número(s) são maiores que 0!!")

# f) Apresente na tela quantos valores são pares.

pares = 0
if(vetor[0] %2 == 0):
    pares = pares + 1

if(vetor[1] %2 == 0):
    pares = pares + 1

if(vetor[2] %2 == 0):
    pares = pares + 1

if(vetor[3] %2 == 0):
    pares = pares + 1

print(f"{pares} número(s) são números pares!!")

# g) Apresente na tela somente o maior valor do vetor.

maior = max(vetor)
print(f"O maior número do vetor é: {maior}")

# h) Apresenta na tela somente o índice do maior valor do vetor.

maiorind = vetor.index(max(vetor))
print(f"O indice do maior número é o indice {maiorind}")

# i) Apresente na tela somente o menor valor do vetor

menor = min(vetor)
print(f"O menor número do vetor é: {menor}")

# j) Apresenta na tela somente o índice do menor valor do vetor.

menorind = vetor.index(min(vetor))
print(f"O indice do menor número é o indice {menorind}")
