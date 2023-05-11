import os
import json
import requests

while(True):
    os.system("cls") or None

    menu = int(input("MENU PRINCIPAL(selecione um valor):\n\n1. Frete\n2. Produtos\n3. Buscar Endereço "))         
    
    if(menu == 1):
        peso = float(input("Informe o peso da entrega (em Kg) "))
        distancia = float(input("Informe a distancia da entrega (em Km) "))

       
        frete = distancia * 1.50
    

        if(peso > 30):
                peso = (peso - 30)
                frete = peso * 5 + frete
                

        if(distancia > 100):
                frete = frete - (frete * 0.1)

        print(f"O valor do frete foi de: R${frete} ")
            

    elif(menu == 2):

        somar = 0
        preco = 1

        while(preco>0):
            preco = float(input("Informe o valor para o produto: "))
            somar = preco + somar
        print(f"A soma total dos valores apresentados foi {somar}")


    elif(menu == 3):
        cep = input("Informe seu cep: ")
        viacep = f"https://viacep.com.br/ws/{cep}/json/"
        dados = requests.get(viacep)
        dados_json = dados.json()
        print(dados_json)

    input("Confirme um ENTER para sair")

