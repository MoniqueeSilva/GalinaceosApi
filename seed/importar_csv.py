import os
import sys

import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from helpers.logger import logger

load_dotenv()

CSV_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "data", "GALINACEOS.csv")
)

COLUNAS_CSV = ['SIST_CRIA', 'NIV_TERR', 'COD_TERR', 'NOM_TERR', 'CL_GAL', 'NOM_CL_GAL', 'E_CRIA_GAL', 'E_TEM_GAL', 'E_GAL_VEND', 'E_OVOS_PROD', 'E_OVOS_VEND', 'E_SUBS', 'E_COMERC', 'E_RECEBE_ORI', 'E_ORI_GOV', 'E_ORI_PROPRIA', 'E_ORI_COOP', 'E_ORI_EMP_INT', 'E_ORI_EMP_PRIV', 'E_ORI_ONG', 'E_ORI_SIST_S', 'E_ORI_OUTRA', 'E_GAL_ENG', 'E_GAL_GALOS', 'E_GAL_POED', 'E_GAL_MATR', 'E_ASSOC_COOP', 'E_FINANC', 'E_FINANC_COOP', 'E_FINANC_INTEG', 'E_DAP', 'E_AGRIFAM', 'E_N_AGRIFAM', 'E_PRODUTOR', 'E_COOPERATIVA', 'E_SA_LDTA', 'E_CNPJ', 'GAL_TOTAL', 'GAL_ENG', 'GAL_GALOS', 'GAL_POED', 'GAL_MATR', 'GAL_VEND', 'V_GAL_VEND', 'Q_DZ_PROD', 'Q_DZ_VEND', 'V_Q_DZ_PROD', 'V_Q_DZ_VEND', 'A_TOTAL', 'A_PAST_PLANT', 'A_LAV_PERM', 'A_LAV_TEMP', 'A_APPRL', 'VTP_AGRO', 'RECT_AGRO', 'N_TRAB_TOTAL', 'N_TRAB_LACOS']
COLUNAS_BANCO = ['sist_cria', 'niv_terr', 'cod_terr', 'nom_terr', 'cl_gal', 'nom_cl_gal', 'e_cria_gal', 'e_tem_gal', 'e_gal_vend', 'e_ovos_prod', 'e_ovos_vend', 'e_subs', 'e_comerc', 'e_recebe_ori', 'e_ori_gov', 'e_ori_propria', 'e_ori_coop', 'e_ori_emp_int', 'e_ori_emp_priv', 'e_ori_ong', 'e_ori_sist_s', 'e_ori_outra', 'e_gal_eng', 'e_gal_galos', 'e_gal_poed', 'e_gal_matr', 'e_assoc_coop', 'e_financ', 'e_financ_coop', 'e_financ_integ', 'e_dap', 'e_agrifam', 'e_n_agrifam', 'e_produtor', 'e_cooperativa', 'e_sa_ldta', 'e_cnpj', 'gal_total', 'gal_eng', 'gal_galos', 'gal_poed', 'gal_matr', 'gal_vend', 'v_gal_vend', 'q_dz_prod', 'q_dz_vend', 'v_q_dz_prod', 'v_q_dz_vend', 'a_total', 'a_past_plant', 'a_lav_perm', 'a_lav_temp', 'a_apprl', 'vtp_agro', 'rect_agro', 'n_trab_total', 'n_trab_lacos']


def limpar_valor(valor):
    if pd.isna(valor):
        return None
    return str(valor).strip()


def get_conn():
    return psycopg2.connect(
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )


def importar_csv():
    df = pd.read_csv(CSV_PATH, sep=";", dtype=str)
    df = df.where(pd.notnull(df), None)

    registros = []
    for _, linha in df.iterrows():
        registros.append(tuple(limpar_valor(linha.get(col)) for col in COLUNAS_CSV))

    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM tb_galinaceos")
        total_existente = cursor.fetchone()[0]

        if total_existente > 0:
            print(f"A tabela já possui {total_existente} registros. Carga cancelada.")
            return

        sql = "INSERT INTO tb_galinaceos (sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, nom_cl_gal, e_cria_gal, e_tem_gal, e_gal_vend, e_ovos_prod, e_ovos_vend, e_subs, e_comerc, e_recebe_ori, e_ori_gov, e_ori_propria, e_ori_coop, e_ori_emp_int, e_ori_emp_priv, e_ori_ong, e_ori_sist_s, e_ori_outra, e_gal_eng, e_gal_galos, e_gal_poed, e_gal_matr, e_assoc_coop, e_financ, e_financ_coop, e_financ_integ, e_dap, e_agrifam, e_n_agrifam, e_produtor, e_cooperativa, e_sa_ldta, e_cnpj, gal_total, gal_eng, gal_galos, gal_poed, gal_matr, gal_vend, v_gal_vend, q_dz_prod, q_dz_vend, v_q_dz_prod, v_q_dz_vend, a_total, a_past_plant, a_lav_perm, a_lav_temp, a_apprl, vtp_agro, rect_agro, n_trab_total, n_trab_lacos) VALUES %s"
        execute_values(cursor, sql, registros)
        conn.commit()

        print(f"Carga concluída com sucesso. Registros importados: {len(registros)}")
    except Exception as erro:
        if conn:
            conn.rollback()
        logger.error(erro)
        print("Erro ao importar CSV:", erro)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    importar_csv()
