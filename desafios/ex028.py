from random import randrange

numero = randrange(0, 5) # Randomizar um numero
escolha = int(input("\nAdvinhe um numero de 0 a 5: "))

if escolha == numero:
    print("\033[32mParabens voce acertou!\033[m")
else:
    print("\033[31mAh que pena, voce errou :c\033[m")
