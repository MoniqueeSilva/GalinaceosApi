from helpers.database import get_conn
from helpers.logger import logger


class GalinaceoRepository():
    def getAll(self, filtros):
        conn = get_conn()
        cursor = conn.cursor()

        query = "SELECT id, sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, nom_cl_gal, e_cria_gal, e_tem_gal, e_gal_vend, e_ovos_prod, e_ovos_vend, e_subs, e_comerc, e_recebe_ori, e_ori_gov, e_ori_propria, e_ori_coop, e_ori_emp_int, e_ori_emp_priv, e_ori_ong, e_ori_sist_s, e_ori_outra, e_gal_eng, e_gal_galos, e_gal_poed, e_gal_matr, e_assoc_coop, e_financ, e_financ_coop, e_financ_integ, e_dap, e_agrifam, e_n_agrifam, e_produtor, e_cooperativa, e_sa_ldta, e_cnpj, gal_total, gal_eng, gal_galos, gal_poed, gal_matr, gal_vend, v_gal_vend, q_dz_prod, q_dz_vend, v_q_dz_prod, v_q_dz_vend, a_total, a_past_plant, a_lav_perm, a_lav_temp, a_apprl, vtp_agro, rect_agro, n_trab_total, n_trab_lacos FROM tb_galinaceos"
        condicoes = []
        valores = []

        if filtros.get("SIST_CRIA"):
            condicoes.append("sist_cria = %s")
            valores.append(filtros.get("SIST_CRIA"))

        if filtros.get("NIV_TERR"):
            condicoes.append("niv_terr = %s")
            valores.append(filtros.get("NIV_TERR"))

        if filtros.get("COD_TERR"):
            condicoes.append("cod_terr = %s")
            valores.append(filtros.get("COD_TERR"))

        if filtros.get("NOM_TERR"):
            condicoes.append("nom_terr ILIKE %s")
            valores.append(f"%{filtros.get('NOM_TERR')}%")

        if filtros.get("CL_GAL"):
            condicoes.append("cl_gal = %s")
            valores.append(filtros.get("CL_GAL"))

        if len(condicoes) > 0:
            query += " WHERE " + " AND ".join(condicoes)

        query += " ORDER BY id"

        logger.info("Preparando consulta de galináceos")
        cursor.execute(query, tuple(valores))
        return cursor.fetchall()

    def getByIdGalinaceo(self, id):
        conn = get_conn()
        cursor = conn.cursor()
        logger.info("Preparando consulta por id")
        cursor.execute("SELECT id, sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, nom_cl_gal, e_cria_gal, e_tem_gal, e_gal_vend, e_ovos_prod, e_ovos_vend, e_subs, e_comerc, e_recebe_ori, e_ori_gov, e_ori_propria, e_ori_coop, e_ori_emp_int, e_ori_emp_priv, e_ori_ong, e_ori_sist_s, e_ori_outra, e_gal_eng, e_gal_galos, e_gal_poed, e_gal_matr, e_assoc_coop, e_financ, e_financ_coop, e_financ_integ, e_dap, e_agrifam, e_n_agrifam, e_produtor, e_cooperativa, e_sa_ldta, e_cnpj, gal_total, gal_eng, gal_galos, gal_poed, gal_matr, gal_vend, v_gal_vend, q_dz_prod, q_dz_vend, v_q_dz_prod, v_q_dz_vend, a_total, a_past_plant, a_lav_perm, a_lav_temp, a_apprl, vtp_agro, rect_agro, n_trab_total, n_trab_lacos FROM tb_galinaceos WHERE id=%s", (id,))
        return cursor.fetchone()
