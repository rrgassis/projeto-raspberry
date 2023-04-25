from datetime import datetime

from flask import Flask, render_template
from flask.globals import request

from bater_ponto import dia_hora, validacao
from funcoes import edv_cadastrado, comprovante, add_user

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("homepage.html")
# tela de bater o ponto {


@app.route("/ponto", methods=["POST"])
def ponto():
    edv = request.form["edv"]
    cadastro_usu, nome = edv_cadastrado(edv)
    if not cadastro_usu:
        return render_template("tela4.html")
    else:
        dia, hora = dia_hora()
        validacao(edv, nome)
        comprovante(nome, edv, dia, hora)
        return render_template("tela2.html", nome=nome)


@app.route("/cadastro", methods=["POST", "GET"])
def cadastro():
    return render_template("tela3.html")

# }

# tela2 {


@app.route("/voltar_inicial", methods=["POST", "GET"])
def voltar_inicial():
    return render_template("homepage.html")

# }

# tela3 cadastro {


@app.route("/cadastrar", methods=["POST", "GET"])
def cadastrar():
    nome = request.form["nome"]
    telefone = request.form["telefone"]
    edv = request.form["edv"]
    add_user(nome, telefone, edv)
    return render_template("homepage.html")
# }

# tela4 cadastro"""

if __name__ == "__main__":
    app.run(debug=True)