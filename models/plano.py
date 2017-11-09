from db import db

class PlanoModel(db.Model):

    __tablename__ = 'planos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(4))
    descricao = db.Column(db.String(60))
    qt_servico = db.Column(db.Integer)
    periodicidade = db.Column(db.String(10))
    valor = db.Column(db.Float(precision=2))

    contratos = db.relationship('ContratoModel', lazy='dynamic')


    def __init__(self, nome, descricao, qt_servico, periodicidade, valor):
        self.nome = nome
        self.descricao = descricao
        self.qt_servico = qt_servico
        self.periodicidade = periodicidade
        self.valor = valor

    def json(self):
        return {'id': self.id,
                'nome': self.nome, 
                "descricao": self.descricao, 
                "qt_servico": self.qt_servico, 
                "periodicidade": self.periodicidade, 
                "valor": self.valor}

    @classmethod
    def buscar_por_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()

    @classmethod
    def buscar_por_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def buscar_por_parte_do_nome(cls, nome):
        str = nome + "%"
        return cls.query.filter(cls.nome.like(str)).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()