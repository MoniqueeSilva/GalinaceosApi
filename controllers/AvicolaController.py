from flask import request
from flask_restful import Resource

from services.AvicolaService import AvicolaService
from helpers.logger import logger

class AvicolasController(Resource):
    def get(self):
        logger.info("Listando avícolas")
        filtros = {
            "endereco": request.args.get("endereco"),
            "territorio": request.args.get("territorio")
        }

        avicolas = AvicolaService().getAll(filtros)
        return [a.toDict() for a in avicolas], 200


    def post(self):
        logger.info("Cadastrando avícola")
        dados = request.json
        avicola = AvicolaService().create(
            dados
        )

        return avicola.toDict(), 201

class AvicolaController(Resource):
    def get(self, id):
        logger.info(
            f"Buscando avícola por id: {id}"
        )

        avicola = AvicolaService().getById(id)

        if avicola is None:
            return {"mensagem": "Avícola não encontrada"}, 404
        return avicola.toDict(), 200

    def put(self, id):
        logger.info(f"Atualizando avícola: {id}")
        dados = request.json
        avicola = AvicolaService().update(id,dados)

        if avicola is None:
            return {"mensagem": "Avícola não encontrada"}, 404
        return avicola.toDict(), 200

    def delete(self, id):
        logger.info(f"Removendo avícola: {id}")
        removido = AvicolaService().delete(id)

        if not removido:
            return {"mensagem": "Avícola não encontrada"}, 404

        return {"mensagem": "Avícola removida com sucesso"}, 200