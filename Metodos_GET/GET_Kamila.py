from flask_restful import Resource
from flask import jsonify

import sys
sys.path.insert(0, '../Funcoes')

# Funcoes
from Funcoes.Kamila import Kamila
f_kamila = Kamila()

class metodo_get_kamila(Resource):
    def get(self):
        try:
            result = f_kamila.funcao_kamila()
        except:
            result = []
        finally:
            return jsonify(result)