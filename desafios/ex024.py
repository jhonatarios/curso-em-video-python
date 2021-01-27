cidade = str(input("Digite o nome de uma cidade para saber se ela comeca com SANTO: ")).strip()
div = cidade.split()
print("santo" in div[0].lower())
