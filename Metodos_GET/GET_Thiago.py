from flask_restful import Resource
from flask import jsonify

import sys
sys.path.insert(0, '../Funcoes')

# Funcoes
from Funcoes.Thiago import Thiago
f_thiago = Thiago()

class metodo_get_thiago(Resource):
    def get(self):
        result = f_thiago.funcao_thiago()
        return jsonify(result)
