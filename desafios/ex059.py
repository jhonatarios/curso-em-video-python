escolha = 0
while not escolha == 5:
    print("Digite dois numeros\n")
    n1 = int(input("Primeiro numero: "))
    n2 = int(input("Segundo numero: "))

    escolha = int(input("\nEscolha o que deseja fazer:\n"
                        "[1] Somar\n"
                        "[2] Multiplicar\n"
                        "[3] Maior\n"
                        "[4] Novos numeros\n"
                        "[5] Sair do programa\n"))
    if escolha == 1:
        print(f"A soma de {n1} com {n2} é de {n1+n2}\n")
    if escolha == 2:
        print(f"A multiplicacao de {n1} com {n2} é de {n1*n2}\n")
    if escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"O maior numero é {maior}\n")
    if escolha == 4:
        continue
    if escolha == 5:
        break
print("Acabou")