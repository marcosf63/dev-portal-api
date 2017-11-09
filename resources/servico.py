#-*- coding: utf8 -*-
from flask_restful import Resource, request
from models.servico import ServicoModel

class Servico(Resource):
    def get(self, _id):
        servico = ServicoModel.buscar_por_id(_id)
        if servico:
            return servico.json()
        return {'mensagem': "Serviço não encontrado."}, 404

    def delete(self, _id):
       servico = ServicoModel.buscar_por_id(_id)
       if servico:
           servico.delete_from_db()

       return {'mensagem': "Serviço deletado com sucesso"}

class ServicoRegister(Resource):
    def post(self):
        data = request.get_json()

        servico = ServicoModel(**data)

        try:
            servico.save_to_db()
        except:
            return {"message": "Um erro cocorreu ao criar uma categoria"}, 500

        return servico.json(), 201

class ServicoQuery(Resource):
    """
      Para fazer busca em pagamentos do tipos /servico?categoria_id=1
    """
    def get(self):
        categoria_id = request.args.get('categoria_id')
        if categoria_id:
            servicos = ServicoModel.buscar_por_categoria(categoria_id)
            if servicos:
                return [servico.json() for servico in servicos]
            return {"mensagem": "Servicos não encontrados."}, 404
        
        nome = request.args.get('nome')
        if nome:
            servico = ServicoModel.buscar_por_nome(nome)
            if servico:
                return servico.json()
            return {"mensagem": "Servico não encontrado."}, 404

        return {"mensagem": "Informe algum parametro para consulta da categoria."}, 400
       

class ServicoList(Resource):
    def get(self):
        return {'servicos': [servico.json() for servico in ServicoModel.query.all()]}