# auth.py
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import requests

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

KEYCLOAK_ISSUER = "https://tdsoft-auth.hsborges.dev/realms/trabalho-pratico"

def verificar_token(token: str = Depends(oauth2_scheme)):
    try:
        # Verifique se o token é válido no Keycloak
        response = requests.get(f"{KEYCLOAK_ISSUER}/protocol/openid-connect/userinfo", headers={"Authorization": f"Bearer {token}"})
        if response.status_code != 200:
            raise HTTPException(status_code=401, detail="Token inválido ou expirado.")
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=401, detail="Erro ao validar o token.")
