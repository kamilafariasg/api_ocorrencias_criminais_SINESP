from flask_restful import Resource
from flask import jsonify

import sys
sys.path.insert(0, '../Funcoes')

# Funcoes
from Funcoes.Hugo import Hugo
f_hugo = Hugo()

ocorrencias = "Ocorrências"
vitimas = "Vítimas"

class Est_ocorrencias(Resource):
    def get(self):
        try:
            result = f_hugo.estados(ocorrencias)
        except:
            result = []
        finally:
            return jsonify(result)

class Est_ocorrencias_estado(Resource):
    def get(self, sigla):
        try:
            result = f_hugo.estados_estado(ocorrencias,sigla)
        except:
            result = []
        finally:
            return jsonify(result)

class Est_ocorrencias_estado_datas(Resource):
    def get(self, sigla, data_inicio, data_fim):
        try:
            result = f_hugo.estados_estado_datas(ocorrencias,sigla, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)

class Est_ocorrencias_crime(Resource):
    def get(self, crime):
        try:
            result = f_hugo.estados_crime(ocorrencias, crime)
        except:
            result = []
        finally:
            return jsonify(result)

class Est_ocorrencias_crime_datas(Resource):
    def get(self, crime, data_inicio, data_fim):
        try:
            result = f_hugo.estados_crime_datas(ocorrencias, crime, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)
class Est_ocorrencias_estado_crime(Resource):
    def get(self, sigla, crime):
        try:
            result = f_hugo.estados_estado_crime(ocorrencias, sigla, crime)
        except:
            result = []
        finally:
            return jsonify(result)

class Est_ocorrencias_estado_crime_datas(Resource):
    def get(self, sigla, crime, data_inicio, data_fim):
        try:
            result = f_hugo.estados_estado_crime_datas(ocorrencias, sigla, crime, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)

class Est_vitimas(Resource):
    def get(self):
        try:
            result = f_hugo.estados(vitimas)
        except:
            result = []
        finally:
            return jsonify(result)
class Est_vitimas_estado(Resource):
    def get(self, sigla):
        try:
            result = f_hugo.estados_estado(vitimas,sigla)
        except:
            result = []
        finally:
            return jsonify(result)
class Est_vitimas_estado_datas(Resource):
    def get(self, sigla, data_inicio, data_fim):
        try:
            result = f_hugo.estados_estado_datas(vitimas,sigla, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)
class Est_vitimas_crime(Resource):
    def get(self, crime):
        try:
            result = f_hugo.estados_crime(vitimas, crime)
        except:
            result = []
        finally:
            return jsonify(result)
class Est_vitimas_crime_datas(Resource):
    def get(self, crime, data_inicio, data_fim):
        try:
            result = f_hugo.estados_crime_datas(vitimas, crime, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)
class Est_vitimas_estado_crime(Resource):
    def get(self, sigla, crime):
        try:
            result = f_hugo.estados_estado_crime(vitimas, sigla, crime)
        except:
            result = []
        finally:
            return jsonify(result)
class Est_vitimas_estado_crime_datas(Resource):
    def get(self, sigla, crime, data_inicio, data_fim):
        try:
            result = f_hugo.estados_estado_crime_datas(vitimas, sigla, crime, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)
class Municipios(Resource):
    def get(self):
        try:
            result = f_hugo.municipio()
        except:
            result = []
        finally:
            return jsonify(result)