from enum import Enum

class Class(Enum):
    Anfibios = "Anfíbios"
    Aves = "Aves"
    Mamiferos = "Mamíferos"
    Peixes = "Peixes"
    Repteis = "Répteis"


class Animal:
    def __init__(self,
                 num_patas: int,
                 nome: str,
                 cor: str,
                 classsificacao: Class):
        self.nome = nome
        self.num_patas = num_patas
        self.cor = cor
        self.classsificacao = classsificacao
        self.idade = 0

    def comer(self):
        print("o animal comeu")

    def beber(self, liquido):
        print(f"o {self.__class__.__name__} chamado {self.nome} bebeu {liquido}")

    def emitir_som(self):
        print("som")

    def __str__(self):

        msg = f"""
        tipo: {self.__class__.__name__}
        nome: {self.nome}
        num_patas: {self.num_patas}
        cor: {self.cor}
        classsificacao: {self.classsificacao.value}
        idade: {self.idade}
        """
        return msg


    def __eq__(self, other):
        return self.nome == other.nome


    def __add__(self, other):
        return Animal(4,"sem nome", "azlul", Class.Mamiferos)



class Gato(Animal):
    def __init__(self,
                 num_patas: int,
                 nome: str,
                 cor: str,
                 classsificacao: Class,
                 num_vidas: int):
        self.num_vidas = num_vidas
        super().__init__(num_patas, nome, cor, classsificacao)

    def emitir_som(self):
        print("Miar")

class Piriquito(Animal):
    def __init__(self,
                 num_patas: int,
                 nome: str,
                 cor: str,
                 classsificacao: Class,
                 num_asas: int):
        self.num_asas = num_asas

        self.cor = cor
        self.classsificacao = classsificacao
        self.num_patas = num_patas
        self.nome = nome
        self.idade = 0

    def voar(self):
        print("a Voar")

    def emitir_som(self):
        print("piar")