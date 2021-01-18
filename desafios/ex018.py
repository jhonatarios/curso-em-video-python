from math import sin, cos, tan, radians

num = float(input("Digite um angulo: "))
print("Seno: {:.2f}".format(sin(radians(num))))
print("Cosseno: {:.2f}".format(cos(radians(num))))
print("Tangente: {:.2f}".format(tan(radians(num))))