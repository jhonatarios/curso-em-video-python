from math import sqrt, floor
import random
import emoji

num = int(input("Digite um numero para saber a raiz quadrada: "))
raiz = sqrt(num)
print("A raiz de {} é igual a {}".format(num, floor(raiz)))

rand = random.randint(1, 10)
print("\nNumero aleatorio: {}".format(rand))

print(emoji.emojize("\nPython é brabo :thumbs_up:"))

