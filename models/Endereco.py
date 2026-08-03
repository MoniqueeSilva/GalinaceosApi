from helpers.database import db
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Endereco(db.Model):
    __tablename__ = "enderecos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    logradouro: Mapped[str] = mapped_column(db.String, nullable=False)
    cep: Mapped[str] = mapped_column(db.String, nullable=False)
    numero: Mapped[str] = mapped_column(db.String, nullable=False)
    avicultor_id: Mapped[int] = mapped_column(db.ForeignKey("avicultores.id"), nullable=False)
    avicultor: Mapped["Avicultor"] = relationship("Avicultor",back_populates="enderecos")

    def toDict(self):
        return {
            "id": self.id,
            "logradouro": self.logradouro,
            "cep": self.cep,
            "numero": self.numero,
            "avicultor_id": self.avicultor_id
        }