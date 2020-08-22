from flask_restful import Resource
from flask import jsonify

import sys
sys.path.insert(0, '../Funcoes')

# Funcoes
from Funcoes.Hugo import Hugo
f_hugo = Hugo()

class Municipios(Resource):
    def get(self):
        result = f_hugo.base_municipio()
        return jsonify(result)

class Est_ocorrencias(Resource):
    def get(self):
        result = f_hugo.base_est_ocorrencias()
        return jsonify(result)

class Est_ocorrencias_estado(Resource):
    def get(self, estado):
        result = f_hugo.base_est_ocorrencias_estado(estado)
        return jsonify(result)

class Est_ocorrencias_estado_datas(Resource):
    def get(self, estado, data_inicio, data_fim):
        result = f_hugo.base_est_ocorrencias_estados_datas(estado, data_inicio, data_fim)
        return jsonify(result)

class Est_vitimas(Resource):
    def get(self):
        result = f_hugo.base_estado_vitimas()
        return jsonify(result)

class UserById(Resource):
    def get(self, id, sexo):
        result = ['USUARIO', id, sexo]
        return jsonify(result)