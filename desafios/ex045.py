from random import randrange
escolha = int(input("Escolha um para jogar:\n1-Pedra\n2-Papel\n3-Tesoura\n"))
pc = randrange(1, 3)
pedra = 1
papel = 2
tesoura = 3
if pc == pedra and escolha == papel:
    print("{}. Voce ganhou!".format(pc))
elif pc == pedra and escolha == tesoura:
    print("{}. Voce perdeu.".format(pc))
elif pc == papel and escolha == tesoura:
    print("{}. Voce ganhou!".format(pc))
elif pc == papel and escolha == pedra:
    print("{}. Voce perdeu.".format(pc))
elif pc == tesoura and escolha == pedra:
    print("{}. Voce ganhou!".format(pc))
elif pc == tesoura and escolha == papel:
    print("{}. Voce perdeu.".format(pc))
else:
    print("{}. Empate!".format(pc))
