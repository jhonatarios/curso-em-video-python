pa = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
count = 1
termos = 10
totalTermos = 0

while termos != 0:
    totalTermos += termos
    while count <= totalTermos:
        print(f"{pa}", end=" → ")
        pa += razao
        count += 1
    termos = int(input("\nQuantos termos voce deseja ver a mais? "))

print("FIM")
