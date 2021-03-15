n = 0
c = -1
t = 0
while not n == 999:
    n = int(input("Digite um numero inteiro: "))
    t += n
    c += 1
print(f"No total foram digitados {c} numeros, resulto no total de {t-999}.")
