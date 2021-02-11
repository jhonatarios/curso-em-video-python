valorProduto = float(input("Digite o valor de um produto: "))
condicaoPagamento = int(input("Digite a condicao de pagamento: \n1-A vista no dinheiro\n2-A vista no cartao\n3-Parcelado no cartao 2x\n4-Parcelado 3x ou mais no cartao\n"))
if condicaoPagamento == 1:
    valorFinal = (valorProduto/100)*90
    print("O valor a ser pago é de R$ {:.2f}".format(valorFinal))
elif condicaoPagamento == 2:
    valorFinal = (valorProduto/100)*95
    print("O valor a ser pago é de R$ {:.2f}".format(valorFinal))
elif condicaoPagamento == 3:
    print("O valor a ser pago é de R$ {:.2f}".format(valorProduto))
elif condicaoPagamento == 4:
    valorFinal = (valorProduto/100)*120
    print("O valor a ser pago é de R$ {:.2f}".format(valorFinal))
else:
    print("Escolha uma opcao valida.")