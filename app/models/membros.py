from configs.extensions import db, login_manager
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Text, Date
from datetime import date
from flask_login import UserMixin
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

from models.membros_ministerio import MembroMinisterio

# Modelo da tabela Membros
class Membro(db.Model, UserMixin):
    __tablename__ = 'membros'
    id_membro: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)  # Email único e opcional
    telefone: Mapped[str | None] = mapped_column(String(20), nullable=True)  # Telefone opcional
    endereco: Mapped[str | None] = mapped_column(Text, nullable=True)  # Endereço opcional
    data_nascimento: Mapped[date | None] = mapped_column(nullable=True)  # Data de nascimento opcional
    data_entrada: Mapped[date | None] = mapped_column(nullable=True)  # Data de entrada opcional
    senha: Mapped[str] = mapped_column(String(255), nullable=False)
    
    ministerios = db.relationship('Ministerio', secondary='membro_ministerio', back_populates='membros')
    

    def __init__(self,nome: str, email: str, telefone: str, endereco: str, data_nascimento: Date, data_entrada: Date, senha: str):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.data_nascimento = data_nascimento
        self.data_entrada = data_entrada
        self.senha = senha

    def set_password(self, senha):
        self.senha = generate_password_hash(senha)

    def check_password(self, senha):
        return check_password_hash(self.senha, senha)
    
    @classmethod
    def find_user_by_email(cls,email):
        return Membro.query.filter_by(email = email).first()
    
    def create_user(self):
        db.session.add(self)
        db.session.commit()

    def get_id(self):
        return str(self.id_membro)


    def user_to_dict(self):
        return {
            "id": self.id_membro,
            "email": self.email
        }
    

    
    