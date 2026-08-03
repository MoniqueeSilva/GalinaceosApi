from flask import request
from flask_restful import Resource

from services.GalpaoService import GalpaoService
from helpers.logger import logger

class GalpoesController(Resource):
    def get(self):
        logger.info("Listando galpões")
        filtros = {"tipo": request.args.get("tipo")}

        galpoes = GalpaoService().getAll(filtros)

        return [g.toDict() for g in galpoes], 200

    def post(self):
        logger.info("Cadastrando galpão")
        galpao = GalpaoService().create(request.json)
        return galpao.toDict(), 201

class GalpaoController(Resource):
    def get(self, id):
        logger.info(f"Buscando galpão pelo id {id}")
        galpao = GalpaoService().getById(id)

        if galpao is None:
            return {"mensagem": "Galpão não encontrado"}, 404

        return galpao.toDict(), 200