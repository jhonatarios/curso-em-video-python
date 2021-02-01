salario = int(input("Digite o salario para um aumento: "))

if salario >= 1250:
    n_salario = salario * 1.1
    print("Seu salario agora é de R$ {:.2f}".format(n_salario))
else:
    n_salario = salario * 1.15
    print("Seu salario agora é de R$ {:.2f}".format(n_salario))