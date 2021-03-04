num = int(input("Digite um numero: "))
c = 0
for div in range(1, num + 1):
    if num % div == 0:
        c += 1
if c == 2:
    print("O numero é primo")
else:
    print("Ele nao é primo")
