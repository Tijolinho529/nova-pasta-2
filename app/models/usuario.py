from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base
from config.connection import db

Base = declarative_base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(250))
    email = Column(String(250))
    senha = Column(String(250))

# Definindo atributos da classe
    def __init__(self, nome: str, email: str, senha: str) -> None
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco
Base.me

















































