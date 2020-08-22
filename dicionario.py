import json

# Dicionarios de siglas e estados
estados = '{"AC": "Acre","AL": "Alagoas","AP": "Amapá","AM": "Amazonas","BA": "Bahia","CE": "Ceará","DF": "Distrito Federal","ES": "Espírito Santo","GO": "Goiás","MA": "Maranhão","MT": "Mato Grosso","MS": "Mato Grosso do Sul","MG": "Minas Gerais","PA": "Pará","PB": "Paraíba","PR": "Paraná","PE": "Pernambuco","PI": "Piauí","RJ": "Rio de Janeiro","RN": "Rio Grande do Norte","RS": "Rio Grande do Sul","RO": "Rondônia","RR": "Roraima","SC": "Santa Catarina","SP": "São Paulo","SE": "Sergipe","TO": "Tocantins"}'
estados_json = json.loads(estados)
#print(estados_json["CE"]) 

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

