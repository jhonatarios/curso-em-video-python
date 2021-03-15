"""pa = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
for c in range(1, 11):
    print(f"{pa}", end=" → ")
    pa += razao
print("FIM")"""

pa = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
count = 1

while count <= 10:
    print(f"{pa}", end=" → ")
    pa += razao
    count +=1
print("FIM")
