from configs.extensions import db
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, String, Text, Integer

from models.membros_ministerio import MembroMinisterio

# Modelo da tabela Ministerio
class Ministerio(db.Model):
    __tablename__ = 'ministerio'
    id_ministerio: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text, nullable=True)
    lider: Mapped[str | None] = mapped_column(String(100), nullable=True)

    membros = db.relationship('Membro', secondary='membro_ministerio', back_populates='ministerios')

    def __init__(self, nome: str, descricao: str | None, lider: str | None):
        self.nome = nome
        self.descricao = descricao
        self.lider = lider

  
    