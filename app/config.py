from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    keycloak_url: str = "http://localhost:8080/auth/"
    realm: str = "trabalho-pratico"
    client_id: str = "myclient"
    client_secret: str = "secret"
    algorithm: str = "RS256"

    class Config:
        env_file = ".env"

settings = Settings()
