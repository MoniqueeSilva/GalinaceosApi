from helpers.logger import logger
from repositories.GalinaceoRepository import GalinaceoRepository

class GalinaceoService:
    def __init__(self):
        self.galinaceoRepository = GalinaceoRepository()

    def getAll(self, filtros):
        galinaceos = self.galinaceoRepository.getAll(filtros)
        logger.info(f"Retornando {len(galinaceos)} registros de galináceos"
        )

        return galinaceos

    def getByIdGalinaceo(self, id):
        galinaceo = self.galinaceoRepository.getByIdGalinaceo(id)
        logger.info("Lendo informações do resultado da consulta ao banco")

        return galinaceo