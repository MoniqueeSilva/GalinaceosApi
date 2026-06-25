from flask import Blueprint, jsonify, request
from services.GalinaceoService import GalinaceoService
from helpers.logger import logger

galinaceo_bp = Blueprint("galinaceo", __name__, url_prefix="/galinaceos")


@galinaceo_bp.get("/")
def getGalinaceos():
    logger.info("Listando os registros de galináceos")
    filtros = {
        "SIST_CRIA": request.args.get("SIST_CRIA"),
        "NIV_TERR": request.args.get("NIV_TERR"),
        "COD_TERR": request.args.get("COD_TERR"),
        "NOM_TERR": request.args.get("NOM_TERR"),
        "CL_GAL": request.args.get("CL_GAL"),
    }

    galinaceos = GalinaceoService().getAll(filtros)
    return [g.toDict() for g in galinaceos], 200

@galinaceo_bp.get("/<int:id>")
def getByIdGalinaceos(id:int):
    logger.info(f"Listando galináceos pelo if: {id}")
    galinaceo = GalinaceoService().getByIdGalinaceo(id)

    if galinaceo is None:
        return {"mensagem": "O registro não foi encontrado"}, 404

    return galinaceo.toDict(), 200
