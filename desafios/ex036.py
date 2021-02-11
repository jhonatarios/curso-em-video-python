valorCasa = float(input("Qual o valor da casa? "))
valorSalario = float(input("Qual o valor do seu salario? "))
qtdParcelas = int(input("Em quantos anos deseja parcelar a casa? "))

valorParcela = valorCasa / (qtdParcelas * 12)

if valorParcela <= ((valorSalario / 100)*30):
    print("Parabens o emprestimo foi aprovado!\nA sua parcela é no valor de R$ {:.2f}".format(valorParcela))
else:
    print("O emprestimo foi negado :c")