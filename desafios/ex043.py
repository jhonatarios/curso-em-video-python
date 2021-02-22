peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
imc = peso / (altura * altura)
if imc < 18.5:
    print("Abaixo do peso.\nIMC: {:.1f}".format(imc))
elif imc < 25:
    print("Peso ideal.\nIMC: {:.1f}".format(imc))
elif imc < 30:
    print("Sobrepeso.\nIMC: {:.1f}".format(imc))
elif imc < 40:
    print("Obesidade.\nIMC: {:.1f}".format(imc))
else:
    print("Obesidade morbida.\nIMC: {:.1f}".format(imc))