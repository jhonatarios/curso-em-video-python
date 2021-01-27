frase = input("Digite uma frase: ").lower().strip()
print("A letra A aparece: {} vezes, na primeira vez na posicao {}, "
      "e na ultima vez na posicao {}".
      format(frase.count("a"), frase.find("a")+1, frase.rfind("a")+1))
