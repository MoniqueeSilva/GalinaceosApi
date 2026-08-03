from models.Avicultor import Avicultor
from helpers.database import db
from helpers.logger import logger

class AvicultorRepository:
    def getAll(self, filtros=None):
        logger.info("Buscando avicultores")
        query = Avicultor.query

        if filtros:
            if filtros.get("nome"):
                query = query.filter(
                    Avicultor.nome.ilike(f"%{filtros.get('nome')}%")
                )

            if filtros.get("cpf"):
                query = query.filter(
                    Avicultor.cpf == filtros.get("cpf")
                )

            if filtros.get("caf"):
                query = query.filter(
                    Avicultor.caf == filtros.get("caf")
                )

        return query.order_by(
            Avicultor.id
        ).all()

    def getById(self, id):
        return Avicultor.query.get(id)

    def save(self, avicultor):
        db.session.add(avicultor)
        db.session.commit()
        return avicultor

    def update(self, avicultor):
        db.session.commit()
        return avicultor

    def delete(self, avicultor):
        db.session.delete(avicultor)
        db.session.commit()