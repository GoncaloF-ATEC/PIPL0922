from dataclasses import dataclass

MAX_FELICIDADE = 100

@dataclass
class Food:
    nome: str
    nivel: int

@dataclass
class Game:
    nome: str
    nivel: int


class MyPessoa:

    def __init__(self, nome: str, idade: int): #<- Construtor - func responsavel por "cirar" a class
        self.nome = nome
        self.idade = idade
        self.fome = 100
        self.felicidade = 0
        self.lista_comidas = []
        self.lista_jogos = []

    def comer(self, comida: Food):

        self.fome -= comida.nivel
        self.lista_comidas.append(comida)

        if self.fome < 0:
            self.fome = 0

    def jogar(self, jogo: Game):
        self.felicidade += jogo.nivel
        self.lista_jogos.append(jogo)

        if self.felicidade > MAX_FELICIDADE:
            self.felicidade = MAX_FELICIDADE

    def get_info(self) -> str:
        return f"nome:{self.nome}, fome: {self.fome}"