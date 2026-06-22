from helpers.database import get_session
from repositories.GalinaceoRepository import GalinaceoRepository


class GalinaceoService:
    """
    Camada de regra de negócio.
    Recebe a solicitação do controller e chama o repository.
    """

    def get_all(self, filtros):
        session = get_session()
        try:
            repository = GalinaceoRepository(session)
            galinaceos = repository.get_all(filtros)
            return [item.to_dict() for item in galinaceos]
        finally:
            session.close()

    def get_by_id(self, galinaceo_id):
        session = get_session()
        try:
            repository = GalinaceoRepository(session)
            galinaceo = repository.get_by_id(galinaceo_id)

            if galinaceo is None:
                return None

            return galinaceo.to_dict()
        finally:
            session.close()
