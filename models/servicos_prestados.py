from db import db

class ServicosPrestadosModel(db.Model):

    __tablename__ = 'servicosPrestados'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    avaliacao = db.Column(db.Integer)
    status = dbColum
    servico_cadastrado_id = db.Column(db.Integer, db.ForeignKey('servicosCadastrados.id'))
    servico_cadastrados = db.relationship('ServicosCadastradosModel')
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    usuario = db.relationship('UsuarioModel')


    def __init__(self, descricao, servico_id, usuario_id):
        self.descricao = descricao
        self.servico_id = servico_id
        self.servico_id = servico_id

    def json(self):
        return {'descricao': self.descricao, 'servico': self.servico.name, 'usuario': self.usuario.name}

    @classmethod
    def buscar_por_descricao(cls, servivo):
        return cls.query.filter_by(descricao.like('servivo')).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()