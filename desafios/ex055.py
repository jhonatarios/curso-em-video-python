maior = 0
menor = 0

for pessoas in range(1, 6):

    peso = float(input("Digite o seu peso: "))

    if pessoas == 1:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso

print(f"\nO maior peso digitado foi de {maior}KG e o menor foi de {menor}KG")