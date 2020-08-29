import pandas as pd
import numpy as np

from func_auxiliares import converte_sigla_em_nome
from func_auxiliares import pega_mes
from func_auxiliares import pega_ano
from func_auxiliares import converte_para_data
from func_auxiliares import pega_meses_maiores
from func_auxiliares import pega_meses_menores
from func_auxiliares import pega_meses_intervalo
from func_auxiliares import trata_vetor_palavra
from func_auxiliares import trata_palavra
from func_auxiliares import data_inicio_eh_maior_data_fim
from func_auxiliares import agrupa_por_municipio

class Hugo:
    def __init__(self):
        self.df_municipio = pd.read_excel('Bases/base_por_municipio.xlsx', sheet_name=["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"])
        self.df_estado = pd.read_excel('Bases/base_por_estado.xlsx', sheet_name=['Ocorrências','Vítimas'])

    def estados(self, tipo):
        result = self.df_estado[tipo]
        result = result.values.tolist()
        return result

    def estados_estado(self, tipo, sigla):
        estado = converte_sigla_em_nome(sigla)
        result = self.df_estado[tipo][self.df_estado[tipo]["UF"] == estado]
        result = result.values.tolist()
        return result
    
    def estados_estado_datas(self, tipo, sigla, data_inicio, data_fim):
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
        cond_estado = np.transpose(np.array([self.df_estado[tipo]["UF"] == estado]))

        #Condicao 2
        cond_anos_maiores = np.transpose(np.array([self.df_estado[tipo]["Ano"] > ano_ini]))

        #Condicao 3
        cond_anos_menores = np.transpose(np.array([self.df_estado[tipo]["Ano"] < ano_fim]))

        #Condicao 4
        cond_ano_ini = np.transpose(np.array([self.df_estado[tipo]["Ano"] == ano_ini]))

        cond_meses_ano_ini = []
        for mes in self.df_estado[tipo]["Mês"]:
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
        cond_ano_fim = np.transpose(np.array([self.df_estado[tipo]["Ano"] == ano_fim]))

        cond_meses_ano_fim = []
        for mes in self.df_estado[tipo]["Mês"]:
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

        result = self.df_estado[tipo][condicao]

        result = result.values.tolist()
        return result

    def estados_crime(self, tipo, crime):
        palavras_tratadas = trata_vetor_palavra(self.df_estado[tipo]["Tipo Crime"])
        palavra = trata_palavra(crime)
        
        result = self.df_estado[tipo][palavras_tratadas == palavra]

        result = result.values.tolist()
        return result

    def estados_crime_datas(self, tipo, crime, data_inicio, data_fim):
        if data_inicio_eh_maior_data_fim(data_inicio, data_fim):
            result = []
            return result
        
        crimes_tratados = trata_vetor_palavra(self.df_estado[tipo]["Tipo Crime"])
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
        cond_anos_maiores = np.transpose(np.array([self.df_estado[tipo]["Ano"] > ano_ini]))

        #Condicao 3
        cond_anos_menores = np.transpose(np.array([self.df_estado[tipo]["Ano"] < ano_fim]))

        #Condicao 4
        cond_ano_ini = np.transpose(np.array([self.df_estado[tipo]["Ano"] == ano_ini]))

        cond_meses_ano_ini = []
        for mes in self.df_estado[tipo]["Mês"]:
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
        cond_ano_fim = np.transpose(np.array([self.df_estado[tipo]["Ano"] == ano_fim]))

        cond_meses_ano_fim = []
        for mes in self.df_estado[tipo]["Mês"]:
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

        result = self.df_estado[tipo][condicao]

        result = result.values.tolist()
        return result

    def estados_estado_crime(self, tipo, sigla, crime):
        crimes_tratados = trata_vetor_palavra(self.df_estado[tipo]["Tipo Crime"])
        crime = trata_palavra(crime)
        estado = converte_sigla_em_nome(sigla)

        #Condicao 1
        cond_crime = crimes_tratados == crime

        #Condicao 2 
        cond_estado = np.transpose(np.array([self.df_estado[tipo]["UF"] == estado]))

        condicao = np.logical_and(cond_crime, cond_estado)
        
        result = self.df_estado[tipo][condicao]

        result = result.values.tolist()
        return result
    
    def estados_estado_crime_datas(self, tipo, sigla, crime, data_inicio, data_fim):
        if data_inicio_eh_maior_data_fim(data_inicio, data_fim):
            result = []
            return result
        
        crimes_tratados = trata_vetor_palavra(self.df_estado[tipo]["Tipo Crime"])
        crime = trata_palavra(crime)

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
        cond_crime = crimes_tratados == crime

        #Condicao 2 
        cond_estado = np.transpose(np.array([self.df_estado[tipo]["UF"] == estado]))

        #Condicao 3
        cond_anos_maiores = np.transpose(np.array([self.df_estado[tipo]["Ano"] > ano_ini]))

        #Condicao 4
        cond_anos_menores = np.transpose(np.array([self.df_estado[tipo]["Ano"] < ano_fim]))

        #Condicao 5
        cond_ano_ini = np.transpose(np.array([self.df_estado[tipo]["Ano"] == ano_ini]))

        cond_meses_ano_ini = []
        for mes in self.df_estado[tipo]["Mês"]:
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
        cond_crime_ano_ini = np.logical_and(cond_crime_ano_ini, cond_estado)
        cond_meses_ano_ini = np.logical_and(cond_meses_ano_ini, cond_crime_ano_ini)

        #Condicao 6
        cond_ano_fim = np.transpose(np.array([self.df_estado[tipo]["Ano"] == ano_fim]))

        cond_meses_ano_fim = []
        for mes in self.df_estado[tipo]["Mês"]:
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
        cond_crime_ano_fim = np.logical_and(cond_crime_ano_fim, cond_estado)
        cond_meses_ano_fim = np.logical_and(cond_meses_ano_fim, cond_crime_ano_fim)

        condicao = np.logical_and(cond_crime, cond_estado)
        condicao = np.logical_and(condicao, cond_anos_maiores)
        condicao = np.logical_and(condicao, cond_anos_menores)
        condicao = np.logical_or(condicao, cond_meses_ano_ini)
        condicao = np.logical_or(condicao, cond_meses_ano_fim)

        result = self.df_estado[tipo][condicao]

        result = result.values.tolist()
        return result

    def municipios(self):
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

    def municipios_total(self):
        result = agrupa_por_municipio(self.municipios())

        result = result.values.tolist()
        return result