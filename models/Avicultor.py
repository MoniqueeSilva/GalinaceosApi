from marshmallow import Schema, fields, validate
from helpers.database import db

from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from datetime import date

class Avicultor(db.Model):
    __tablename__ = "avicultores"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(db.String, nullable=False)
    nascimento: Mapped[date] = mapped_column(db.Date, nullable=False)
    cpf: Mapped[str] = mapped_column(db.String, nullable=False)
    caf: Mapped[str] = mapped_column(db.String,nullable=False)
    enderecos: Mapped[List["Endereco"]] = relationship("Endereco", back_populates="avicultor",cascade="all, delete-orphan")


    def toDict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "nascimento": (self.nascimento.isoformat() if self.nascimento else None),
            "cpf": self.cpf,
            "caf": self.caf
        }

class AvicultorSchema(Schema):
    nome = fields.Str(required=True, error_messages={"required": "Adicione um nome."})
    nascimento = fields.Date(required=True)
    cpf = fields.Str(required=True, validate=validate.Length(max=11, error="Tamanho do CPF inválido."))
    caf = fields.Str(required=True)