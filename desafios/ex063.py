n = int(input("Digite um numero inteiro: "))
c = 1
t1 = 0
t2 = 1
t3 = 0
print(F"{t1} → {t2} → ", end='')

while c <= n:
    t3 = t1 + t2
    print(f"{t3} → ", end='')
    t1 = t2
    t2 = t3
    c += 1
print("FIM")
