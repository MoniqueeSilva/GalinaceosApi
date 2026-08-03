from models.Avicola import Avicola
from repositories.AvicolaRepository import AvicolaRepository
from helpers.logger import logger

class AvicolaService:
    def __init__(self):
        self.repository = AvicolaRepository()

    def getAll(self, filtros=None):
        logger.info("Buscando avícolas")
        return self.repository.getAll(filtros)

    def getById(self, id):
        logger.info(f"Buscando avícola pelo id: {id}")
        return self.repository.getById(id)

    def create(self, dados):
        logger.info("Criando avícola")
        avicola = Avicola(endereco=dados.get("endereco"), territorio=dados.get("territorio"))
        return self.repository.save(avicola)

    def update(self, id, dados):
        logger.info(f"Atualizando avícola: {id}")
        avicola = self.repository.getById(id)

        if avicola is None:
            return None

        if dados.get("endereco"):
            avicola.endereco = dados.get("endereco")

        if dados.get("territorio"):
            avicola.territorio = dados.get("territorio")

        return self.repository.update(avicola)

    def delete(self, id):
        logger.info(f"Removendo avícola: {id}")
        avicola = self.repository.getById(id)

        if avicola is None:
            return False

        self.repository.delete(
            avicola
        )

        return True