from marshmallow import Schema, fields
from helpers.database import db

from sqlalchemy.orm import Mapped, mapped_column

class Galinaceo(db.Model):
    __tablename__ = "galinaceos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    sist_cria: Mapped[str | None] = mapped_column(db.String, nullable=True)
    niv_terr: Mapped[str | None] = mapped_column(db.String, nullable=True)
    cod_terr: Mapped[str | None] = mapped_column(db.String, nullable=True)
    nom_terr: Mapped[str | None] = mapped_column(db.String, nullable=True)
    cl_gal: Mapped[str | None] = mapped_column(db.String, nullable=True)
    nom_cl_gal: Mapped[str | None] = mapped_column(db.String, nullable=True)
    gal_total: Mapped[int | None] = mapped_column(db.BigInteger, nullable=True)

    def toDict(self):
        return {
            "id": self.id,
            "sist_cria": self.sist_cria,
            "niv_terr": self.niv_terr,
            "cod_terr": self.cod_terr,
            "nom_terr": self.nom_terr,
            "cl_gal": self.cl_gal,
            "nom_cl_gal": self.nom_cl_gal,
            "gal_total": self.gal_total
        }

class GalinaceoSchema(Schema):
    id = fields.Int(dump_only=True)
    sist_cria = fields.Str(allow_none=True)
    niv_terr = fields.Str(allow_none=True)
    cod_terr = fields.Str(allow_none=True)
    nom_terr = fields.Str(allow_none=True)
    cl_gal = fields.Str(allow_none=True)
    nom_cl_gal = fields.Str(allow_none=True)
    gal_total = fields.Int(allow_none=True)