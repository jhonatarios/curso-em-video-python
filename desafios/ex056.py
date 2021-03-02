soma = 0
cm = 0
media = 0
maior = 0
nomeHomemMaisVelho = ""

for pessoas in range(1, 5):
    nome = str(input("Digite um nome: "))
    idade = int(input("Digite uma idade: "))
    sexo = str(input("Digite o seu sexo (M/F): ")).upper()[0]

    soma = soma + idade
    media = soma / pessoas

    if sexo == "M" and idade > maior:
        maior = idade
        nomeHomemMaisVelho = nome

    if sexo == "F" and idade < 20:
        cm += 1

print(f"A media das idades é de {media:.2f}\nNome do homem mais velho é: {nomeHomemMaisVelho}")

if cm == 0:
    print("Nenhuma mulher com menos de 20 anos foi citada")
else:
    print(f"Ao todo temos um total de {cm} mulhere(s) com menos de 20 anos.")