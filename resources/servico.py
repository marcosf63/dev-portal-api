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
        if ServicoModel.buscar_por_nome(data['nome']):
            return {'message': "Serviço '{}' já existe.".format(data['nome'])}, 400

        servico = ServicoModel(**data)

        try:
            servico.save_to_db()
        except:
            return {"message": "Um erro cocorreu ao criar uma categoria"}, 500

        return servico.json(), 201

class ServicoList(Resource):
    def get(self):
        return {'servicos': [servico.json() for servico in ServicoModel.query.all()]}