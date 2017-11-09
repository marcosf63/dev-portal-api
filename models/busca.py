from db import db

class BuscaModel(db.Model):

    __tablename__ = 'buscas'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    servico_id = db.Column(db.Integer, db.ForeignKey('servicos.id'))
    servico = db.relationship('ServicoModel')


    def __init__(self, data, servico_id):
        self.data = data
        self.servico_id = servico_id

    def json(self):
        return {'data': str(self.data), 'servico': self.servico.json()}

    @classmethod
    def buscar_por_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()