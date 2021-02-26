valorProduto = float(input("Digite o valor de um produto: "))
condicaoPagamento = int(input("Digite a condicao de pagamento: \n1-A vista no dinheiro\n2-A vista no cartao\n3-Parcelado no cartao 2x\n4-Parcelado 3x ou mais no cartao\n"))
if condicaoPagamento == 1:
    valorFinal = (valorProduto/100)*90
    print("O valor a ser pago é de R$ {:.2f}".format(valorFinal))
elif condicaoPagamento == 2:
    valorFinal = (valorProduto/100)*95
    print("O valor a ser pago é de R$ {:.2f}".format(valorFinal))
elif condicaoPagamento == 3:
    print("O valor a ser pago é de R$ {:.2f}, em 2 parcelas de R$ {:.2f}".format(valorProduto, (valorProduto/2)))
elif condicaoPagamento == 4:
    parcelas = int(input("Digite a quantidade de parcelas: "))
    if parcelas >= 3:
        valorFinal = (valorProduto / 100) * 120
        valorParcelas = valorFinal / parcelas
        print("O valor a ser pago é de R$ {:.2f}, em {} parcelas de {}.".format(valorFinal, parcelas, valorParcelas))
    else:
        print("Quantidade de parcelas invalidas, tente novamente.")
        quit()
else:
    print("Escolha uma opcao valida.")