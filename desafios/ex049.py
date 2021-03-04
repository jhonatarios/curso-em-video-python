num = int(input('Insira um numero para ver a sua tabuada: '))

for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
