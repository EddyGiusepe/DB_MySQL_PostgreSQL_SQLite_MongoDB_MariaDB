from infra.configs.base import Base
from sqlalchemy import Column, Integer, String


class Filmes(Base):
    __tablename__ = "filmes"

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self): # Método de reprodução
        return f"Filme [titulo={self.titulo}, ano={self.ano}]"
