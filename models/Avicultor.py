from marshmallow import Schema, fields, validate
from helpers.database import db

class Avicultor(db.Model):
    __tablename__ = "avicultores"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    nome = db.Column(
        db.String,
        nullable=False
    )

    nascimento = db.Column(
        db.Date,
        nullable=False
    )

    cpf = db.Column(
        db.String,
        nullable=False
    )

    caf = db.Column(
        db.String,
        nullable=False
    )

    def toDict(self):

        return {
            "id": self.id,
            "nome": self.nome,
            "nascimento": self.nascimento.isoformat() if self.nascimento else None,
            "cpf": self.cpf,
            "caf": self.caf
        }

class AvicultorSchema(Schema):

    nome = fields.Str(
        required=True,
        error_messages={
            "required": "Adicione um nome."
        }
    )

    nascimento = fields.Date(
        required=True
    )

    cpf = fields.Str(
        required=True,
        validate=validate.Length(
            max=11,
            error="Tamanho do CPF inválido."
        )
    )

    caf = fields.Str(
        required=True
    )