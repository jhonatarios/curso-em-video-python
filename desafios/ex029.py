km = int(input("Voce esta numa rodovia e passou em um radar de 80Km/h, a quantos Km/h voce estava? "))
if km <= 80:
    print("Cara que sorte, o radar era de 80Km/h, voce nao foi multado!")
else:
    multa = (km - 80) * 7
    print("Voce foi multado em R$ {:.2f}".format(multa))