from fastapi import HTTPException, Security
from fastapi.security import OAuth2PasswordBearer

# Configurando o esquema de autenticação
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user():
    """
    Simples verificação da presença do token.
    Não valida o token, apenas verifica se foi enviado.
    """
    
    return {"message": "Token is valid (not validated in depth yet)"}
