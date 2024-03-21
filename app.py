from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "Olá, </b>Tudo bem</b>?"

@app.route("/teste")
def teste():
  return "Esse é apenas um </b>teste</b> com o qual checamos a implementação de alterações no site" 



