import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Parâmetros para conexão com o banco de dados MySQL
db_user = "user"
db_password = "user_password"
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"

# URL da conexão para o banco de dados MySQL
DATABASE_URL = f"mysql+pymsql://{db_user}:{db_password}@{db_host}"