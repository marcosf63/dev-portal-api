from db import db

class ServicosCadastradosModel(db.Model):

    __tablename__ = 'servicosCadastrados'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(80))
    servico_id = db.Column(db.Integer, db.ForeignKey('servicos.id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    usuario_prestador = db.relationship('UsuarioModel')
    servico_cadastrado = db.relationship('ServicoModel')
    exibir_anuncio = db.Column(db.Boolean)


    def __init__(self, descricao, servico_id, usuario_id, exibir_anuncio):
        self.descricao = descricao
        self.servico_id = servico_id
        self.usuario_id = usuario_id
        self.exibir_anuncio = exibir_anuncio

    def json(self):
        return {
                    'id': self.id,
                    'exibir_anuncio': self.exibir_anuncio, 
                    'descricao': self.descricao, 
                    'servico': self.servico_cadastrado.nome, 
                    'usuario': self.usuario_prestador.nome,
                    'usuario_prestador_id': self.usuario_prestador.id,
                    'situacao_usuario': self.usuario_prestador.situacao,
                    'foto': self.usuario_prestador.foto,
                    'email': self.usuario_prestador.email,
                    'telefoneFixo1': self.usuario_prestador.telefoneFixo1,
                    'telefoneFixo2': self.usuario_prestador.telefoneFixo2,
                    'celular1': self.usuario_prestador.celular1,
                    'celular2': self.usuario_prestador.celular2
        }

    @classmethod
    def buscar_por_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def buscar_por_servico_id(cls, servico_id):
        return cls.query.filter_by(servico_id=servico_id).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        