from flask_restful import Resource
from flask import jsonify

import sys
sys.path.insert(0, '../Funcoes')

# Funcoes
from Funcoes.Alice import Alice
f_alice = Alice()

class metodo_get_alice(Resource):
    def get(self):
        result = f_alice.funcao_alice()
        return jsonify(result)
