import math
import random
import os

while(True):
    os.system("cls") or None
    menu = int(input("MENU PRINCIPAL(selecione um valor):\n\n1. Calculo Aritmético\n2. Contagem\n3. Sortear Número\n4. Sair do sistema\n"))
    
    if(menu == 1):
        while(True):
            os.system("cls") or None
            print("Calculo Aritmético:")
            print("1. Tabuada de um número")
            print("2. Raiz quadrada")
            print("3. Potência")
            print("4. Volta")
            menu1 = int(input())

            if(menu1 == 1):
                print("Tabuada de um número")
                x = int(input("Informe um número: "))
                for i in range (1,11):
                    print(f"{x} * {i} = {x*i}")

            elif(menu1 == 2):
                print("Raiz quadrada")   
                x = int(input("Informe um número para calcular raiz: "))
                print(f"A raíz quadrada de {x} é: {math.sqrt(x)}!!")

            elif(menu1 == 3):
                print("Potência")
                x = int(input("Informe um número para calcular potência: "))
                x1 = int(input("Informe um valor para essa potência: "))
                print(f"{x} elevado a {x1} = {x ** x1}")

            elif(menu1 == 4):
                break
            
            else:
                print("Opção Inválida!!")
           
            input("Confirme com um ENTER")


    elif(menu == 2):
        while(True):
            os.system("cls") or None
            print("Contagem:")
            print("1. Contar de 1 a 20 de n em n")
            print("2. Contar do início ao fim de n em n")
            print("3. Voltar")
            menu2 = int(input())

            if(menu2 == 1):
                for x in range (1, 21):
                    print(x)

            elif(menu2 == 2):
                x1 = int(input("Informe um número para iniciar contagem: "))
                x2 = int(input("Informe outro número para finalizar a contagem: "))

                for x in range (x1,x2):
                    print(x)

            elif(menu2 == 3):
                break
           
            else:
                print("Opção Inválida!!")
           
            input("Confirme com um ENTER")


    elif(menu == 3):
        while(True):
            os.system("cls") or None
            print("Sortear Número")
            print("1. Sortear de 1 a 10")
            print("2. Sortear de n a n")
            print("3. Voltar")
            menu3 = int(input())

            if(menu3 == 1):
                x = random.randint(1,10)
                print(f"O número sorteado foi {x}")

            elif(menu3 == 2):
                x1 = int(input("Informe um número para iniciar contagem do sorteio: "))
                x2 = int(input("Informe outro número para finalizar a contagem do sorteio: "))
                x3 = random.randint(x1,x2)

                print(f"O número sorteado foi {x3}")

            elif(menu3 == 3):
                break
                
            else:
                print("Opção Inválida!!")
            
            input("Confirme com um ENTER")
            

    elif(menu == 4):
        print("Sair do Sistema.")
        break

    input("Confirme com um ENTER")

