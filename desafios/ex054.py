import datetime
year = datetime.date.today().year

maior = 0
menor = 0

for pessoas in range(1, 8):
    ano = int(input("Digite o seu ano de nascimento: "))
    if (year - ano) > 21 or (year - ano) < -21:
        maior += 1
    else:
        menor += 1

print(f"Ha um total de {maior} maiores de idade e {menor} menores de idade")
