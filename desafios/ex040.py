a = float(input("Digite o valor da primeira nota: "))
b = float(input("Digite o valor da segunda nota: "))
media = (a + b) / 2
if media < 5.0:
    print("Reprovado!")
elif 5.0 <= media <= 6.9:
    print("Recuperacao.")
else:
    print("Aprovado!")
