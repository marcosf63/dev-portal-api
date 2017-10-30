#-*- coding: utf8 -*-
from flask_restful import Resource, request
from models.categoria import CategoriaModel

class Categoria(Resource):
    def get(self, _id):
        categoria = CategoriaModel.buscar_por_id(_id)
        if categoria:
            return categoria.json()
        return {'mensagem': "Categoria não encontrada."}, 404

    def delete(self, _id):
       categoria = CategoriaModel.buscar_por_id(_id)
       if categoria:
           categoria.delete_from_db()

       return {'mensagem': "Categoria deletada com sucesso"}

class CategoriaRegister(Resource):
    def post(self):
        data = request.get_json()
        if CategoriaModel.buscar_por_nome(data['nome']):
            return {'message': "Store '{}' ja existe.".format(data['nome'])}, 400

        categoria = CategoriaModel(**data)

        try:
            categoria.save_to_db()
        except:
            return {"message": "Um erro cocorreu ao criar uma categoria"}, 500

        return categoria.json(), 201

class CategoriaList(Resource):
    def get(self):
        return {'categorias': [categoria.json() for categoria in CategoriaModel.query.all()]}