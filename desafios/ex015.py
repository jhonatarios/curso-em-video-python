km = float(input("Quantos KM foram rodados? "))
dias = int(input("Quantos dias foram rodados? "))
pago = (dias * 60) + (km * 0.15)
print("O valor a ser pago é de R$ {:.2f}".format(pago))