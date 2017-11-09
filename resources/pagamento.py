#-*- coding: utf8 -*-
from flask_restful import Resource, request
from models.pagamento import PagamentoModel
from datetime import datetime

class Pagamento(Resource):
    def get(self, _id):
        pagamento = PagamentoModel.buscar_por_id(_id)
        if pagamento:
            return pagamento.json()
        return {'mensagem': "Pagamento não encontrado."}, 404

    def delete(self, _id):
       pagamento = PagamentoModel.buscar_por_id(_id)
       if pagamento:
           pagamento.delete_from_db()

       return {'mensagem': "Pagamento deletado com sucesso"}

class PagamentoQuery(Resource):
    """
      Para fazer busca em pagamentos do tipos /pagamento?mes=05
    """
    def get(self):
        mes = request.args.get('mes')
        if mes:
            pagamento = PagamentoModel.buscar_por_mes(mes)
            if pagamento:
                return pagamento.json()
            return {"mensagem": "Pagamento não encontrado."}, 404
        return {"mensagem": "Informe o mes do pagamento."}, 400

class PagamentoRegister(Resource):
    def post(self):
        data = request.get_json()
        data_pagamento = datetime.strptime(data['data'], '%d/%m/%Y')
        pagamento = PagamentoModel(data_pagamento, data['valor'], data['contrato_id'])

        try:
            pagamento.save_to_db()
        except:
            return {"message": "Um erro cocorreu ao criar um pagamento"}, 500

        return pagamento.json(), 201

class PagamentoList(Resource):
    def get(self):
        return {'pagamentos': [pagamento.json() for pagamento in PagamentoModel.query.all()]}