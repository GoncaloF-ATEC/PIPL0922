""""
import Pessoa

p = Pessoa.MyPessoa("Joao", 40)
"""

"""
import Pessoa as p

p = p.MyPessoa("Joao", 40)
"""

from Pessoa import MyPessoa, Food, Game

p = MyPessoa("Joao", 40)


comidas = {"Picanha": Food("Picanha", 50),
           "Chocolate": Food("Chocolate", 60),
           "Fruta": Food("Fruta", 50)
           }

jogos = {"jogo1": Game("jogo1", 50),
         "jogo2": Game("jogo2", 60),
         "jogo3": Game("jogo3", 50)
        }



print(p.nome)
print(p.idade)
print(p.fome)


p.comer(comidas["Picanha"])
p.comer(comidas["Picanha"])
p.comer(comidas["Chocolate"])

print(p.lista_comidas)

print(p.fome)


print("-" * 10)

print(p.felicidade)

p.jogar(jogos["jogo1"])
print(p.felicidade)

p2 = MyPessoa("maria", 10)

lista_pessoas = [p, p2]

print("-" * 10)
for pessoa in lista_pessoas:
   print(pessoa.get_info())
