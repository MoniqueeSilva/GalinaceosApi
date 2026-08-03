from helpers.database import db
from sqlalchemy.orm import Mapped, mapped_column

class Avicola(db.Model):
    __tablename__ = "avicola"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    endereco: Mapped[str] = mapped_column(nullable=False)
    territorio: Mapped[str] = mapped_column(nullable=False)

    def toDict(self):
        return {
            "id": self.id,
            "endereco": self.endereco,
            "territorio": self.territorio
        }