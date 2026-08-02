from helpers.application import app, api
from helpers.database import db

from controllers.GalinaceoController import (
    GalinaceosController,
    GalinaceoController
)


@app.get("/")
def index():
    return {"versao": "1.0.0", "projeto": "GalinaceosApi"}, 200


@app.get("/health")
def healthCheck():
    return {"online": "true"}, 200

api.add_resource(GalinaceosController, "/galinaceos")
api.add_resource(GalinaceoController, "/galinaceos/<int:id>")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
