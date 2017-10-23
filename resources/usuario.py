from flask_restful import Resource, reqparse
from models.usuario import UsuarioModel

class UsuarioRegister(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('nome',
        type=str,
        required=True,
        help="Este campo (nome) nao pode esta em branco."
    )
    parser.add_argument('email',
        type=str,
        required=True,
        help="Este campo (email) nao pode esta em branco."
    )
    parser.add_argument('senha',
        type=str,
        required=True,
        help="Este campo (senha) nao pode esta em branco."
    )

    def post(self):
        data = UsuarioRegister.parser.parse_args()

        if UsuarioModel.buscar_por_email(data['email']):
            return {"message": "Usuario ja existe"}, 400
       
        user = UsuarioModel(**data)
        user.save_to_db()

        return {"message": "Usuarios criado com sucesso"}, 201
     