numero = int(input("Digite um numero para converter: "))
escolha = int(input("Escolha para qual deseja converter:\n1-Binario\n2-Octal\n3-Hexadecimal\n"))
if escolha == 1:
    print(bin(numero))
elif escolha == 2:
    print(oct(numero))
elif escolha == 3:
    print(hex(numero))
else:
    print("Voce nao escolheu nenhuma das opcoes.")
