from db import db
from sqlalchemy import extract

class PagamentoModel(db.Model):

    __tablename__ = 'pagamentos'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    valor = db.Column(db.Float)
    contrato_id = db.Column(db.Integer, db.ForeignKey('contratos.id'))
    contrato = db.relationship('ContratoModel')

    def __init__(self, data, valor, contrato_id):
        self.data = data
        self.valor = valor
        self.contrato_id = contrato_id

    def json(self):
        return {'data': str(self.data), 'valor': self.valor, 'contrato': self.contrato.json()}

    @classmethod
    def buscar_por_mes(cls, mes):
        return cls.query.filter(extract('month', cls.data) == mes).first()

    @classmethod
    def buscar_por_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()