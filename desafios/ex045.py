from random import randrange
escolha = int(input("Escolha um para jogar:\n1-Pedra\n2-Papel\n3-Tesoura\n"))
pc = randrange(1, 3)
pedra = 1
papel = 2
tesoura = 3
if pc == pedra and escolha == papel:
    print("Computador jogou PEDRA\nJogador jogou PAPEL\n\nVoce ganhou!")
elif pc == pedra and escolha == tesoura:
    print("Computador jogou PEDRA\nJogador jogou TESOURA\n\nVoce perdeu.")
elif pc == papel and escolha == tesoura:
    print("Computador jogou PAPEL\nJogador jogou TESOURA\n\nVoce ganhou!")
elif pc == papel and escolha == pedra:
    print("Computador jogou PAPEL\nJogador jogou PEDRA\n\nVoce perdeu.")
elif pc == tesoura and escolha == pedra:
    print("Computador jogou TESOURA\nJogador jogou PEDRA\n\nVoce ganhou!")
elif pc == tesoura and escolha == papel:
    print("Computador jogou TESOURA\nJogador jogou PAPEL\n\nVoce perdeu.")
else:
    if escolha == 1:
        empate = "Pedra"
        print("Ambos escolheram {}\n\nEmpate!".format(empate))
    elif escolha == 2:
        empate = "Papel"
        print("Ambos escolheram {}\n\nEmpate!".format(empate))
    elif escolha == 3:
        empate = "Tesoura"
        print("Ambos escolheram {}\n\nEmpate!".format(empate))
    else:
        print("Escolha invalida")
