import json
import unicodedata
import numpy as np
import pandas as pd

### Hugo

estados = '{"AC": "Acre","AL": "Alagoas","AP": "Amapá","AM": "Amazonas","BA": "Bahia","CE": "Ceará","DF": "Distrito Federal","ES": "Espírito Santo","GO": "Goiás","MA": "Maranhão","MT": "Mato Grosso","MS": "Mato Grosso do Sul","MG": "Minas Gerais","PA": "Pará","PB": "Paraíba","PR": "Paraná","PE": "Pernambuco","PI": "Piauí","RJ": "Rio de Janeiro","RN": "Rio Grande do Norte","RS": "Rio Grande do Sul","RO": "Rondônia","RR": "Roraima","SC": "Santa Catarina","SP": "São Paulo","SE": "Sergipe","TO": "Tocantins"}'
estados_json = json.loads(estados)

meses_ab_numero = '{"jan":"01", "fev":"02", "mar":"03", "abr":"04", "mai":"05", "jun":"06", "jul":"07", "ago":"08", "set":"09", "out":"10", "nov":"11", "dez":"12"}'
meses_ab_numero_json = json.loads(meses_ab_numero)

meses_ab_nome = '{"jan":"janeiro", "fev":"fevereiro", "mar":"março", "abr":"abril", "mai":"maio", "jun":"junho", "jul":"julho", "ago":"agosto", "set":"setembro", "out":"outubro", "nov":"novembro", "dez":"dezembro"}'
meses_ab_nome_json = json.loads(meses_ab_nome)

meses_vetor = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]

def converte_sigla_em_nome(sigla): 
    try:
        retorno = estados_json[sigla]
    except:
        retorno = []
    finally:
        return retorno

def converte_abrev_numero(abrev):
    try:
        retorno = meses_ab_numero_json[abrev]
    except:
        retorno = []
    finally:
        return retorno

def converte_abrev_nome(abrev):
    try:
        retorno = meses_ab_nome_json[abrev]
    except:
        retorno = []
    finally:
        return retorno

def pega_mes(var):
    try: 
        splitado = var.split('-')
        retorno = converte_abrev_nome(splitado[0])
    except:
        retorno = []
    finally:
        return retorno

def pega_ano(var):
    try: 
        splitado = var.split('-')
        retorno = splitado[1]
    except:
        retorno = []
    finally:
        return retorno

def converte_para_data(var): 
    try: 
        splitado = var.split('-')
        mes = converte_abrev_numero(splitado[0])
        ano = splitado[1]
        retorno = ano+'-'+mes+'-'+'01'
    except:
        retorno = []
    finally:
        return retorno

def pega_meses_maiores(mes):
    index = meses_vetor.index(mes)
    return meses_vetor[index:]

def pega_meses_menores(mes):
    index = meses_vetor.index(mes)
    return meses_vetor[0:index+1]

def pega_meses_intervalo(mes_ini, mes_fim):
    index_ini = meses_vetor.index(mes_ini)
    index_fim = meses_vetor.index(mes_fim)
    return meses_vetor[index_ini:index_fim+1]

def data_inicio_eh_maior_data_fim(data_inicio, data_fim):
    meses_ano = pega_meses_maiores("janeiro")
    mes_ini = pega_mes(data_inicio)
    ano_ini = int(pega_ano(data_inicio))
    mes_fim = pega_mes(data_fim)
    ano_fim = int(pega_ano(data_fim))

    if ano_ini>ano_fim:
        return True
    elif ano_fim == ano_ini:
        index_ini = meses_vetor.index(mes_ini)
        index_fim = meses_vetor.index(mes_fim)
        if index_ini>index_fim:
            return True
        else:
            return False
    else:
        return False

def tira_acentos(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def trata_palavra(palavra):
    palavra = palavra.replace("_"," ")
    palavra = tira_acentos(palavra)
    palavra = palavra.lower()
    return palavra

def trata_vetor_palavra(vetor):
    vetor_tratado = []
    for palavra in vetor:
        vetor_tratado.append([trata_palavra(palavra)])
    return np.array(vetor_tratado)

def agrupa_por_municipio(municipios):
    base_mun = pd.DataFrame(municipios,columns=['Município','Sigla UF','Região','Mês/Ano','Vítimas'])
    base_mun[['Município']] = base_mun[['Município']].apply(lambda x: x.str.lower())
    new_base = base_mun.groupby(['Município','Sigla UF','Região']).agg(['sum', 'count']).reset_index()
    new_base.columns = new_base.columns.droplevel()
    new_base.columns = ['Município','Sigla UF','Região','Quant_Vítimas', 'Quant_Instâncias']

    return new_base

### Alice

### Angela

### Fabricio

### Kamila

### Renato

### Thiago
