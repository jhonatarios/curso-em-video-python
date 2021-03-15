n = c =  m = t = maior = menor = 0
e = "S"

while e in "S":
    n = int(input("Digite um numero inteiro: "))
    t += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    e = str(input("Quer continuar? [S] / [N] ")).upper()

m = n / c
print(f"A media entre os numeros foi de {m}, o maior valor digitado foi {maior} e o menor foi {menor}.")
