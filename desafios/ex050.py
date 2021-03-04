s = 0
ct = 0

for c in range(1, 7):
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        s += num
        ct += 1

print(f"A soma dos {ct} numeros pares sao de {s}")
