#-*- coding: utf8 -*-
from flask_restful import Resource, request
from models.usuario import UsuarioModel

class Usuario(Resource):
    def get(self, _id):
        usuario = UsuarioModel.buscar_por_id(_id)
        if usuario:
            return usuario.json()
        return {'mensagem': "usuario não encontrada."}, 404

    def delete(self, _id):
       usuario = UsuarioModel.buscar_por_id(_id)
       if usuario:
           usuario.delete_from_db()

       return {'mensagem': "usuario deletada com sucesso"}

class UsuarioRegister(Resource):
    def post(self):
        data = request.get_json()
        if UsuarioModel.buscar_por_email(data['email']):
            return {'message': "Email '{}' ja existe.".format(data['email'])}, 400

        usuario = UsuarioModel(**data)

        try:
            usuario.save_to_db()
        except:
            return {"message": "Um erro cocorreu ao criar um usuario"}, 500

        return usuario.json(), 201

class UsuarioList(Resource):
    def get(self):
        tipo = request.args.get('tipo')
        if tipo:
            return {'usuarios': [usuario.json() for usuario in UsuarioModel.buscar_por_tipo(tipo)]}
        return {'usuarios': [usuario.json() for usuario in UsuarioModel.query.all()]}