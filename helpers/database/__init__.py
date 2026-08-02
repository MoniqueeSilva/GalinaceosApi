from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from helpers.application import app
from helpers.enviroment import enviroment


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{enviroment.get('DB_USER')}:"
    f"{enviroment.get('DB_PASSWORD')}@"
    f"{enviroment.get('DB_HOST')}:"
    f"{enviroment.get('DB_PORT')}/"
    f"{enviroment.get('DB_NAME')}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)


# manter temporariamente
def get_conn():
    import psycopg2

    return psycopg2.connect(
        host=enviroment.get("DB_HOST"),
        port=enviroment.get("DB_PORT"),
        database=enviroment.get("DB_NAME"),
        user=enviroment.get("DB_USER"),
        password=enviroment.get("DB_PASSWORD")
    )