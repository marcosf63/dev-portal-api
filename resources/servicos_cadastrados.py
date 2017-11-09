#-*- coding: utf8 -*-
from flask_restful import Resource, request
from models.servicos_cadastrados import ServicosCadastradosModel
from db import db

class ServicosCadastrados(Resource):
    def get(self, _id):
        servico_cadastrado = ServicosCadastradosModel.buscar_por_id(_id)
        if servico_cadastrado:
            return servico_cadastrado.json()
        return {'mensagem': "Serviço não encontrado."}, 404

    def delete(self, _id):
       servico_cadastrado = ServicosCadastradosModel.buscar_por_id(_id)
       if servico_cadastrado:
           servico_cadastrado.delete_from_db()

       return {'mensagem': "Serviço deletado com sucesso"}

class ServicosCadastradosRegister(Resource):
    def post(self):
        data = request.get_json()
        print data
        # if ServicosCadastradosModel.buscar_por_servico_id(data['servico_id']):
        #     return {'message': "Serviço já cadastrado."}, 400

        servico_cadastrado = ServicosCadastradosModel(**data)

        try:
            servico_cadastrado.save_to_db()
        except:
            return {"message": "Um erro cocorreu ao criar um servico"}, 500

        return servico_cadastrado.json(), 201

class ServicosCadastradosList(Resource):
    def get(self):
        servico_id = request.args.get('servico_id')
        if servico_id:
            servicos = ServicosCadastradosModel.query.filter_by(servico_id=servico_id).all()
            return {'servicos_cadastrados': [servico_cadastrado.json() for servico_cadastrado in servicos]}
        return {'servicos_cadastrados': [servico_cadastrado.json() for servico_cadastrado in ServicosCadastradosModel.query.all()]}