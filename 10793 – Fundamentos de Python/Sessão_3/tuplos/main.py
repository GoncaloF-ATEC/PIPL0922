lista = [1,2,3,4]

print(lista)

lista[0] = 19

print(lista)

tup = ("Joao", 12, True)

print(tup[0])
# tup[0] = "Carlos" <- erro um tuplo e imutaval

aux = list(tup)
aux[0] = "Carlos"
tup = tuple(aux)
print(tup[0])


(nome, nota, aprovado) = tup

print(nome)
print(nota)
print(aprovado)


for elm in tup:
    print(elm)


soma = tup + tup

print(soma)

print(tup.index("Carlos"))
print(tup.__contains__("Luis"))

print(tup.__contains__("Carlos"))