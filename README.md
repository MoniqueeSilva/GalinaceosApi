# GalinaceosApi

API Flask para consulta dos dados de galináceos da Embrapa.

A estrutura segue o mesmo padrão da aplicação de Avicultores da branch sqlite do professor:

- controllers
- services
- repositories
- models
- helpers

## Executar

```bash
docker-compose up -d
python3 -m venv venv
source venv/bin/activate
pip install -r requiriments.txt
cp .env.example .env
python init_db_schema.py
python seed/importar_csv.py
python app.py
```

## Endpoints

```txt
GET /galinaceos/
GET /galinaceos/<id>
```

## Filtros

```txt
GET /galinaceos/?SIST_CRIA=1-SIST_POC
GET /galinaceos/?NIV_TERR=BR
GET /galinaceos/?COD_TERR=25
GET /galinaceos/?NOM_TERR=Brasil
GET /galinaceos/?CL_GAL=1
```
