from werkzeug.security import safe_str_cmp
from models.usuario import UsuarioModel


def authenticate(email, senha):
    user = UsuarioModel.buscar_por_email(email)
    if user and safe_str_cmp(user.senha, senha):
        return user

def identity(payload):
    user_id = payload['identity']
    return UsuarioModel.buscar_por_id(user_id)