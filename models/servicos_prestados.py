#-*- coding: utf8 -*-
from db import db
from sqlalchemy import and_

class ServicosPrestadosModel(db.Model):

    __tablename__ = 'servicosPrestados'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    avaliacao = db.Column(db.Integer)
    status = db.Column(db.String) # Em negociação, Em execução, Excluído, Finalizado  
    servico_cadastrado_id = db.Column(db.Integer, db.ForeignKey('servicosCadastrados.id'))
    servico_cadastrado = db.relationship('ServicosCadastradosModel')
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    usuario = db.relationship('UsuarioModel')


    def __init__(self, data, status, servico_cadastrado_id, usuario_id, avaliacao):
        self.data = data
        self.status = status
        self.servico_cadastrado_id = servico_cadastrado_id
        self.usuario_id = usuario_id
        self.avaliacao = avaliacao

    def json(self):
        return {'id': self.id, 'data': str(self.data), 'status': self.status, 'servico': self.servico_cadastrado.json(), 'usuario': self.usuario.nome, 'usuario_id': self.usuario_id, 'avalicao': self.avaliacao}

    @classmethod
    def buscar_por_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def buscar_por_usuario_id(cls, _id):
        return cls.query.filter(and_(cls.usuario_id == _id, cls.status==u"Em execução"))

    # @classmethod
    # def buscar_por_prestador_id(cls, prestador_id):
    #     return cls.query.all().filter(cls.servico_cadastrado.usuario_id==prestador_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()