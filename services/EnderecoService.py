from models.Endereco import Endereco
from repositories.EnderecoRepository import EnderecoRepository
from helpers.logger import logger


class EnderecoService:


    def __init__(self):

        self.repository = EnderecoRepository()



    def getAll(self, filtros=None):

        logger.info(
            "Listando endereços"
        )

        return self.repository.getAll(
            filtros
        )



    def create(self, dados):

        logger.info(
            "Cadastrando endereço"
        )


        endereco = Endereco(

            logradouro=dados.get("logradouro"),

            numero=dados.get("numero"),

            bairro=dados.get("bairro"),

            cidade=dados.get("cidade"),

            estado=dados.get("estado")

        )


        return self.repository.save(
            endereco
        )