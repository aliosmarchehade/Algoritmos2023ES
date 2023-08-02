a = int(input("Digite um número "))
b = int(input("Digite um número "))
c = int(input("Digite um número "))

if(a > b and a > c):
    print(f" O número {a} é o maior de todos")
elif (b > a and b > c):
    print(f" O número {b} é o maior de todos")
else:
    print(f" O número {c} é o maior de todos")