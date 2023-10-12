notas = [10, 13, 17, 11, 15]

print(notas)

print(notas[3])

notas.append(18)

print(notas)

print(notas.__len__())
print(len(notas))

notas.append(10)
notas.append(10)
notas.append(10)


print(notas.__len__())

# print(notas[9])


notas.remove(17) # remove um valor

print(notas)

print(notas[0])
notas.pop(0)

print(notas) # remove o conteudo de um index

print(notas[0])


notas.insert(3,20) # [13, 11, 15, 20 ,18, 10, 10, 10]
print(notas)


notas.sort()
print(notas)


soma = 0
print("-" * 10, "for list", "-" * 10)
for elm in notas:
   soma += elm

media = soma/notas.__len__()
print(media)
print(media.__round__(0))


# Peça ao utilizador notas e adicione as validas a uma lista,
# quando o utilizador adicionar -1 termine a lista e mostre o seu conteudo

# print(not True and not False)

lista_notas = []

while True:
    nota = input("nova nota: ")

    if nota.__eq__("-1"):
        break

    if not bool(nota) or not nota.isnumeric():
        continue

    nota = float(nota)

    if 0 < nota < 20:
        lista_notas.append(nota)
    else:
        print("nota invalida")

print(lista_notas)



