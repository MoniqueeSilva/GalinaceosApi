from helpers.application import app, api
from helpers.database import db

from models.Galinaceo import Galinaceo
from models.Avicultor import Avicultor
from models.Avicola import Avicola

from controllers.GalinaceoController import (
    GalinaceosController,
    GalinaceoController
)

from controllers.AvicultorController import (
    AvicultoresController,
    AvicultorController
)

from controllers.AvicolaController import (
    AvicolasController,
    AvicolaController
)

@app.get("/")
def index():
    return {"versao": "1.0.0", "projeto": "GalinaceosApi"}, 200


@app.get("/health")
def healthCheck():
    return {"online": "true"}, 200

api.add_resource(GalinaceosController, "/galinaceos")
api.add_resource(GalinaceoController, "/galinaceos/<int:id>")

api.add_resource(AvicultoresController, "/avicultores")
api.add_resource(AvicultorController, "/avicultores/<int:id>")

api.add_resource(AvicolasController, "/avicola")
api.add_resource(AvicolaController, "/avicola/<int:id>")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
