from configs.extensions import db
from sqlalchemy.orm import Mapped

class MembroMinisterio(db.Model):
    __tablename__ = 'membro_ministerio'

    id_membro: Mapped[int] = db.Column(db.Integer, db.ForeignKey('membros.id_membro', ondelete='CASCADE'), primary_key=True)
    id_ministerio: Mapped[int] = db.Column(db.Integer, db.ForeignKey('ministerio.id_ministerio', ondelete='CASCADE'), primary_key=True)

    # Relacionamento inverso (membro e ministerio)
    membro = db.relationship('Membro', backref=db.backref('membro_ministerio', cascade="all, delete-orphan"))
    ministerio = db.relationship('Ministerio', backref=db.backref('membro_ministerio', cascade="all, delete-orphan"))