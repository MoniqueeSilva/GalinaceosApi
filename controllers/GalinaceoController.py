from flask import Blueprint, jsonify, request
from services.GalinaceoService import GalinaceoService

galinaceo_bp = Blueprint("galinaceo", __name__, url_prefix="/galinaceos")


@galinaceo_bp.get("/")
def get_galinaceos():
    """
    Lista todos os registros de galináceos.
    Também aceita filtros pela URL:
    /galinaceos?SIST_CRIA=...&NIV_TERR=...&COD_TERR=...&NOM_TERR=...&CL_GAL=...
    """

    filtros = {
        "SIST_CRIA": request.args.get("SIST_CRIA"),
        "NIV_TERR": request.args.get("NIV_TERR"),
        "COD_TERR": request.args.get("COD_TERR"),
        "NOM_TERR": request.args.get("NOM_TERR"),
        "CL_GAL": request.args.get("CL_GAL"),
    }

    resultado = GalinaceoService().get_all(filtros)

    return jsonify({
        "total": len(resultado),
        "dados": resultado
    }), 200


@galinaceo_bp.get("/<int:galinaceo_id>")
def get_galinaceo_by_id(galinaceo_id):
    """Busca um registro pelo ID."""

    resultado = GalinaceoService().get_by_id(galinaceo_id)

    if resultado is None:
        return jsonify({"mensagem": "Registro não encontrado"}), 404

    return jsonify(resultado), 200
