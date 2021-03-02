s = 0
for c in range(1, 7):
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        s += num
    else:
        continue
print(f"A soma dos numeros pares sao de {s}")