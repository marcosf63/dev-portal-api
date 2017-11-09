#-*- coding: utf8 -*-
from flask_restful import Resource, request
from models.servicos_prestados import ServicosPrestadosModel
from datetime import datetime
from db import db

class ServicosPrestados(Resource):
    def get(self, _id):
        servicos_prestados = ServicosPrestadosModel.buscar_por_id(_id)
        if servicos_prestados:
            return servicos_prestados.json()
        return {'mensagem': "Serviço não encontrado."}, 404

    def delete(self, _id):
       servicos_prestados = ServicosPrestadosModel.buscar_por_id(_id)
       if servicos_prestados:
           servicos_prestados.delete_from_db()

       return {'mensagem': "Serviço deletado com sucesso"}

    def put(self, _id):
       data = request.get_json()
       servico_prestado = ServicosPrestadosModel.buscar_por_id(_id)
       if servico_prestado:
           servico_prestado.avaliacao = data['avaliacao']
           servico_prestado.status = data['status']
           servico_prestado.save_to_db()
           return servico_prestado.json()

       return {'mensagem': "Serviço não encontrado."}


class ServicosPrestadosRegister(Resource):
    def post(self):
        data = request.get_json()
        data_do_servico = datetime.strptime(data['data'], '%d/%m/%Y')
        servicos_prestados = ServicosPrestadosModel(
            data_do_servico,
            data['status'],
            data['servico_cadastrado_id'],
            data['usuario_id'],
            data['avaliacao']
        )

        try:
            servicos_prestados.save_to_db()
        except:
            return {"message": "Um erro cocorreu ao criar uma categoria"}, 500

        return servicos_prestados.json(), 201

class ServicosPrestadosList(Resource):
    def get(self):
        usuario = request.args.get('usuario_id')
        prestador = request.args.get('prestador_id')
        if usuario:
            servicos_prestados = ServicosPrestadosModel.buscar_por_usuario_id(usuario)
            if servicos_prestados:
                return {'servicos_prestados': [sp.json() for sp in servicos_prestados]}
            return {'mensagem': 'Não há servicos a avaliar'}, 400
        if prestador:
            servicos_prestados_tmp = ServicosPrestadosModel.query.all()
            if servicos_prestados_tmp:
                return { 'servicos_prestados': [sp.json() for sp in servicos_prestados_tmp if sp.servico_cadastrado.usuario_id == int(prestador)]}
            return {'mensagem': 'Não há servicos a avaliar'}, 400
        return {'servicos_prestados': [servico_prestado.json() for servico_prestado in ServicosPrestadosModel.query.all()]}