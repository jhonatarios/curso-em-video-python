n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

if n1 > n2 and n1 > n3:
    print("{} é o maior numero".format(n1))

if n2 > n1 and n2 > n3:
    print("{} é o maior numero".format(n2))

if n3 > n1 and n3 > n2:
    print("{} é o maior numero".format(n3))
