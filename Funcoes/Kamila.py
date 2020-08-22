import pandas as pd
from dicionario import converte_sigla_em_nome
from dicionario import pega_mes
from dicionario import pega_ano
from dicionario import converte_para_data

class Kamila:
    def __init__(self):
        self.df_municipio = pd.read_excel('Bases/base_por_municipio.xlsx', sheet_name=["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"])
        self.df_estado = pd.read_excel('Bases/base_por_estado.xlsx', sheet_name=['Ocorrências','Vítimas'])

    # Metodo Modelo/Teste
    def funcao_kamila(self):
        result = "Kamila"
        return result