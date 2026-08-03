from helpers.database import db
from models.Endereco import Endereco


class EnderecoRepository:


    def getAll(self, filtros=None):

        query = Endereco.query


        if filtros:

            if filtros.get("cidade"):

                query = query.filter(
                    Endereco.cidade == filtros.get("cidade")
                )


            if filtros.get("estado"):

                query = query.filter(
                    Endereco.estado == filtros.get("estado")
                )


        return query.all()



    def save(self, endereco):

        db.session.add(endereco)

        db.session.commit()

        return endereco