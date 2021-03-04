s = 0
ct = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        ct += 1

print(f"A soma de todos os {ct} numeros impares que sao multiplos de tres entre 1 a 500 foi de {s}")
