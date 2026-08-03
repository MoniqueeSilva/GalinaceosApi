from datetime import datetime

from models.Avicultor import Avicultor
from repositories.AvicultorRepository import AvicultorRepository
from helpers.logger import logger


class AvicultorService:

    def __init__(self):
        self.repository = AvicultorRepository()


    def getAll(self, filtros=None):

        logger.info("Buscando avicultores")

        return self.repository.getAll(filtros)



    def getById(self, id):

        logger.info(
            f"Buscando avicultor pelo id: {id}"
        )

        return self.repository.getById(id)



    def create(self, dados):

        logger.info(
            "Criando novo avicultor"
        )

        avicultor = Avicultor(
            nome=dados.get("nome"),
            nascimento=datetime.strptime(
                dados.get("nascimento"),
                "%Y-%m-%d"
            ),
            cpf=dados.get("cpf"),
            caf=dados.get("caf")
        )


        return self.repository.save(
            avicultor
        )



    def update(self, id, dados):

        logger.info(
            f"Atualizando avicultor: {id}"
        )


        avicultor = self.repository.getById(id)


        if avicultor is None:
            return None



        if dados.get("nome"):

            avicultor.nome = dados.get("nome")



        if dados.get("nascimento"):

            avicultor.nascimento = datetime.strptime(
                dados.get("nascimento"),
                "%Y-%m-%d"
            )



        if dados.get("cpf"):

            avicultor.cpf = dados.get("cpf")



        if dados.get("caf"):

            avicultor.caf = dados.get("caf")



        return self.repository.update(
            avicultor
        )



    def delete(self, id):

        logger.info(
            f"Removendo avicultor: {id}"
        )


        avicultor = self.repository.getById(id)


        if avicultor is None:
            return False



        self.repository.delete(
            avicultor
        )


        return True