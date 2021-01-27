nome = str(input("Digite o seu nome completo: ")).strip()
pnome = nome.split()
unome = pnome[-1]
print("Primeiro nome: {}\nUltimo nome: {}".format(pnome[0], unome))
