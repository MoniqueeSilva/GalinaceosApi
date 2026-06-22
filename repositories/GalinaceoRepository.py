from models.Galinaceo import Galinaceo


class GalinaceoRepository:
    """
    Camada responsável pelo acesso ao banco de dados.
    Aqui ficam as consultas SQLAlchemy.
    """

    def __init__(self, session):
        self.session = session

    def get_all(self, filtros):
        query = self.session.query(Galinaceo)

        if filtros.get("SIST_CRIA"):
            query = query.filter(Galinaceo.sist_cria == filtros["SIST_CRIA"])

        if filtros.get("NIV_TERR"):
            query = query.filter(Galinaceo.niv_terr == filtros["NIV_TERR"])

        if filtros.get("COD_TERR"):
            query = query.filter(Galinaceo.cod_terr == filtros["COD_TERR"])

        if filtros.get("NOM_TERR"):
            query = query.filter(Galinaceo.nom_terr.ilike(f"%{filtros['NOM_TERR']}%"))

        if filtros.get("CL_GAL"):
            query = query.filter(Galinaceo.cl_gal == filtros["CL_GAL"])

        return query.order_by(Galinaceo.id).all()

    def get_by_id(self, galinaceo_id):
        return self.session.query(Galinaceo).filter(Galinaceo.id == galinaceo_id).first()
