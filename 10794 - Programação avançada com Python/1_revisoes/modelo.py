from dataclasses import dataclass



@dataclass
class Aluno:
    id: int
    nome: str
    nome: str
    email: str
    idade: int

    def novoIdade(self, idade:int):
        self.idade = idade

    def __eq__(self, other):
        return self.id == other.id

    def __int__(self):
        return self.id

    def __copy__(self):
        return Aluno(self.id, self.nome, self.email, self.idade)



class AlunoClass:

    def __init__(self, id, nome, email, idade):
        self.id = id
        self.nome = nome
        self.email = email
        self.idade = idade


    def novoIdade(self, idade: int):
        self.idade = idade

    def __str__(self):
        return f"AlunoClass(Nome: {self.nome}, Idade: {self.idade})"