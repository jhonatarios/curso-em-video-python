from math import hypot
oposto = float(input("Digite o comprimento do cateto oposto: "))
adjacente = float(input("Digite o comprimento do cateto adjacente: "))
print("\nO comprimento da hipotenusa é de {:.2f}".format(hypot(oposto, adjacente)))