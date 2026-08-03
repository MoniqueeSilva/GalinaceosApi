from helpers.database import db
from models.Avicola import Avicola

class AvicolaRepository:
    def getAll(self, filtros=None):
        query = Avicola.query

        if filtros:
            if filtros.get("endereco"):
                query = query.filter(Avicola.endereco == filtros.get("endereco"))

            if filtros.get("territorio"):
                query = query.filter(Avicola.territorio == filtros.get("territorio"))

        return query.all()

    def getById(self, id):
        return Avicola.query.get(id)

    def save(self, avicola):
        db.session.add(avicola)
        db.session.commit()
        return avicola

    def update(self, avicola):
        db.session.commit()
        return avicola

    def delete(self, avicola):
        db.session.delete(avicola)
        db.session.commit()