from db import db

class ServicosCadastradosModel(db.Model):

    __tablename__ = 'servicosCadastrados'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(80))
    servico_id = db.Column(db.Integer, db.ForeignKey('servicos.id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    usuario_prestador = db.relationship('UsuarioModel')
    servico_cadastrado = db.relationship('ServicoModel')


    def __init__(self, descricao, servico_id, usuario_id):
        self.descricao = descricao
        self.servico_id = servico_id
        self.usuario_id = usuario_id

    def json(self):
        return {'descricao': self.descricao, 'servico': self.servico.name, 'usuario': self.usuario.name}

    @classmethod
    def buscar_por_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        