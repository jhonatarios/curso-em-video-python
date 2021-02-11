from datetime import date
idade = int(input("Digite o seu ano de nascimento: "))
anoAtual = date.today()
tempo = anoAtual.year - idade
tempoRestante = tempo - 18
if tempo < 18:
    print("Voce ainda nao precisa se alistar, ainda falta {} ano(s).".format(tempoRestante*-1))
elif tempo == 18:
    print("Está na hora de se alistar.")
else:
    print("Já passou {} ano(s) do tempo de alistamento.".format(tempoRestante))
