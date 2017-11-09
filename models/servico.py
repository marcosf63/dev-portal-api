from db import db

class ServicoModel(db.Model):

    __tablename__ = 'servicos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'))
    categoria = db.relationship('CategoriaModel')


    def __init__(self, nome, categoria_id):
        self.nome = nome
        self.categoria_id = categoria_id

    def json(self):
        return {'id': self.id, 'nome': self.nome }

    @classmethod
    def buscar_por_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def buscar_por_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()

    @classmethod
    def buscar_por_categoria(cls, categoria_id):
        return cls.query.filter_by(categoria_id=categoria_id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        