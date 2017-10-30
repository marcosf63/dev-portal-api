from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

#from security import authenticate, identity
#from resources.usuario import UsuarioRegister, Usuario, UsuarioList
from resources.servico import ServicoRegister, Servico, ServicoList
from resources.categoria import Categoria, CategoriaList, CategoriaRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
app.config['JWT_AUTH_PASSWORD_KEY'] = 'senha'
app.secret_key = 'marcos'
api = Api(app)


@app.cli.command()
def initdb():
  """Initialize the database."""
  from db import db
  db.init_app(app)
  db.create_all()

#jwt = JWT(app, authenticate, identity)

#api.add_resource(UsuarioRegister, '/register')
#api.add_resource(Usuario, '/usuario/<int:id>')
#api.add_resource(UsuarioList, '/usuarios' )
api.add_resource(CategoriaRegister, '/categoria')
api.add_resource(Categoria, '/categoria/<int:_id>')
api.add_resource(CategoriaList, '/categorias')
api.add_resource(ServicoRegister, '/servico')
api.add_resource(Servico, '/servico/<int:_id>')
api.add_resource(ServicoList, '/servicos')

if __name__ == '__main__':
  from db import db
  db.init_app(app)
  app.run(debug=True)
