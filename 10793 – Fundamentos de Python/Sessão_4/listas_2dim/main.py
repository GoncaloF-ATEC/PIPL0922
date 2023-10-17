lista = [[1, 2, 3], [4, 5, 6], [7, 8 ,9]]


print(lista[0][2])
lista[0][2] = 99
print(lista[0][2])

lista.append([2, 3, 5])

print(lista)


for i in lista:
    print(i[2])


for subLita in lista:
    for elm in subLita:
        print(elm, end="\t")
    print("")



lista = [[1, 2, 3], [4, 5, 6], [7, 8 ,9]]

print("-" * 10)
contador = 0

for subLita in range(lista.__len__()):
    print(f"{subLita}: {lista[subLita]}", end="\t")
    contador += 1
    print("")

print(contador)

print("-" * 10)
contador = 0
for subLita in range(lista.__len__()):
    for elm in range(lista[subLita].__len__()):
        print(f"[{subLita}, {elm}]; {lista[subLita][elm]}", end="\t")
        contador += 1
    print()

print(contador)