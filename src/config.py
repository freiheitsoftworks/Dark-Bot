import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

class Config:
    MONGODB_SETTINGS = {
        'db': os.getenv("MONGO_URI")
    }