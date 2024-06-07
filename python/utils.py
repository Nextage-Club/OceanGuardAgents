import os
from dotenv import load_dotenv, find_dotenv

# Arquivo de funcionalidades

# Função para carregar variáveis de ambiente a partir de um arquivo .env
def load_env():
    _ = load_dotenv(find_dotenv()) # Encontra e carrega o arquivo .env

# Função para obter a chave API do Google a partir das variáveis de ambiente
def get_google_api_key():
    load_env() # Carrega as variáveis de ambiente
    google_api_key = os.getenv('GOOGLE_API_KEY') # Obtém o valor da variável de ambiente 'GOOGLE_API_KEY'
    return google_api_key # Retorna a chave API do Google