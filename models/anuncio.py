from db import db

class AnuncioModel(db.Model):

    __tablename__ = 'servicosCadastrados'

    id = db.Column(db.Integer, primary_key=True)
    in_exibir = db.Column(db.Boolean)
    servico_cadastrado_id = db.Column(db.Integer, db.ForeignKey('servicosCadastrados.id'))
    servico_cadastrado = db.relationship('ServicosCadastradosModel', lazy='dynamic') # relacionamento 1 para 1


    def __init__(self, in_exibir, servico_id):
        self.in_exibir = in_exibir
        self.servico_cadastrado_id = servico_cadastrado_id


    def json(self):
        return {'servico_cadastrado': self.servico.json() }

    @classmethod
    def buscar_por_servico_id(cls, servico_cadastrado_id):
        return cls.query.filter_by(servico_cadastrado_id=servico_cadastrado_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()