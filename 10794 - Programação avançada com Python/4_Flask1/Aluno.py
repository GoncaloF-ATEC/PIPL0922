from dataclasses import dataclass


@dataclass
class Aluno:
    nome: str
    numero: int

    def __init__(self, *lista):
        self.nome = lista[0]
        self.numero = lista[1]

    def __str__(self):
        return f"nome:{self.nome}, numero:{self.numero}"