from helpers.database import db
from sqlalchemy.orm import Mapped, mapped_column


class Endereco(db.Model):
    __tablename__ = "enderecos"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    logradouro: Mapped[str] = mapped_column(
        nullable=False
    )

    numero: Mapped[str] = mapped_column(
        nullable=False
    )


    bairro: Mapped[str] = mapped_column(
        nullable=True
    )


    cidade: Mapped[str] = mapped_column(
        nullable=False
    )


    estado: Mapped[str] = mapped_column(
        nullable=False
    )


    def toDict(self):

        return {
            "id": self.id,
            "logradouro": self.logradouro,
            "numero": self.numero,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "estado": self.estado
        }