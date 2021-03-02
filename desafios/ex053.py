frase = str(input("Digite uma frase: ")).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f"Junto: {junto}, Inverso: {inverso}")
if inverso == junto:
    print("É palidromo")
else:
    print("Nao é palidromo")