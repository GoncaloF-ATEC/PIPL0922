
if True:
    pass

for i in range(2):
    pass

def Ola_Mundo():
    print("Ola Mundo")


Ola_Mundo()
Ola_Mundo()


def ola_mundo2(nome: str):
    print(f"Ola Mundo, {nome}")


ola_mundo2("Gonçalo")
ola_mundo2("Joao")
ola_mundo2("Maria")


def ola_mundo3(nome: str, ano: int):
    print(f"Ola Mundo, {nome} em {ano}")


ola_mundo3("Gonçalo", 2023)
ola_mundo3("Maria", 2020)


def ola_mundo4(nome: str, ano: int):
    return f"Ola Mundo, {nome} em {ano}"

resp = ola_mundo4("nome", 21)

print(resp)
print(ola_mundo4("nome", 21))


def soma(a: int, b: int) -> int:
    return a + b

def multip(a: int, b: int) -> int:
    return a * b
def calc (a, b):
    v1 = multip(a, 2)
    v2 = multip(b, 4)

    s = soma(v1,v2)

    return s

c = calc(1,1)
print(c)




def ola_mundo5(valor1: str, valor2: str):
    print(f"valor1: {valor1}\nvalor2: {valor2}")

ola_mundo5("v1", "v2")
print("-" * 10)
ola_mundo5(valor1="v1", valor2="v2")
print("-" * 10)
ola_mundo5(valor2="v2", valor1="v1")

print("-" * 10)
print("-" * 10)
def ola_mundo6(valor1: str, valor2: str, valor3 : str):
    print(f"valor1: {valor1}\nvalor2: {valor2}\nvalor3: {valor3}")

ola_mundo6("v1", valor3="v3", valor2="v2")