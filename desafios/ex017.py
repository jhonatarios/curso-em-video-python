from math import hypot
oposto = int(input("Digite o comprimento do cateto oposto: "))
adjacente = int(input("Digite o comprimento do cateto adjacente: "))
print("\nO comprimento da hipotenusa é de {:.2f}".format(hypot(oposto, adjacente)))