distancia = int(input("Qual a distancia da viagem em Km? "))
if distancia <= 200:
    passagem = distancia * 0.50
    print("O valor da passagem vai ser de R$ {:.2f}".format(passagem))
else:
    passagem = distancia * 0.45
    print("O valor da passagem vai ser de R$ {:.2f}".format(passagem))