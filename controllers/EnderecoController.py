from flask import request
from flask_restful import Resource

from services.EnderecoService import EnderecoService
from helpers.logger import logger



class EnderecosController(Resource):


    def get(self):

        logger.info(
            "Listando endereços"
        )


        filtros = {

            "cidade": request.args.get("cidade"),

            "estado": request.args.get("estado")

        }


        enderecos = EnderecoService().getAll(
            filtros
        )


        return [

            e.toDict()

            for e in enderecos

        ], 200




    def post(self):

        logger.info(
            "Criando endereço"
        )


        endereco = EnderecoService().create(
            request.json
        )


        return endereco.toDict(), 201