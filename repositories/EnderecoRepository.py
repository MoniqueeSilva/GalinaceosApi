from helpers.database import db
from models.Endereco import Endereco

class EnderecoRepository:
    def getAll(self, filtros=None):
        query = Endereco.query

        if filtros:
            if filtros.get("cep"):
                query = query.filter(
                    Endereco.cep == filtros.get("cep")
                )

            if filtros.get("logradouro"):
                query = query.filter(
                    Endereco.logradouro.ilike(f"%{filtros.get('logradouro')}%")
                )

            if filtros.get("avicultor_id"):
                query = query.filter(
                    Endereco.avicultor_id == filtros.get("avicultor_id")
                )

        return query.all()

    def getById(self, id):
        return Endereco.query.get(id)

    def save(self, endereco):
        db.session.add(endereco)
        db.session.commit()
        return endereco