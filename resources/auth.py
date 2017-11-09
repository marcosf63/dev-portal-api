#-*- coding: utf8 -*-
from flask_restful import Resource, request
from models.usuario import UsuarioModel
from flask_jwt_extended import create_access_token

class UsuarioAuth(Resource):
    def post(self):
        credenciais = request.get_json()
        if not credenciais:
            return {"mensagem": "Informe email e senha"}
        usuario = UsuarioModel.buscar_por_email(credenciais['email'])
        if not usuario:
            return {"mensagem": "Usuário nao existe."}

        if usuario.email == credenciais['email'] and usuario.senha == credenciais['senha']:
            return {
                'access_token': create_access_token(identity=usuario.email),
                'nome': usuario.nome,
                'tipo': usuario.tipo,
                'id': usuario.id
            }, 200
        return {'mensagem': "Usuario ou senha errada."}, 404