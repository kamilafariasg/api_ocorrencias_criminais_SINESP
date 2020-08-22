import pandas as pd
from dicionario import converte_sigla_em_nome
from dicionario import pega_mes
from dicionario import pega_ano
from dicionario import converte_para_data

class Hugo:
    def __init__(self):
        self.df_municipio = pd.read_excel('Bases/base_por_municipio.xlsx', sheet_name=["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"])
        self.df_estado = pd.read_excel('Bases/base_por_estado.xlsx', sheet_name=['Ocorrências','Vítimas'])

    def municipio(self):
        result = self.df_municipio["AC"]
        result = result.append(self.df_municipio["AL"])
        result = result.append(self.df_municipio["AP"])
        result = result.append(self.df_municipio["AM"])
        result = result.append(self.df_municipio["BA"])
        result = result.append(self.df_municipio["CE"])
        result = result.append(self.df_municipio["DF"])
        result = result.append(self.df_municipio["ES"])
        result = result.append(self.df_municipio["GO"])
        result = result.append(self.df_municipio["MA"])
        result = result.append(self.df_municipio["MT"])
        result = result.append(self.df_municipio["MS"])
        result = result.append(self.df_municipio["MG"])
        result = result.append(self.df_municipio["PA"])
        result = result.append(self.df_municipio["PB"])
        result = result.append(self.df_municipio["PR"])
        result = result.append(self.df_municipio["PE"])
        result = result.append(self.df_municipio["PI"])
        result = result.append(self.df_municipio["RJ"])
        result = result.append(self.df_municipio["RN"])
        result = result.append(self.df_municipio["RS"])
        result = result.append(self.df_municipio["RO"])
        result = result.append(self.df_municipio["RR"])
        result = result.append(self.df_municipio["SC"])
        result = result.append(self.df_municipio["SP"])
        result = result.append(self.df_municipio["SE"])
        result = result.append(self.df_municipio["TO"])
        result = result.values.tolist()
        return result

    def est_ocorrencias(self):
        result = self.df_estado["Ocorrências"]
        result = result.values.tolist()
        return result

    def est_ocorrencias_estado(self, sigla):
        estado = converte_sigla_em_nome(sigla)
        result = self.df_estado["Ocorrências"][self.df_estado["Ocorrências"]["UF"] == estado]
        result = result.values.tolist()
        return result
    
    def est_ocorrencias_estados_datas(self, estado, data_inicio, data_fim):
        #result = self.df_estado["Ocorrências"].values.tolist()
        return [estado, data_inicio, data_fim]

    def estado_vitimas(self):
        result = self.df_estado["Vítimas"].values.tolist()
        return result