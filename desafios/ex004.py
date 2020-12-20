algo = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(algo)}\nEle é numerico? {algo.isnumeric()}\nEle é alfabetico? {algo.isalpha()}\nEle esta em maisculo? {algo.isupper()}\nEle esta em minusculo? {algo.islower()}\nEle só tem espacos? {algo.isspace()}')

