from flask_restful import Resource
from flask import jsonify

import sys
sys.path.insert(0, '../Funcoes')

# Funcoes
from Funcoes.Renato import Renato
f_renato = Renato()

class metodo_get_renato(Resource):
    def get(self):
        try:
            result = f_renato.funcao_renato()
        except:
            result = []
        finally:
            return jsonify(result)