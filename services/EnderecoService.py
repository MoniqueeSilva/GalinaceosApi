from models.Endereco import Endereco
from repositories.EnderecoRepository import EnderecoRepository
from helpers.logger import logger

class EnderecoService:
    def __init__(self):
        self.repository = EnderecoRepository()

    def getAll(self, filtros=None):
        logger.info("Listando endereços")
        return self.repository.getAll(filtros)

    def getById(self, id):
        logger.info(f"Buscando endereço pelo id {id}")
        return self.repository.getById(id)

    def create(self, dados):
        logger.info("Cadastrando endereço")
        endereco = Endereco(
            logradouro=dados.get("logradouro"),
            cep=dados.get("cep"),
            numero=dados.get("numero"),
            avicultor_id=dados.get("avicultor_id")
        )

        return self.repository.save(endereco)