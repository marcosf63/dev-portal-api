from db import db

class PagamentoModel(db.Model):

    __tablename__ = 'pagamentos'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    valor = db.Column(db.Float(precision=2))

    contrato_id = db.Column(db.Integer, db.ForeignKey('contratos.id'))
    contrato = db.relationship('ContratoModel')


    def __init__(self, data, ):
        self.data = data
        self.valor = valor
        self.contrato_id = contrato_id

    def json(self):
        return {'data': self.data, 'valor': self.valor, 'prestador': self.contrato.usuario.nome}

    @classmethod
    def buscar_pagamentos_por_mes(cls, mes):
        #implementar esta funcao para recuperar os pagamentos por mes
        return cls.query.filter_by(mes=mes).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()