import requests
import json
import urllib.request 

def download():
    # Fazendo a requisão dos dados na api do governo (ckan)
    url_api_dados = "http://dados.gov.br/api/rest/dataset/sistema-nacional-de-estatisticas-de-seguranca-publica"
    r = requests.get(url_api_dados)

    # Pegando o conteudo do retorno, para entao pegar os links das bases de dados
    conteudo = json.loads(r.content)

    #url_municipio = "http://dados.mj.gov.br/dataset/210b9ae2-21fc-4986-89c6-2006eb4db247/resource/03af7ce2-174e-4ebd-b085-384503cfb40f/download/indicadoressegurancapublicamunicmar20.xlsx"
    #url_estado = "http://dados.mj.gov.br/dataset/210b9ae2-21fc-4986-89c6-2006eb4db247/resource/feeae05e-faba-406c-8a4a-512aec91a9d1/download/indicadoressegurancapublicaufmar20.xlsx"
    url_municipio = json.dumps(conteudo["resources"][1]['url']) 
    url_municipio = url_municipio[1:-1]
    url_estado = json.dumps(conteudo["resources"][2]['url']) 
    url_estado = url_estado[1:-1]

    # Baixando as bases e salvando em dois arquivos
    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', 'whatever')
    filename, headers = opener.retrieve(url_municipio, 'Bases/base_por_municipio.xlsx')
    filename, headers = opener.retrieve(url_estado, 'Bases/base_por_estado.xlsx')
