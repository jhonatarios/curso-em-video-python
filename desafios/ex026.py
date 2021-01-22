frase = input("Digite uma frase: ")
print("A letra A aparece: {} vezes, na primeira vez na posicao {}, "
      "e na ultima vez na posicao {}".
      format(frase.lower().count("a"), frase.lower().find("a"), frase.lower().rfind("a")))
