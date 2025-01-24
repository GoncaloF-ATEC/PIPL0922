from fastapi import FastAPI

from modelo import Aluno

app = FastAPI()


#host/
@app.get("/")
async def root():
    return {"message": "Hello World"}

#host/alunos
@app.get("/alunos")
async def alunos():
    return {"message": " Teste Infos dos alunos"}


#/aluno?nome=Goncalo
@app.get("/alunos/")
async def aluno(nome: str):
    al = Aluno(nome=nome, idade=19)

    return al


@app.get("/alunos/{turma}")
async def alunoTurma(turma: str):
    return {"message": f"Infos do alunos de {turma}"}


@app.post("/aluno")
async def aluno(aluno: Aluno):
    return aluno