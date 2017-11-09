#-*- coding: utf8 -*-
from flask_restful import Resource, request
from models.busca import BuscaModel
from datetime import datetime
from db import db

class Busca(Resource):
    def get(self, _id):
        busca = BuscaModel.buscar_por_id(_id)
        if busca:
            return busca.json()
        return {'mensagem': "Busca não encontrado."}, 404

    def delete(self, _id):
       busca = BuscaModel.buscar_por_id(_id)
       if busca:
           busca.delete_from_db()

       return {'mensagem': "Busca deletado com sucesso"}

class BuscaRegister(Resource):
    def post(self):
        data = request.get_json()
        data_da_busca = datetime.strptime(data['data'], '%d/%m/%Y')

        busca = BuscaModel(data_da_busca, data['servico_id'])

        try:
            busca.save_to_db()
        except:
            return {"message": "Um erro cocorreu ao criar uma busca"}, 500

        return busca.json(), 201

class BuscaList(Resource):
    def get(self):
        dado = request.args.get('contagem')
        if dado:
            buscas = db.session.execute(
                'select count(buscas.servico_id) as qt , buscas.servico_id, servicos.nome from buscas, servicos where buscas.servico_id = servicos.id group by servico_id order by qt desc'
            ).fetchall()
            return {'buscas': [ {'servico': busca[2], 'quantidade': busca[0]} for busca in buscas]}
        return {'buscas': [busca.json() for busca in BuscaModel.query.all()]}