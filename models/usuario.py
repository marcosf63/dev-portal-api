from db import db

class UsuarioModel(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(20))
    tipo = db.Column(db.String(20)) # Prestador, Consumidor, Administrador
    endereco = db.Column(db.String(100))
    cidade = db.Column(db.String(80))
    cep = db.Column(db.String(10))
    telefoneFixo1 = db.Column(db.String(15))
    telefoneFixo2 = db.Column(db.String(15))
    celular1 = db.Column(db.String(15))
    celular2 = db.Column(db.String(15))
    foto = db.Column(db.String(50))
    situacao = db.Column(db.String(10))
    in_pf_pf = db.Column(db.String(2))
    cpf = db.Column(db.String(14))
    cnpj = db.Column(db.String(20))
    servicos_cadastrados = db.relationship('ServicosCadastradosModel', lazy='dynamic')
    contratos = db.relationship('ContratoModel', lazy='dynamic')

    #tipo, endereco, cidade, cep, telefoneFixo1, telefoneFixo2, celular1, celular2, foto, situacao, in_pf_pf, cpf, cnpj
    def __init__(
            self,
            nome,
            email, 
            senha,
            tipo,
            endereco,
            cidade,
            cep,
            telefoneFixo1,
            telefoneFixo2,
            celular1,
            celular2,
            foto,
            situacao,
            in_pf_pf,
        ):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo
        self.endereco = endereco
        self.cidade = cidade
        self.cep = cep
        self.telefoneFixo1 = telefoneFixo1
        self.telefoneFixo2 = telefoneFixo2
        self.celular1 = celular1
        self.celular2 = celular2
        self.foto = foto
        self.situacao = situacao
        self.in_pf_pf = in_pf_pf
        # self.cpf = cpf
        # self.cnpj = cnpj

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha,
            'tipo': self.tipo,
            'endereco': self.endereco,
            'cidade': self.cidade,
            'cep': self.cep,
            'telefoneFixo1': self.telefoneFixo1,
            'telefoneFixo2': self.telefoneFixo2,
            'celular1': self.celular1,
            'celular2': self.celular2,
            'foto': self.foto,
            'situacao': self.situacao,
            'in_pf_pf': self.in_pf_pf,
            'cpf': self.cpf,
            'cnpf': self.cnpj,
            'servicos_cadastrados': [
                servico_cadastrado.json() for servico_cadastrado in self.servicos_cadastrados.all()
            ],
            'contratos': [
                contrato.json() for contrato in self.contratos.all()
            ]
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def buscar_por_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def buscar_por_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def buscar_por_tipo(cls, tipo):
        return cls.query.filter_by(tipo=tipo).all()


