from flask import request
from flask_restful import Resource

from services.AvicultorService import AvicultorService
from helpers.logger import logger


class AvicultoresController(Resource):

    def get(self):

        logger.info("Listando avicultores")

        filtros = {
            "nome": request.args.get("nome"),
            "cpf": request.args.get("cpf"),
            "caf": request.args.get("caf")
        }

        avicultores = AvicultorService().getAll(filtros)

        return [
            avicultor.toDict()
            for avicultor in avicultores
        ], 200


    def post(self):

        logger.info("Cadastrando avicultor")

        dados = request.json

        avicultor = AvicultorService().create(dados)

        return avicultor.toDict(), 201



    def put(self):

        logger.info("Atualizando avicultor")

        dados = request.json

        id = dados.get("id")

        avicultor = AvicultorService().update(
            id,
            dados
        )

        if avicultor is None:
            return {
                "mensagem": "Avicultor não encontrado"
            }, 404


        return avicultor.toDict(), 200



    def delete(self):

        logger.info("Removendo avicultor")

        id = request.args.get("id")

        removido = AvicultorService().delete(
            id
        )

        if not removido:
            return {
                "mensagem": "Avicultor não encontrado"
            }, 404


        return {
            "mensagem": "Avicultor removido com sucesso"
        }, 200




class AvicultorController(Resource):

    def get(self, id):

        logger.info(
            f"Listando avicultor pelo id: {id}"
        )

        avicultor = AvicultorService().getById(id)

        if avicultor is None:
            return {
                "mensagem": "O registro não foi encontrado"
            }, 404


        return avicultor.toDict(), 200