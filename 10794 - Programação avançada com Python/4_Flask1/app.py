from flask import Flask, request, render_template, redirect
from Aluno import Aluno
import sqlite3


alunos = [
    Aluno("João", 101),
    Aluno("Maria", 102),
    Aluno("Pedro", 103),
    Aluno("Ana", 104),
    Aluno("Rita", 105),
]

app = Flask(__name__)


@app.route('/setup')
def setup():
    # criar a base dados
    conn = sqlite3.connect('alunos.db')
    cursor = conn.cursor()
    # criar tabelas

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (nome VARCHAR, idade INTEGER);
    """)

    conn.commit()

    # adicionar dados

    cursor.execute("""
    INSERT INTO alunos (nome, idade) VALUES 
            ('João', 20),
            ('Maria', 22),
            ('Pedro', 19),
            ('Ana', 21),
            ('Rita', 23);
    """)

    conn.commit()

    return redirect("/", code=302)


@app.route('/')
def hello_world():
    return render_template('template_base.html')

@app.route('/pag2/')
def pag2():
    return 'Bem vindo desconhecido!'

@app.route('/pag2/<nome>')
def pag2_info(nome:str):
    return f'Bem vindo {nome}!'


@app.route('/pag2/<nome>/notas')
def pag_notas(nome:str):
    return f'<h2>Lista de notas do {nome}!</h2>'


"""
?nome=goncalo
"""
@app.route('/pag3/')
def pag3():
    return request.query_string

"""
?nome=goncalo&ano=2025
"""
@app.route('/pag4/')
def pag4():
    nome = request.args.get('nome')
    ano = request.args.get('ano')
    return f"<h1>Ola mundo, {nome}, em {ano}</h1>"

@app.route("/main")
def main():
    return render_template("index.html", nome= "Gonçalo")


@app.route("/home")
def index():
    return render_template("mainPage.html", nome="Gonçalo")


@app.route("/info")
def infos():
    return render_template("pag2.html")





@app.route('/add')
def addAluno():
    return render_template("addPage.html", nome="Adicionar Aluno")


#@app.route('/add', methods=['POST'])
@app.post("/add")
def addResp():
    conn = sqlite3.connect('alunos.db')
    cursor = conn.cursor()


    nome = request.form.get('nome')
    num = int(request.form.get('numero'))
    #CREATE TABLE IF NOT EXISTS alunos (nome VARCHAR, idade INTEGER);

    cursor.execute(f"""
    insert into alunos (nome, idade) values 
    ('{nome}', {num})""")

    conn.commit()
    conn.close()
    alunos.append(Aluno(nome, num))
    return redirect("/list")



@app.route('/list')
def listaAlunos():
    return render_template("lista.html", listaAlunos = alunos)



@app.route('/demoSQL')
def demoSQL():
    conn = sqlite3.connect('alunos.db')
    cursor = conn.cursor()

    myData = cursor.execute("SELECT * FROM alunos")

    data = myData.fetchmany(2)
    data2 = myData.fetchone()

    conn.close()

    return [data, data2]

@app.route('/demoSQL2')
def demoSQL2():
    conn = sqlite3.connect('alunos.db')
    cursor = conn.cursor()

    myData = cursor.execute("SELECT * FROM alunos")

    data = myData.fetchall()

    conn.close()

    return data

@app.route('/demoSQL3')
def demoSQL3():
    conn = sqlite3.connect('alunos.db')
    cursor = conn.cursor()

    myData = cursor.execute("SELECT * FROM alunos")

    data = myData.fetchone()

    aluno = Aluno(data[0], data[1])

    conn.close()

    return str(aluno)




@app.errorhandler(404)
def page_not_found(e):
    return f'<h1>Erro  404</h1>'


@app.errorhandler(405)
def page_not_found(e):
    return f'<h1>Erro  405</h1>'


if __name__ == '__main__':
    app.run(debug=True)
