nome = str(input("Digite o seu nome completo: ")).strip()
pnome = nome.split()
unome = pnome[-1]
print("\033[7;37;40mPrimeiro nome: {}\033[m\n\033[7;37;40mUltimo nome: {}\033[m".format(pnome[0], unome))
