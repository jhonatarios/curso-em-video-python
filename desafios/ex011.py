largura = float(input("Qual a largura da parede em metros? "))
altura = float(input("Qual a altura da parede em metros? "))
area = largura * altura
print("\nSua parede tem dimensao de {:.2f} x {:.2f} e sua area é de {:.2f}m².\nSerao necessarios {:.2f} litros de tinta para pintar a parede.\n(Utilizando 1 litro de tinta para cada 2m².)".format(largura, altura, area, area/2))
