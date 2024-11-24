from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    keycloak_url: str = "http://localhost:8080/auth/"
    realm: str = "trabalho-pratico"
    client_id: str = "myclient"
    client_secret: str = "secret"
    algorithm: str = "RS256"

    db_user: str = "postgres"
    db_password: str = "postgres"
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "tadsbanco"

    class Config:
        env_file = ".env"
    @property
    def database_url(self) -> str:
        """ Retorna a URL de conexão com o banco de dados
        """
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
settings = Settings()
