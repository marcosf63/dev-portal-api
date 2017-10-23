from db import db

class ContratoModel(db.Model):

    __tablename__ = 'contratos'

    id = db.Column(db.Integer, primary_key=True)
    data_inicio = db.Column(db.Date)
    data_vencimento = db.Column(db.Date)

    plano_id = db.Column(db.Integer, db.ForeignKey('planos.id'))
    plano = db.relationship('PlanoModel')

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    usuario = db.relationship('UsuarioModel')


    def __init__(self, plano_id, usuario_id,data_vencimento ):
        self.plano_id = plano_id
        self.usuario_id = usuario_id
        self.data_vencimento = data_vencimento

    def json(self):
        return {'usuario': self.usuario.nome, 'plano': self.plano.nome, 'data_inicio': self.data_inicio, 'data_vencimento': self.data_vencimento}

    @classmethod
    def buscar_por_data_vencimento(cls, data_vencimento):
        return cls.query.filter_by(data_vencimento=data_vencimento).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()