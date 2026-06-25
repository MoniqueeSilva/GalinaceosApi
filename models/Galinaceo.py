from marshmallow import Schema, fields

class Galinaceo():
    def __init__(self, id, sist_cria, niv_terr, cod_terr, nom_terr, cl_gal, nom_cl_gal, e_cria_gal, e_tem_gal, e_gal_vend, e_ovos_prod, e_ovos_vend, e_subs, e_comerc, e_recebe_ori, e_ori_gov, e_ori_propria, e_ori_coop, e_ori_emp_int, e_ori_emp_priv, e_ori_ong, e_ori_sist_s, e_ori_outra, e_gal_eng, e_gal_galos, e_gal_poed, e_gal_matr, e_assoc_coop, e_financ, e_financ_coop, e_financ_integ, e_dap, e_agrifam, e_n_agrifam, e_produtor, e_cooperativa, e_sa_ldta, e_cnpj, gal_total, gal_eng, gal_galos, gal_poed, gal_matr, gal_vend, v_gal_vend, q_dz_prod, q_dz_vend, v_q_dz_prod, v_q_dz_vend, a_total, a_past_plant, a_lav_perm, a_lav_temp, a_apprl, vtp_agro, rect_agro, n_trab_total, n_trab_lacos):
        self.id = id
        self.sist_cria = sist_cria
        self.niv_terr = niv_terr
        self.cod_terr = cod_terr
        self.nom_terr = nom_terr
        self.cl_gal = cl_gal
        self.nom_cl_gal = nom_cl_gal
        self.e_cria_gal = e_cria_gal
        self.e_tem_gal = e_tem_gal
        self.e_gal_vend = e_gal_vend
        self.e_ovos_prod = e_ovos_prod
        self.e_ovos_vend = e_ovos_vend
        self.e_subs = e_subs
        self.e_comerc = e_comerc
        self.e_recebe_ori = e_recebe_ori
        self.e_ori_gov = e_ori_gov
        self.e_ori_propria = e_ori_propria
        self.e_ori_coop = e_ori_coop
        self.e_ori_emp_int = e_ori_emp_int
        self.e_ori_emp_priv = e_ori_emp_priv
        self.e_ori_ong = e_ori_ong
        self.e_ori_sist_s = e_ori_sist_s
        self.e_ori_outra = e_ori_outra
        self.e_gal_eng = e_gal_eng
        self.e_gal_galos = e_gal_galos
        self.e_gal_poed = e_gal_poed
        self.e_gal_matr = e_gal_matr
        self.e_assoc_coop = e_assoc_coop
        self.e_financ = e_financ
        self.e_financ_coop = e_financ_coop
        self.e_financ_integ = e_financ_integ
        self.e_dap = e_dap
        self.e_agrifam = e_agrifam
        self.e_n_agrifam = e_n_agrifam
        self.e_produtor = e_produtor
        self.e_cooperativa = e_cooperativa
        self.e_sa_ldta = e_sa_ldta
        self.e_cnpj = e_cnpj
        self.gal_total = gal_total
        self.gal_eng = gal_eng
        self.gal_galos = gal_galos
        self.gal_poed = gal_poed
        self.gal_matr = gal_matr
        self.gal_vend = gal_vend
        self.v_gal_vend = v_gal_vend
        self.q_dz_prod = q_dz_prod
        self.q_dz_vend = q_dz_vend
        self.v_q_dz_prod = v_q_dz_prod
        self.v_q_dz_vend = v_q_dz_vend
        self.a_total = a_total
        self.a_past_plant = a_past_plant
        self.a_lav_perm = a_lav_perm
        self.a_lav_temp = a_lav_temp
        self.a_apprl = a_apprl
        self.vtp_agro = vtp_agro
        self.rect_agro = rect_agro
        self.n_trab_total = n_trab_total
        self.n_trab_lacos = n_trab_lacos

    def toDict(self):
        return {
            "id": self.id,
            "SIST_CRIA": self.sist_cria,
            "NIV_TERR": self.niv_terr,
            "COD_TERR": self.cod_terr,
            "NOM_TERR": self.nom_terr,
            "CL_GAL": self.cl_gal,
            "NOM_CL_GAL": self.nom_cl_gal,
            "E_CRIA_GAL": self.e_cria_gal,
            "E_TEM_GAL": self.e_tem_gal,
            "E_GAL_VEND": self.e_gal_vend,
            "E_OVOS_PROD": self.e_ovos_prod,
            "E_OVOS_VEND": self.e_ovos_vend,
            "E_SUBS": self.e_subs,
            "E_COMERC": self.e_comerc,
            "E_RECEBE_ORI": self.e_recebe_ori,
            "E_ORI_GOV": self.e_ori_gov,
            "E_ORI_PROPRIA": self.e_ori_propria,
            "E_ORI_COOP": self.e_ori_coop,
            "E_ORI_EMP_INT": self.e_ori_emp_int,
            "E_ORI_EMP_PRIV": self.e_ori_emp_priv,
            "E_ORI_ONG": self.e_ori_ong,
            "E_ORI_SIST_S": self.e_ori_sist_s,
            "E_ORI_OUTRA": self.e_ori_outra,
            "E_GAL_ENG": self.e_gal_eng,
            "E_GAL_GALOS": self.e_gal_galos,
            "E_GAL_POED": self.e_gal_poed,
            "E_GAL_MATR": self.e_gal_matr,
            "E_ASSOC_COOP": self.e_assoc_coop,
            "E_FINANC": self.e_financ,
            "E_FINANC_COOP": self.e_financ_coop,
            "E_FINANC_INTEG": self.e_financ_integ,
            "E_DAP": self.e_dap,
            "E_AGRIFAM": self.e_agrifam,
            "E_N_AGRIFAM": self.e_n_agrifam,
            "E_PRODUTOR": self.e_produtor,
            "E_COOPERATIVA": self.e_cooperativa,
            "E_SA_LDTA": self.e_sa_ldta,
            "E_CNPJ": self.e_cnpj,
            "GAL_TOTAL": self.gal_total,
            "GAL_ENG": self.gal_eng,
            "GAL_GALOS": self.gal_galos,
            "GAL_POED": self.gal_poed,
            "GAL_MATR": self.gal_matr,
            "GAL_VEND": self.gal_vend,
            "V_GAL_VEND": self.v_gal_vend,
            "Q_DZ_PROD": self.q_dz_prod,
            "Q_DZ_VEND": self.q_dz_vend,
            "V_Q_DZ_PROD": self.v_q_dz_prod,
            "V_Q_DZ_VEND": self.v_q_dz_vend,
            "A_TOTAL": self.a_total,
            "A_PAST_PLANT": self.a_past_plant,
            "A_LAV_PERM": self.a_lav_perm,
            "A_LAV_TEMP": self.a_lav_temp,
            "A_APPRL": self.a_apprl,
            "VTP_AGRO": self.vtp_agro,
            "RECT_AGRO": self.rect_agro,
            "N_TRAB_TOTAL": self.n_trab_total,
            "N_TRAB_LACOS": self.n_trab_lacos,
        }


class GalinaceoSchema(Schema):
    id = fields.Integer(dump_only=True)
    sist_cria = fields.Str(allow_none=True)
    niv_terr = fields.Str(allow_none=True)
    cod_terr = fields.Str(allow_none=True)
    nom_terr = fields.Str(allow_none=True)
    cl_gal = fields.Str(allow_none=True)
    nom_cl_gal = fields.Str(allow_none=True)
    e_cria_gal = fields.Str(allow_none=True)
    e_tem_gal = fields.Str(allow_none=True)
    e_gal_vend = fields.Str(allow_none=True)
    e_ovos_prod = fields.Str(allow_none=True)
    e_ovos_vend = fields.Str(allow_none=True)
    e_subs = fields.Str(allow_none=True)
    e_comerc = fields.Str(allow_none=True)
    e_recebe_ori = fields.Str(allow_none=True)
    e_ori_gov = fields.Str(allow_none=True)
    e_ori_propria = fields.Str(allow_none=True)
    e_ori_coop = fields.Str(allow_none=True)
    e_ori_emp_int = fields.Str(allow_none=True)
    e_ori_emp_priv = fields.Str(allow_none=True)
    e_ori_ong = fields.Str(allow_none=True)
    e_ori_sist_s = fields.Str(allow_none=True)
    e_ori_outra = fields.Str(allow_none=True)
    e_gal_eng = fields.Str(allow_none=True)
    e_gal_galos = fields.Str(allow_none=True)
    e_gal_poed = fields.Str(allow_none=True)
    e_gal_matr = fields.Str(allow_none=True)
    e_assoc_coop = fields.Str(allow_none=True)
    e_financ = fields.Str(allow_none=True)
    e_financ_coop = fields.Str(allow_none=True)
    e_financ_integ = fields.Str(allow_none=True)
    e_dap = fields.Str(allow_none=True)
    e_agrifam = fields.Str(allow_none=True)
    e_n_agrifam = fields.Str(allow_none=True)
    e_produtor = fields.Str(allow_none=True)
    e_cooperativa = fields.Str(allow_none=True)
    e_sa_ldta = fields.Str(allow_none=True)
    e_cnpj = fields.Str(allow_none=True)
    gal_total = fields.Str(allow_none=True)
    gal_eng = fields.Str(allow_none=True)
    gal_galos = fields.Str(allow_none=True)
    gal_poed = fields.Str(allow_none=True)
    gal_matr = fields.Str(allow_none=True)
    gal_vend = fields.Str(allow_none=True)
    v_gal_vend = fields.Str(allow_none=True)
    q_dz_prod = fields.Str(allow_none=True)
    q_dz_vend = fields.Str(allow_none=True)
    v_q_dz_prod = fields.Str(allow_none=True)
    v_q_dz_vend = fields.Str(allow_none=True)
    a_total = fields.Str(allow_none=True)
    a_past_plant = fields.Str(allow_none=True)
    a_lav_perm = fields.Str(allow_none=True)
    a_lav_temp = fields.Str(allow_none=True)
    a_apprl = fields.Str(allow_none=True)
    vtp_agro = fields.Str(allow_none=True)
    rect_agro = fields.Str(allow_none=True)
    n_trab_total = fields.Str(allow_none=True)
    n_trab_lacos = fields.Str(allow_none=True)
