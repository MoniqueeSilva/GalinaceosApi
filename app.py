from helpers.application import app
from controllers.GalinaceoController import galinaceo_bp


@app.get("/")
def index():
    return {"versao": "1.0.0", "projeto": "GalinaceosApi"}, 200


@app.get("/health")
def healthCheck():
    return {"online": "true"}, 200


app.register_blueprint(galinaceo_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
