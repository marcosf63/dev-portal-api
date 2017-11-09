#-*- coding: utf8 -*-
from flask_restful import Resource, request
from models.plano import PlanoModel

class Plano(Resource):
    def get(self, _id):
        plano = PlanoModel.buscar_por_id(_id)
        if plano:
            return plano.json()
        return {'mensagem': "Plano não encontrada."}, 404

    def delete(self, _id):
       plano = PlanoModel.buscar_por_id(_id)
       if plano:
           plano.delete_from_db()

       return {'mensagem': "Plano deletada com sucesso"}

class PlanoRegister(Resource):
    def post(self):
        data = request.get_json()
        if PlanoModel.buscar_por_nome(data['nome']):
            return {'message': "Plano ja existe."}, 400

        plano = PlanoModel(**data)

        try:
            plano.save_to_db()
        except:
            return {"message": "Um erro cocorreu ao criar uma categoria"}, 500

        return plano.json(), 201


class PagamentoQuery(Resource):
    """
      Para fazer busca em plano do tipos /plano_?mes=05
    """
    def get(self):
        mes = request.args.get('mes')
        if mes:
            pagamento = PagamentoModel.buscar_por_mes(mes)
            if pagamento:
                return pagamento.json()
            return {"mensagem": "Pagamento não encontrado."}, 404
        return {"mensagem": "Informe o mes do pagamento."}, 400

class PlanoList(Resource):
    def get(self):
        nome_like = request.args.get('nome_like')
        if nome_like:
            return {'planos': [plano.json() for plano in PlanoModel.buscar_por_parte_do_nome(nome_like)]} 
        
        return {'planos': [plano.json() for plano in PlanoModel.query.all()]}