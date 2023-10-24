from enum import Enum

class classif(Enum):
    Anfibios = "Anfíbios"
    Aves = "Aves"
    Mamiferos = "Mamíferos"
    Peixes = "Peixes"
    Repteis = "Répteis"


class Animal:
    def __init__(self,
                 num_patas: int,
                 nome: str ,
                 cor: str,
                 classsificacao: classif):
        self.nome = nome
        self.num_patas = num_patas
        self.cor = cor
        self.classsificacao = classsificacao
        self.idade = 0

    def comer(self):
        print("o animal comeu")


class gato(Animal):
    def __init__(self,
                 num_patas: int,
                 nome: str,
                 cor: str,
                 classsificacao: classif,
                 num_vidas: int):
        self.num_vidas = num_vidas
        super().__init__(num_patas, nome, cor, classsificacao)


class piriquito(Animal):
    def __init__(self,
                 num_patas: int,
                 nome: str,
                 cor: str,
                 classsificacao: classif,
                 num_asas: int):
        self.num_asas = num_asas

        self.cor = cor
        self.classsificacao = classsificacao
        self.num_patas = num_patas
        self.nome = nome

    def voar(self):
        print("a Voar")