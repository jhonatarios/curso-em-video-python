num = int(input("Digite um numero de 0 a 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 %10
m = num // 1000 % 10
print("Milhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}".format(m, c, d, u))
