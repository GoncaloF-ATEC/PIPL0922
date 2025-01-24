from flask import Flask, request, render_template

app = Flask(__name__)

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


@app.errorhandler(404)
def page_not_found(e):
    return f'<h1>Erro  404</h1>'



if __name__ == '__main__':
    app.run(debug=True)
