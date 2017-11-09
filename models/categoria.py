from db import db

class CategoriaModel(db.Model):

    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    servicos = db.relationship('ServicoModel', lazy='dynamic')


    def __init__(self, nome):
        self.nome = nome

    def json(self):
        return {'id': self.id, 'name': self.nome, 'servicos': [ servico.json() for servico in self.servicos.all()]}

    @classmethod
    def buscar_por_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def buscar_por_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()
 
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()