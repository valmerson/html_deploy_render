from flask import Flask, request
import requests 
import os

app = Flask(__name__)
BOT_TOKEN=os.environ["TELEGRAM_BOT_TOKEN"]

@app.route("/")
def index():
  return "Olá, </b>Tudo bem</b>?"

@app.route("/teste")
def teste():
  return "Esse é apenas um </b>teste</b> com o qual checamos a implementação de alterações no site" 

@app.route("/telegram", methods=['POST'])
def telegram_update():
  update=request.json
  url_envio_mensagem=f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
  chat_id=update["mensage"] ["chat"] ["id"]
  mensagem={"chat_id": chat_id, "text": "mensagem <b>recebida</b>", "parse_mode":"HTML"}
  requests.post(url_envio_mensagem, data=mensagem)
  return "ok"

