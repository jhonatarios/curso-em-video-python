r1 = float(input("Digite o valor da primeira reta: "))
r2 = float(input("Digite o valor da segunda reta: "))
r3 = float(input("Digite o valor da terceira reta: "))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r2 + r1:
    print('\033[32mAs retas podem formar um triangulo!\033[m')
else:
    print('\033[31mAs retas não podem formar um triangulo!\033[m')
