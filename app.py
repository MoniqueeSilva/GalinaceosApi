from flask import Flask, jsonify
from flask_cors import CORS

from controllers.GalinaceoController import galinaceo_bp
from helpers.database import init_db


def create_app():
    app = Flask(__name__)
    CORS(app)

    init_db()

    app.register_blueprint(galinaceo_bp)

    @app.get("/")
    def index():
        return jsonify({
            "mensagem": "API GalinaceosApi funcionando",
            "endpoints": [
                "/galinaceos",
                "/galinaceos/<id>",
                "/health"
            ]
        }), 200

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
