from helpers.database import db
from sqlalchemy.orm import Mapped, mapped_column


class Galpao(db.Model):

    __tablename__ = "galpoes"


    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )


    nome: Mapped[str] = mapped_column(
        nullable=False
    )


    capacidade: Mapped[int] = mapped_column(
        nullable=True
    )


    tipo: Mapped[str] = mapped_column(
        nullable=True
    )

    def toDict(self):

        return {
            "id": self.id,
            "nome": self.nome,
            "capacidade": self.capacidade,
            "tipo": self.tipo,
        }