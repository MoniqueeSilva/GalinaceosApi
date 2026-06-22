import os
import sys

import pandas as pd

# Permite executar este arquivo de dentro da pasta seed/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from helpers.database import init_db, get_session
from models.Galinaceo import Galinaceo


CSV_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "data", "GALINACEOS.csv")
)


def limpar_valor(valor):
    """Converte NaN para None e transforma os demais valores em texto."""
    if pd.isna(valor):
        return None
    return str(valor).strip()


def importar_csv():
    init_db()

    df = pd.read_csv(CSV_PATH, sep=";", dtype=str)
    df = df.where(pd.notnull(df), None)

    session = get_session()

    try:
        total_existente = session.query(Galinaceo).count()

        if total_existente > 0:
            print(f"A tabela já possui {total_existente} registros. Carga cancelada.")
            return

        registros = []

        for _, linha in df.iterrows():
            registro = Galinaceo(
                sist_cria=limpar_valor(linha.get("SIST_CRIA")),
                niv_terr=limpar_valor(linha.get("NIV_TERR")),
                cod_terr=limpar_valor(linha.get("COD_TERR")),
                nom_terr=limpar_valor(linha.get("NOM_TERR")),
                cl_gal=limpar_valor(linha.get("CL_GAL")),
                nom_cl_gal=limpar_valor(linha.get("NOM_CL_GAL")),
                e_cria_gal=limpar_valor(linha.get("E_CRIA_GAL")),
                e_tem_gal=limpar_valor(linha.get("E_TEM_GAL")),
                e_gal_vend=limpar_valor(linha.get("E_GAL_VEND")),
                e_ovos_prod=limpar_valor(linha.get("E_OVOS_PROD")),
                e_ovos_vend=limpar_valor(linha.get("E_OVOS_VEND")),
                e_subs=limpar_valor(linha.get("E_SUBS")),
                e_comerc=limpar_valor(linha.get("E_COMERC")),
                e_recebe_ori=limpar_valor(linha.get("E_RECEBE_ORI")),
                e_ori_gov=limpar_valor(linha.get("E_ORI_GOV")),
                e_ori_propria=limpar_valor(linha.get("E_ORI_PROPRIA")),
                e_ori_coop=limpar_valor(linha.get("E_ORI_COOP")),
                e_ori_emp_int=limpar_valor(linha.get("E_ORI_EMP_INT")),
                e_ori_emp_priv=limpar_valor(linha.get("E_ORI_EMP_PRIV")),
                e_ori_ong=limpar_valor(linha.get("E_ORI_ONG")),
                e_ori_sist_s=limpar_valor(linha.get("E_ORI_SIST_S")),
                e_ori_outra=limpar_valor(linha.get("E_ORI_OUTRA")),
                e_gal_eng=limpar_valor(linha.get("E_GAL_ENG")),
                e_gal_galos=limpar_valor(linha.get("E_GAL_GALOS")),
                e_gal_poed=limpar_valor(linha.get("E_GAL_POED")),
                e_gal_matr=limpar_valor(linha.get("E_GAL_MATR")),
                e_assoc_coop=limpar_valor(linha.get("E_ASSOC_COOP")),
                e_financ=limpar_valor(linha.get("E_FINANC")),
                e_financ_coop=limpar_valor(linha.get("E_FINANC_COOP")),
                e_financ_integ=limpar_valor(linha.get("E_FINANC_INTEG")),
                e_dap=limpar_valor(linha.get("E_DAP")),
                e_agrifam=limpar_valor(linha.get("E_AGRIFAM")),
                e_n_agrifam=limpar_valor(linha.get("E_N_AGRIFAM")),
                e_produtor=limpar_valor(linha.get("E_PRODUTOR")),
                e_cooperativa=limpar_valor(linha.get("E_COOPERATIVA")),
                e_sa_ldta=limpar_valor(linha.get("E_SA_LDTA")),
                e_cnpj=limpar_valor(linha.get("E_CNPJ")),
                gal_total=limpar_valor(linha.get("GAL_TOTAL")),
                gal_eng=limpar_valor(linha.get("GAL_ENG")),
                gal_galos=limpar_valor(linha.get("GAL_GALOS")),
                gal_poed=limpar_valor(linha.get("GAL_POED")),
                gal_matr=limpar_valor(linha.get("GAL_MATR")),
                gal_vend=limpar_valor(linha.get("GAL_VEND")),
                v_gal_vend=limpar_valor(linha.get("V_GAL_VEND")),
                q_dz_prod=limpar_valor(linha.get("Q_DZ_PROD")),
                q_dz_vend=limpar_valor(linha.get("Q_DZ_VEND")),
                v_q_dz_prod=limpar_valor(linha.get("V_Q_DZ_PROD")),
                v_q_dz_vend=limpar_valor(linha.get("V_Q_DZ_VEND")),
                a_total=limpar_valor(linha.get("A_TOTAL")),
                a_past_plant=limpar_valor(linha.get("A_PAST_PLANT")),
                a_lav_perm=limpar_valor(linha.get("A_LAV_PERM")),
                a_lav_temp=limpar_valor(linha.get("A_LAV_TEMP")),
                a_apprl=limpar_valor(linha.get("A_APPRL")),
                vtp_agro=limpar_valor(linha.get("VTP_AGRO")),
                rect_agro=limpar_valor(linha.get("RECT_AGRO")),
                n_trab_total=limpar_valor(linha.get("N_TRAB_TOTAL")),
                n_trab_lacos=limpar_valor(linha.get("N_TRAB_LACOS")),
            )
            registros.append(registro)

        session.bulk_save_objects(registros)
        session.commit()

        print(f"Carga concluída com sucesso. Registros importados: {len(registros)}")

    except Exception as erro:
        session.rollback()
        print("Erro ao importar CSV:", erro)

    finally:
        session.close()


if __name__ == "__main__":
    importar_csv()
