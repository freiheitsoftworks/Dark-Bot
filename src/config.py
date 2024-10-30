# config.py
import os
from dotenv import load_dotenv
import secrets

# Carregar variáveis do arquivo .env
load_dotenv()

class Config:
    MONGODB_SETTINGS = {
        'host': os.getenv("MONGO_URI")  # Define o 'host' como a URI completa do MongoDB
    }
    SECRET_KEY = secrets.token_hex(16)  # Gera uma chave secreta aleatória
