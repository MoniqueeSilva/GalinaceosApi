import psycopg2
from helpers.enviroment import enviroment
from helpers.logger import logger

DATABASE_NAME = enviroment.get("DB_NAME")
DATABASE_USER = enviroment.get("DB_USER")
DATABASE_PASS = enviroment.get("DB_PASSWORD")
DATABASE_PORT = enviroment.get("DB_PORT")
DATABASE_HOST = enviroment.get("DB_HOST")

conn = None
try:
    conn = psycopg2.connect(
        database=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASS,
        host=DATABASE_HOST,
        port=DATABASE_PORT
    )
    logger.info("Conectou ao banco de dados")

    cursor = conn.cursor()

    with open('schema.sql', mode='r') as file:
        cursor.execute(file.read())

    logger.info("Criou as tabelas")
    conn.commit()
except psycopg2.Error as e:
    logger.error(e)
finally:
    if conn:
        conn.close()
