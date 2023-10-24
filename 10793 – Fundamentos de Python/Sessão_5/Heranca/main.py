from classes import *

gato1 = Gato(4, "ze", "preto", Class.Mamiferos, 7)
gato2 = Gato(4, "Maria", "amarelo", Class.Aves, 9)

print(gato1)

print(gato1 == gato2)


print(gato1 + gato2)


pi = Piriquito(4, "ze", "preto", Class.Mamiferos, 7)

print(pi)

print(type(pi))
print(type(pi).__name__)
print(pi.__class__.__name__)