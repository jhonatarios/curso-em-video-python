from datetime import date
num = int(input("Digite o ano para saber se é bissexto, ou digite 0 para analisar o ano atual: "))
if num == 0:
    num = date.today().year
if num % 4 == 0 and num % 100 !=0 or num % 400 == 0:
    print("É bissexto!")
else:
    print("Nao é bissexto!")