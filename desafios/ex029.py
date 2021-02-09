km = int(input("Voce esta numa rodovia e passou em um radar de 80Km/h, a quantos Km/h voce estava? "))
if km <= 80:
    print("\033[32mCara que sorte, o radar era de 80Km/h, voce nao foi multado!\033[m")
else:
    multa = (km - 80) * 7
    print("\033[31mVoce foi multado em R$ {:.2f}\033[m".format(multa))