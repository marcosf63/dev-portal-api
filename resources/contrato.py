#-*- coding: utf8 -*-
from flask_restful import Resource, request
from models.contrato import ContratoModel
from datetime import datetime

class Contrato(Resource):
    def get(self, _id):
        contrato = ContratoModel.buscar_por_id(_id)
        if contrato:
            return contrato.json()
        return {'mensagem': "Contrato não encontrado."}, 404

    def delete(self, _id):
       contrato = ContratoModel.buscar_por_id(_id)
       if contrato:
           contrato.delete_from_db()

       return {'mensagem': "Contrato deletado com sucesso"}

class ContratoRegister(Resource):
    def post(self):
        data = request.get_json()
        contrato = ContratoModel(data['plano_id'], data['usuario_id'], data['dia_vencimento'])

        try:
            contrato.save_to_db()
        except:
            return {"message": "Um erro cocorreu ao criar um contrato"}, 500

        return contrato.json(), 201

class ContratoList(Resource):
    def get(self):
        return {'contratos': [contrato.json() for contrato in ContratoModel.query.all()]}