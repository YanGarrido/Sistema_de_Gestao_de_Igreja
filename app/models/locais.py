from configs.extensions import db
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Text

# Modelo da tabela Locais
class Local(db.Model):
    __tablename__ = 'locais'
    id_local: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    endereco: Mapped[str | None] = mapped_column(Text, nullable=True)  # Pode ser nulo
    capacidade: Mapped[int | None] = mapped_column(nullable=True)  # Pode ser nulo
    descricao: Mapped[str | None] = mapped_column(Text, nullable=True)  # Pode ser nulo

    def __init__(self, nome: str, endereco: str | None, capacidade: int | None, descricao: str | None):
        self.nome = nome
        self.endereco = endereco
        self.capacidade = capacidade
        self.descricao = descricao

    @staticmethod
    def get_todos_locais():
        locais = Local.query.all()
        for local in locais:
            print(f"ID: {local.id_local}, Nome: {local.nome}, Capacidade: {local.capacidade}")