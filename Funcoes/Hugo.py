import pandas as pd
import numpy as np

from dicionario import converte_sigla_em_nome
from dicionario import pega_mes
from dicionario import pega_ano
from dicionario import converte_para_data
from dicionario import pega_meses_maiores
from dicionario import pega_meses_menores
from dicionario import pega_meses_intervalo
from dicionario import trata_vetor_palavra
from dicionario import trata_palavra
from dicionario import data_inicio_eh_maior_data_fim
class Hugo:
    def __init__(self):
        self.df_municipio = pd.read_excel('Bases/base_por_municipio.xlsx', sheet_name=["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"])
        self.df_estado = pd.read_excel('Bases/base_por_estado.xlsx', sheet_name=['Ocorrências','Vítimas'])

    def est_ocorrencias(self):
        result = self.df_estado["Ocorrências"]
        result = result.values.tolist()
        return result

    def est_ocorrencias_estado(self, sigla):
        estado = converte_sigla_em_nome(sigla)
        result = self.df_estado["Ocorrências"][self.df_estado["Ocorrências"]["UF"] == estado]
        result = result.values.tolist()
        return result
    
    def est_ocorrencias_estados_datas(self, sigla, data_inicio, data_fim):
        if data_inicio_eh_maior_data_fim(data_inicio, data_fim):
            result = []
            return result
        
        estado = converte_sigla_em_nome(sigla)
        mes_ini = pega_mes(data_inicio)
        maiores_mes_ini = pega_meses_maiores(mes_ini)
        ano_ini = int(pega_ano(data_inicio))
        mes_fim = pega_mes(data_fim)
        menores_mes_fim = pega_meses_menores(mes_fim)
        ano_fim = int(pega_ano(data_fim))

        if ano_ini == ano_fim:
            maiores_mes_ini = pega_meses_intervalo(mes_ini, mes_fim)
            menores_mes_fim = maiores_mes_ini

        #Condicao 1
        cond_estado = np.transpose(np.array([self.df_estado["Ocorrências"]["UF"] == estado]))

        #Condicao 2
        cond_anos_maiores = np.transpose(np.array([self.df_estado["Ocorrências"]["Ano"] > ano_ini]))

        #Condicao 3
        cond_anos_menores = np.transpose(np.array([self.df_estado["Ocorrências"]["Ano"] < ano_fim]))

        #Condicao 4
        cond_ano_ini = np.transpose(np.array([self.df_estado["Ocorrências"]["Ano"] == ano_ini]))

        cond_meses_ano_ini = []
        for mes in self.df_estado["Ocorrências"]["Mês"]:
            x = 0
            for mesX in maiores_mes_ini:
                if mes == mesX:
                    cond_meses_ano_ini.append([1])
                    x = 1
                    break 
            if x == 0:
                cond_meses_ano_ini.append([0])

        cond_meses_ano_ini = np.array(cond_meses_ano_ini, dtype=bool)
        cond_estado_ano_ini = np.logical_and(cond_estado, cond_ano_ini)
        cond_meses_ano_ini = np.logical_and(cond_meses_ano_ini, cond_estado_ano_ini)

        #Condicao 5
        cond_ano_fim = np.transpose(np.array([self.df_estado["Ocorrências"]["Ano"] == ano_fim]))

        cond_meses_ano_fim = []
        for mes in self.df_estado["Ocorrências"]["Mês"]:
            x = 0
            for mesX in menores_mes_fim:
                if mes == mesX:
                    cond_meses_ano_fim.append([1])
                    x = 1
                    break 
            if x == 0:
                cond_meses_ano_fim.append([0])

        cond_meses_ano_fim = np.array(cond_meses_ano_fim, dtype=bool)
        cond_estado_ano_fim = np.logical_and(cond_estado, cond_ano_fim)
        cond_meses_ano_fim = np.logical_and(cond_meses_ano_fim, cond_estado_ano_fim)

        condicao = np.logical_and(cond_estado, cond_anos_maiores)
        condicao = np.logical_and(condicao, cond_anos_menores)
        condicao = np.logical_or(condicao, cond_meses_ano_ini)
        condicao = np.logical_or(condicao, cond_meses_ano_fim)

        result = self.df_estado["Ocorrências"][condicao]

        result = result.values.tolist()
        return result

    def est_ocorrencias_crime(self, crime):
        palavras_tratadas = trata_vetor_palavra(self.df_estado["Ocorrências"]["Tipo Crime"])
        palavra = trata_palavra(crime)
        
        result = self.df_estado["Ocorrências"][palavras_tratadas == palavra]

        result = result.values.tolist()
        return result

    def est_ocorrencias_crimes_datas(self, crime, data_inicio, data_fim):
        if data_inicio_eh_maior_data_fim(data_inicio, data_fim):
            result = []
            return result
        
        crimes_tratados = trata_vetor_palavra(self.df_estado["Ocorrências"]["Tipo Crime"])
        crime = trata_palavra(crime)
        
        mes_ini = pega_mes(data_inicio)
        maiores_mes_ini = pega_meses_maiores(mes_ini)
        ano_ini = int(pega_ano(data_inicio))
        mes_fim = pega_mes(data_fim)
        menores_mes_fim = pega_meses_menores(mes_fim)
        ano_fim = int(pega_ano(data_fim))

        if ano_ini == ano_fim:
            maiores_mes_ini = pega_meses_intervalo(mes_ini, mes_fim)
            menores_mes_fim = maiores_mes_ini

        #Condicao 1
        cond_crime = crimes_tratados == crime

        #Condicao 2
        cond_anos_maiores = np.transpose(np.array([self.df_estado["Ocorrências"]["Ano"] > ano_ini]))

        #Condicao 3
        cond_anos_menores = np.transpose(np.array([self.df_estado["Ocorrências"]["Ano"] < ano_fim]))

        #Condicao 4
        cond_ano_ini = np.transpose(np.array([self.df_estado["Ocorrências"]["Ano"] == ano_ini]))

        cond_meses_ano_ini = []
        for mes in self.df_estado["Ocorrências"]["Mês"]:
            x = 0
            for mesX in maiores_mes_ini:
                if mes == mesX:
                    cond_meses_ano_ini.append([1])
                    x = 1
                    break 
            if x == 0:
                cond_meses_ano_ini.append([0])

        cond_meses_ano_ini = np.array(cond_meses_ano_ini, dtype=bool)
        cond_crime_ano_ini = np.logical_and(cond_crime, cond_ano_ini)
        cond_meses_ano_ini = np.logical_and(cond_meses_ano_ini, cond_crime_ano_ini)

        #Condicao 5
        cond_ano_fim = np.transpose(np.array([self.df_estado["Ocorrências"]["Ano"] == ano_fim]))

        cond_meses_ano_fim = []
        for mes in self.df_estado["Ocorrências"]["Mês"]:
            x = 0
            for mesX in menores_mes_fim:
                if mes == mesX:
                    cond_meses_ano_fim.append([1])
                    x = 1
                    break 
            if x == 0:
                cond_meses_ano_fim.append([0])

        cond_meses_ano_fim = np.array(cond_meses_ano_fim, dtype=bool)
        cond_crime_ano_fim = np.logical_and(cond_crime, cond_ano_fim)
        cond_meses_ano_fim = np.logical_and(cond_meses_ano_fim, cond_crime_ano_fim)

        condicao = np.logical_and(cond_crime, cond_anos_maiores)
        condicao = np.logical_and(condicao, cond_anos_menores)
        condicao = np.logical_or(condicao, cond_meses_ano_ini)
        condicao = np.logical_or(condicao, cond_meses_ano_fim)

        result = self.df_estado["Ocorrências"][condicao]

        result = result.values.tolist()
        return result

    def estado_vitimas(self):
        result = self.df_estado["Vítimas"].values.tolist()
        return result
    
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
