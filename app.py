from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "Olá, </b>Tudo bem</b>?"

@app.route("/teste")
def teste():
  return "Essa Página é um <b>teste</b>"