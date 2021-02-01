import random

numero = random.randrange(0, 5)
escolha = int(input("\nAdvinhe um numero de 0 a 5: "))

if escolha == numero:
    print("Parabens voce acertou!")
else:
    print("Ah que pena, voce errou :c")
