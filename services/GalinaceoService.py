from helpers.logger import logger
from repositories.GalinaceoRepository import GalinaceoRepository
from models.Galinaceo import Galinaceo


def rowToGalinaceo(row):
    return Galinaceo(
        id=row[0],
        sist_cria=row[1], 
        niv_terr=row[2], 
        cod_terr=row[3], 
        nom_terr=row[4], 
        cl_gal=row[5], 
        nom_cl_gal=row[6], 
        e_cria_gal=row[7], 
        e_tem_gal=row[8], 
        e_gal_vend=row[9], 
        e_ovos_prod=row[10], 
        e_ovos_vend=row[11], 
        e_subs=row[12], 
        e_comerc=row[13], 
        e_recebe_ori=row[14], 
        e_ori_gov=row[15], 
        e_ori_propria=row[16], 
        e_ori_coop=row[17], 
        e_ori_emp_int=row[18], 
        e_ori_emp_priv=row[19], 
        e_ori_ong=row[20], 
        e_ori_sist_s=row[21], 
        e_ori_outra=row[22], 
        e_gal_eng=row[23], 
        e_gal_galos=row[24], 
        e_gal_poed=row[25], 
        e_gal_matr=row[26], 
        e_assoc_coop=row[27], 
        e_financ=row[28], 
        e_financ_coop=row[29], 
        e_financ_integ=row[30], 
        e_dap=row[31], 
        e_agrifam=row[32], 
        e_n_agrifam=row[33], 
        e_produtor=row[34], 
        e_cooperativa=row[35], 
        e_sa_ldta=row[36], 
        e_cnpj=row[37], 
        gal_total=row[38], 
        gal_eng=row[39], 
        gal_galos=row[40], 
        gal_poed=row[41], 
        gal_matr=row[42], 
        gal_vend=row[43], 
        v_gal_vend=row[44], 
        q_dz_prod=row[45], 
        q_dz_vend=row[46], 
        v_q_dz_prod=row[47], 
        v_q_dz_vend=row[48], 
        a_total=row[49], 
        a_past_plant=row[50], 
        a_lav_perm=row[51], 
        a_lav_temp=row[52], 
        a_apprl=row[53], 
        vtp_agro=row[54], 
        rect_agro=row[55], 
        n_trab_total=row[56], 
        n_trab_lacos=row[57], 
    )


class GalinaceoService():
    def __init__(self):
        self.galinaceoRepository = GalinaceoRepository()

    def getAll(self, filtros):
        rows = self.galinaceoRepository.getAll(filtros)
        logger.info(f"Retornando {len(rows)} registros de galináceos")
        return [rowToGalinaceo(r) for r in rows]

    def getByIdGalinaceo(self, id):
        row = self.galinaceoRepository.getByIdGalinaceo(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return rowToGalinaceo(row) if row is not None else None
