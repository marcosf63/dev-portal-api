from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from resources.usuario import UsuarioRegister, Usuario, UsuarioList
from models.pagamento import PagamentoModel
from models.contrato import ContratoModel
from models.plano import PlanoModel
from resources.servico import ServicoRegister, Servico, ServicoList, ServicoQuery
from resources.categoria import Categoria, CategoriaList, CategoriaRegister
from resources.servicos_cadastrados import ServicosCadastrados, ServicosCadastradosRegister, ServicosCadastradosList
from resources.plano import Plano, PlanoList, PlanoRegister
from resources.contrato import Contrato, ContratoList, ContratoRegister
from resources.pagamento import (
  Pagamento,
  PagamentoQuery,
  PagamentoRegister,
  PagamentoList
)
from resources.busca import Busca, BuscaList, BuscaRegister
from resources.servicos_prestados import ServicosPrestados
from resources.servicos_prestados import ServicosPrestadosRegister
from resources.servicos_prestados import ServicosPrestadosList
from resources.auth import UsuarioAuth


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
#app.config['JWT_AUTH_PASSWORD_KEY'] = 'senha'
app.config['JWT_SECRET_KEY'] = 'marcos'
jwt = JWTManager(app)
api = Api(app)


@app.cli.command()
def initdb():
  """Initialize the database."""
  from db import db
  db.init_app(app)
  db.create_all()

#jwt = JWT(app, authenticate, identity)

api.add_resource(UsuarioRegister, '/register')
api.add_resource(Usuario, '/usuario/<int:_id>')
api.add_resource(UsuarioList, '/usuarios' )
api.add_resource(CategoriaRegister, '/categoria')
api.add_resource(Categoria, '/categoria/<int:_id>')
api.add_resource(CategoriaList, '/categorias')
api.add_resource(ServicoRegister, '/servico')
api.add_resource(Servico, '/servico/<int:_id>')
api.add_resource(ServicoList, '/servicos')
api.add_resource(PlanoRegister, '/plano')
api.add_resource(Plano, '/plano/<int:_id>')
api.add_resource(PlanoList, '/planos')
api.add_resource(ContratoRegister, '/contrato')
api.add_resource(Contrato, '/contrato/<int:_id>')
api.add_resource(ContratoList, '/contratos')
api.add_resource(PagamentoRegister, '/pagamento')
api.add_resource(Pagamento, '/pagamento/<int:_id>')
api.add_resource(PagamentoList, '/pagamentos')
api.add_resource(PagamentoQuery, '/pagamento')
api.add_resource(BuscaRegister, '/busca')
api.add_resource(Busca, '/busca/<int:_id>')
api.add_resource(BuscaList, '/buscas')
api.add_resource(ServicosPrestadosRegister, '/servico_prestado')
api.add_resource(ServicosPrestados, '/servico_prestado/<int:_id>')
api.add_resource(ServicosPrestadosList, '/servicos_prestados')
api.add_resource(ServicosCadastradosRegister, '/servico_cadastrado')
api.add_resource(ServicosCadastrados, '/servico_cadastrado/<int:_id>')
api.add_resource(ServicosCadastradosList, '/servicos_cadastrados')
api.add_resource(UsuarioAuth, '/auth')
api.add_resource(ServicoQuery, '/servico')

if __name__ == '__main__':
  from db import db
  db.init_app(app)
  app.run(debug=True)
