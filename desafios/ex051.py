pa = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
for c in range(1, 11): 
    print(f"{pa}", end=" → ")
    pa += razao
print("FIM")