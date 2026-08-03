from flask import request
from flask_restful import Resource

from services.EnderecoService import EnderecoService
from helpers.logger import logger

class EnderecosController(Resource):
    def get(self):
        logger.info("Listando endereços")
        filtros = {
            "logradouro": request.args.get("logradouro"),
            "cep": request.args.get("cep"),
            "avicultor_id": request.args.get("avicultor_id")
        }

        enderecos = EnderecoService().getAll(filtros)

        return [e.toDict() for e in enderecos], 200

    def post(self):
        logger.info("Criando endereço")
        endereco = EnderecoService().create(request.json)

        return endereco.toDict(), 201