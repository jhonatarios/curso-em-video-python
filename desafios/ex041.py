from datetime import date
ano = int(input("Digite o seu ano de nascimento: "))
idade = date.today().year - ano
if idade <= 9:
    print("Mirim")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Junior")
elif idade <= 20:
    print("Senior")
else:
    print("Master")