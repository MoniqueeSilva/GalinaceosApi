from models.Galpao import Galpao
from repositories.GalpaoRepository import GalpaoRepository
from helpers.logger import logger

class GalpaoService:
    def __init__(self):
        self.repository = GalpaoRepository()

    def getAll(self, filtros=None):
        logger.info("Listando galpões")
        return self.repository.getAll(filtros)

    def getById(self, id):
        logger.info(f"Buscando galpão {id}")
        return self.repository.getById(id)

    def create(self, dados):
        logger.info("Criando galpão")
        galpao = Galpao(
            nome=dados.get("nome"),
            capacidade=dados.get("capacidade"),
            tipo=dados.get("tipo"),
        )

        return self.repository.save(galpao)