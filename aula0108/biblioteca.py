def qualCategoria(a):

    if(a>=0 and a<=4):
        print(f"Sua categoria se encaixa como Júnior")
    elif (a >= 5 and a <= 8):
        print(f"Sua categoria se encaixa como Pleno")
    elif(a>=9 and a<=35):
        print(f"Sua categoria se encaixa como Sênior")
    else:
        print(f"Você está aposentado!")