# GalinaceosApi

API Flask com endpoint `/galinaceos`, filtros por query params e persistência no PostgreSQL usando Docker.

## Filtros exigidos

- `SIST_CRIA`
- `NIV_TERR`
- `COD_TERR`
- `NOM_TERR`
- `CL_GAL`

## Como executar

### 1. Subir o PostgreSQL

```bash
docker compose up -d
```

### 2. Criar ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

No Windows:

```bash
venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Importar o CSV para o banco

```bash
python seed/importar_csv.py
```

### 5. Rodar a API

```bash
python app.py
```

A API ficará disponível em:

```text
http://localhost:5000
```

## Exemplos de uso

Listar todos:

```text
http://localhost:5000/galinaceos
```

Filtrar por território:

```text
http://localhost:5000/galinaceos?NOM_TERR=Paraíba
```

Filtrar por classe:

```text
http://localhost:5000/galinaceos?CL_GAL=1
```

Filtrar por múltiplos campos:

```text
http://localhost:5000/galinaceos?NIV_TERR=UF&COD_TERR=25
```

Buscar por ID:

```text
http://localhost:5000/galinaceos/1
```

## Arquitetura

O projeto segue a estrutura em camadas usada em aula:

```text
Controller -> Service -> Repository -> Model -> Database
```

- **Controller:** recebe as requisições HTTP.
- **Service:** concentra a regra de negócio.
- **Repository:** consulta o banco.
- **Model:** representa a tabela.
- **Database:** configura a conexão com PostgreSQL.
