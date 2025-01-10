"""

var
if
for
def

list
set
dict

class

"""
from modelo import Aluno, AlunoClass

al = Aluno(1, "João", "joao@atec.pt", 19 )
print(al.nome)
print(al)

alc = AlunoClass(1,"João", "joao@atec.pt", 19 )
print(alc.nome)
print(alc)


print("----------")


print(al.idade)
al.novoIdade(30)
print(al.idade)

print("---")

print(alc.idade)
alc.novoIdade(30)
print(alc.idade)

print("----------")

al2 = Aluno(1, "João", "joao@atec.pt", 19 )
alc2 = AlunoClass(1, "João", "joao@atec.pt", 19 )


print("---")
print(al == al2) # data class
print(alc == alc2) # data class

print("---")
print(al == alc) #

print("---")
print(int("10"))

print("---")

print(int(al))

print("--dataclass--")
al3 = al.__copy__()
al3.nome = "Sem nome"

print(al3.nome)
print(al.nome)

print(al is al3)

print("---")


print("-- Class --")
alc3 = alc
alc3.nome = "Sem nome"

print(alc3.nome)
print(alc.nome)

print(alc is alc3)

print("---")

## Crie uma Agenda de contactos
#Funcionalidades:
# Adiconar contacto
# listar contactos
# Pesquisar contacto (por nome)
# não adicionar conctatos duplicados
#
