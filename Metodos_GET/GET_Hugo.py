from flask_restful import Resource
from flask import jsonify

import sys
sys.path.insert(0, '../Funcoes')

# Funcoes
from Funcoes.Hugo import Hugo
f_hugo = Hugo()

class Est_ocorrencias(Resource):
    def get(self):
        result = f_hugo.est_ocorrencias()
        return jsonify(result)

class Est_ocorrencias_estado(Resource):
    def get(self, sigla):
        result = f_hugo.est_ocorrencias_estado(sigla)
        return jsonify(result)

class Est_ocorrencias_estado_datas(Resource):
    def get(self, sigla, data_inicio, data_fim):
        result = f_hugo.est_ocorrencias_estados_datas(sigla, data_inicio, data_fim)
        return jsonify(result)

class Est_ocorrencias_crimes(Resource):
    def get(self, crime):
        result = f_hugo.est_ocorrencias_crime(crime)
        return jsonify(result)

class Est_ocorrencias_crimes_datas(Resource):
    def get(self, crime, data_inicio, data_fim):
        result = f_hugo.est_ocorrencias_crimes_datas(crime, data_inicio, data_fim)
        return jsonify(result)

class Est_ocorrencias_estado_crimes(Resource):
    def get(self, estado, crime):
        result = f_hugo.est_ocorrencias_estado_crimes_datas(estado, crime)
        return jsonify(result)

class Est_vitimas(Resource):
    def get(self):
        result = f_hugo.estado_vitimas()
        return jsonify(result)

class Municipios(Resource):
    def get(self):
        result = f_hugo.municipio()
        return jsonify(result)

class UserById(Resource):
    def get(self, id, sexo):
        result = ['USUARIO', id, sexo]
        return jsonify(result)