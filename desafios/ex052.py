num = int(input("Digite um numero inteiro: "))
c = 0

for div in range(1, num + 1):
    res = num % div
    if res == 0:
        c += 1
    else:
        continue
if c == 2:
    print("O numero é primo")
else:
    print("Ele nao é primo")



