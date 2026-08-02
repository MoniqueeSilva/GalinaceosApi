from flask import Flask
from flask_restful import Api # facilita a criação de APIs REST
from dotenv import load_dotenv # carregar variáveis de ambiente que estão armazenadas em um arquivo .env

from helpers.cors import cors # permite que o seu backend aceite requisições feitas por sites hospedados em domínios/portas diferentes

load_dotenv()

app = Flask(__name__)
cors.init_app(app)

api = Api(app) 