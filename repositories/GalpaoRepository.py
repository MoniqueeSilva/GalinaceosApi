from helpers.database import db
from models.Galpao import Galpao

class GalpaoRepository:
    def getAll(self, filtros=None):
        query = Galpao.query

        if filtros:
            if filtros.get("tipo"):
                query = query.filter(Galpao.tipo == filtros.get("tipo"))

        return query.all()

    def getById(self, id):
        return Galpao.query.get(id)

    def save(self, galpao):
        db.session.add(galpao)
        db.session.commit()
        return galpao