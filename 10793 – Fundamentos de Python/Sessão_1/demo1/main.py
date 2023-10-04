#valor inteiro
i = 10

#valor texto
txt = "Valor"

#valor decimal
d = 10.5

#valor bool (T ou F)
b = True

#int + int
soma = i + 23
print(soma)

""" 
#int + str - Erro
soma2 = i + " nome"
print(soma2)
"""


#decimal + int
soma3 = d + 23
print(soma3)


#bool(T) + int
soma4 = b + 23
print(soma4)

#bool(F) + int
b = False
soma5 = b + 23
print(soma5)


inData = int(input("valor 1: "))
inData2 = int(input("valor 2: "))

print("inData", inData)
print(f"inData2 {inData2}")

soma6 = inData + inData2

print(f"soma {soma6}")


if soma6 == 10:
    print("soma = 10")
else:
    print("outro valor")
    print("outro valor 2")

print("fora do else")

"""

10 / 2  = 5


10 / 3 =  3  sobra  1

(3 *  3) + 1 = 10

10 / 4 = 2 sobra 2

4 * 2 = 8 

10 - 8 = 2 


10 / 3 = 3

10 % 3 = 1


"""

if soma6 % 2 == 0:
    print(f"{soma6} é par")
else:
    print(f"{soma6} é ímapar")


i.__ceil__()