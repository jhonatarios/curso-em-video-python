from random import randrange

numero = randrange(0, 10) # Randomizar um numero
escolha = 30
tentativas = 0

while not escolha == numero:
    escolha = int(input("\nAdvinhe um numero de 0 a 10: "))
    if escolha == numero:
        print(f"\033[32mParabens voce acertou! Foram necessarias {tentativas} tentativas para voce acertar.\033[m")
        break
    else:
        print("\033[31mAh que pena, voce errou :c, tente novamente\033[m")
        tentativas += 1
