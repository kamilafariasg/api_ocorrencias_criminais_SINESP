from flask import Flask
from flask_restful import Api

# A sessão esta comentada para rodar mais rápido(Testes)
"""
from download_df import download #comentado pra executar mais rapido
download()
"""

app = Flask(__name__)
api = Api(app)

from Metodos_GET.GET_Alice import *
from Metodos_GET.GET_Angela import *
from Metodos_GET.GET_Fabricio import *
from Metodos_GET.GET_Hugo import *
from Metodos_GET.GET_Kamila import *
from Metodos_GET.GET_Renato import *
from Metodos_GET.GET_Thiago import *

# Rotas Hugo
api.add_resource(Municipios, '/municipios') 
api.add_resource(Est_ocorrencias, '/estados_ocorrencias')
api.add_resource(Est_ocorrencias_estado, '/estados_ocorrencias/<estado>')
api.add_resource(Est_ocorrencias_estado_datas, '/estados_ocorrencias/<estado>/<data_inicio>/<data_fim>')

api.add_resource(Est_vitimas, '/estados_vitimas') 
api.add_resource(UserById, '/users/<id>/<sexo>') 

# Rotas Alice
api.add_resource(metodo_get_alice, '/alice') 

# Rotas Angela
api.add_resource(metodo_get_angela, '/angela') 

# Rotas Fabricio
api.add_resource(metodo_get_fabricio, '/fabricio') 

# Rotas Kamila
api.add_resource(metodo_get_kamila, '/kamila') 

# Rotas Renato
api.add_resource(metodo_get_renato, '/renato') 

# Rotas Thiago
api.add_resource(metodo_get_thiago, '/thiago') 

if __name__ == '__main__':
    app.run(host="localhost", port=3000)