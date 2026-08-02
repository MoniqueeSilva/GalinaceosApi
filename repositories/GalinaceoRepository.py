from models.Galinaceo import Galinaceo
from helpers.logger import logger

class GalinaceoRepository:
    def getAll(self, filtros=None):
        logger.info("Buscando galináceos")
        query = Galinaceo.query

        if filtros:
            if filtros.get("SIST_CRIA"):
                query = query.filter(
                    Galinaceo.sist_cria == filtros.get("SIST_CRIA")
                )

            if filtros.get("NIV_TERR"):
                query = query.filter(
                    Galinaceo.niv_terr == filtros.get("NIV_TERR")
                )

            if filtros.get("COD_TERR"):
                query = query.filter(
                    Galinaceo.cod_terr == filtros.get("COD_TERR")
                )

            if filtros.get("NOM_TERR"):
                query = query.filter(
                    Galinaceo.nom_terr.ilike(
                        f"%{filtros.get('NOM_TERR')}%"
                    )
                )

            if filtros.get("CL_GAL"):
                query = query.filter(
                    Galinaceo.cl_gal == filtros.get("CL_GAL")
                )

        return query.order_by(
            Galinaceo.id
        ).all()

    def getByIdGalinaceo(self, id):
        logger.info("Buscando galináceo por id")
        return Galinaceo.query.get(id)