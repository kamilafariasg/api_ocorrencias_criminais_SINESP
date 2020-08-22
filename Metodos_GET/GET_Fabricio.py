from flask_restful import Resource
from flask import jsonify

import sys
sys.path.insert(0, '../Funcoes')

# Funcoes
from Funcoes.Fabricio import Fabricio
f_fabricio = Fabricio()

class metodo_get_fabricio(Resource):
    def get(self):
        result = f_fabricio.funcao_fabricio()
        return jsonify(result)
