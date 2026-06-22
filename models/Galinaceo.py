from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String
from helpers.database import Base


class Galinaceo(Base):
    """
    Modelo que representa uma linha da tabela GALINACEOS.
    As colunas foram mantidas como texto para preservar exatamente os valores do CSV.
    """
    __tablename__ = "galinaceos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sist_cria = Column(String)
    niv_terr = Column(String)
    cod_terr = Column(String)
    nom_terr = Column(String)
    cl_gal = Column(String)
    nom_cl_gal = Column(String)
    e_cria_gal = Column(String)
    e_tem_gal = Column(String)
    e_gal_vend = Column(String)
    e_ovos_prod = Column(String)
    e_ovos_vend = Column(String)
    e_subs = Column(String)
    e_comerc = Column(String)
    e_recebe_ori = Column(String)
    e_ori_gov = Column(String)
    e_ori_propria = Column(String)
    e_ori_coop = Column(String)
    e_ori_emp_int = Column(String)
    e_ori_emp_priv = Column(String)
    e_ori_ong = Column(String)
    e_ori_sist_s = Column(String)
    e_ori_outra = Column(String)
    e_gal_eng = Column(String)
    e_gal_galos = Column(String)
    e_gal_poed = Column(String)
    e_gal_matr = Column(String)
    e_assoc_coop = Column(String)
    e_financ = Column(String)
    e_financ_coop = Column(String)
    e_financ_integ = Column(String)
    e_dap = Column(String)
    e_agrifam = Column(String)
    e_n_agrifam = Column(String)
    e_produtor = Column(String)
    e_cooperativa = Column(String)
    e_sa_ldta = Column(String)
    e_cnpj = Column(String)
    gal_total = Column(String)
    gal_eng = Column(String)
    gal_galos = Column(String)
    gal_poed = Column(String)
    gal_matr = Column(String)
    gal_vend = Column(String)
    v_gal_vend = Column(String)
    q_dz_prod = Column(String)
    q_dz_vend = Column(String)
    v_q_dz_prod = Column(String)
    v_q_dz_vend = Column(String)
    a_total = Column(String)
    a_past_plant = Column(String)
    a_lav_perm = Column(String)
    a_lav_temp = Column(String)
    a_apprl = Column(String)
    vtp_agro = Column(String)
    rect_agro = Column(String)
    n_trab_total = Column(String)
    n_trab_lacos = Column(String)

    def to_dict(self):
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
            "N_TRAB_LACOS": self.n_trab_lacos
        }


class GalinaceoSchema(Schema):
    id = fields.Integer(dump_only=True)
    sist_cria = fields.String(allow_none=True)
    niv_terr = fields.String(allow_none=True)
    cod_terr = fields.String(allow_none=True)
    nom_terr = fields.String(allow_none=True)
    cl_gal = fields.String(allow_none=True)
    nom_cl_gal = fields.String(allow_none=True)
    e_cria_gal = fields.String(allow_none=True)
    e_tem_gal = fields.String(allow_none=True)
    e_gal_vend = fields.String(allow_none=True)
    e_ovos_prod = fields.String(allow_none=True)
    e_ovos_vend = fields.String(allow_none=True)
    e_subs = fields.String(allow_none=True)
    e_comerc = fields.String(allow_none=True)
    e_recebe_ori = fields.String(allow_none=True)
    e_ori_gov = fields.String(allow_none=True)
    e_ori_propria = fields.String(allow_none=True)
    e_ori_coop = fields.String(allow_none=True)
    e_ori_emp_int = fields.String(allow_none=True)
    e_ori_emp_priv = fields.String(allow_none=True)
    e_ori_ong = fields.String(allow_none=True)
    e_ori_sist_s = fields.String(allow_none=True)
    e_ori_outra = fields.String(allow_none=True)
    e_gal_eng = fields.String(allow_none=True)
    e_gal_galos = fields.String(allow_none=True)
    e_gal_poed = fields.String(allow_none=True)
    e_gal_matr = fields.String(allow_none=True)
    e_assoc_coop = fields.String(allow_none=True)
    e_financ = fields.String(allow_none=True)
    e_financ_coop = fields.String(allow_none=True)
    e_financ_integ = fields.String(allow_none=True)
    e_dap = fields.String(allow_none=True)
    e_agrifam = fields.String(allow_none=True)
    e_n_agrifam = fields.String(allow_none=True)
    e_produtor = fields.String(allow_none=True)
    e_cooperativa = fields.String(allow_none=True)
    e_sa_ldta = fields.String(allow_none=True)
    e_cnpj = fields.String(allow_none=True)
    gal_total = fields.String(allow_none=True)
    gal_eng = fields.String(allow_none=True)
    gal_galos = fields.String(allow_none=True)
    gal_poed = fields.String(allow_none=True)
    gal_matr = fields.String(allow_none=True)
    gal_vend = fields.String(allow_none=True)
    v_gal_vend = fields.String(allow_none=True)
    q_dz_prod = fields.String(allow_none=True)
    q_dz_vend = fields.String(allow_none=True)
    v_q_dz_prod = fields.String(allow_none=True)
    v_q_dz_vend = fields.String(allow_none=True)
    a_total = fields.String(allow_none=True)
    a_past_plant = fields.String(allow_none=True)
    a_lav_perm = fields.String(allow_none=True)
    a_lav_temp = fields.String(allow_none=True)
    a_apprl = fields.String(allow_none=True)
    vtp_agro = fields.String(allow_none=True)
    rect_agro = fields.String(allow_none=True)
    n_trab_total = fields.String(allow_none=True)
    n_trab_lacos = fields.String(allow_none=True)
