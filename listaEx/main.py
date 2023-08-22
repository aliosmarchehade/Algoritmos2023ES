import bib, random

num =  bib.pedirNum()
print(f"O número informado foi {num}")



while(True):
    bib.exibirMenu()
    op = int(input("Selecione uma opção: "))


    if(op == 3):
        num = bib.pedirNum()
        a = bib.gerarAleatorios(num)
        print(f"O número aleatório gerado foi: {a}")

    if(op == 4):
        min = bib.pedirNum()
        max = bib.pedirNum()
        par = bib.gerarPar(min,max)
        impar = bib.gerarImpar(min,max)
        print(f"O numero par aleatório gerado foi o: {par}")
        print(f"O numero ímpar aleatório gerado foi o: {impar}")
    
    if(op == 5):
        num = bib.pedirNum()
        mes = bib.mes(num)
        print(f"O mês correspondente é: {mes}")
    
    if(op == 6):
        print("** SELECIONE A EQUAÇÃO DESEJADA: \n A. B. C. ou D.: ")
        op = input("Selecione uma opção: ")

        if(op == "A" or op == "a"):
            x = bib.pedirNum()
            quad = bib.quadrado(x)
            print(f"O quadrado do número {x} é {quad}")
        
        elif(op == "B" or op == "b"):
            altura = bib.pedirNum()
            base = bib.pedirNum()
            ret = bib.retangulo(base, altura)
            print(f"A área do retângulo é {ret}")
        
        elif(op == "C" or op == "c"):
            altura = bib.pedirNum()
            base = bib.pedirNum()
            tra = bib.triangulo(base, altura)
            print(f"A área do triângulo é {tra}")
        
        elif (op == "D" or op == "d"):
            altura = bib.pedirNum()
            baseMaior = bib.pedirNum()
            baseMenor = bib.pedirNum()
            trap = bib.trapezio(baseMaior, baseMenor, altura)
            print(f"A área do trapézio é {trap}")
        
    if(op == 7):
        fat = bib.pedirNum()
        res = bib.fatorial(fat)
        print(f"O fatorial de {fat} é: {res} ")
            
    if(op == 8):
        vetorM = bib.pedirNum()
        res = bib.vetorMaior(vetorM)
        print(f"O maior valor gerado no vetor foi {res} ")

    if(op == 9):
        vetorMin = bib.pedirNum()
        res = bib.vetorMenor(vetorMin)
        print(f"O menor valor do vetor foi: {res} ")
