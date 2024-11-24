from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from routes import router

app = FastAPI()
app.include_router(router)

def detalhes_swagger():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Trabalho de Técnicas avançadas de Desenvolvimento de Software",
        version="1.0.0",
        description="API CRUD protegida com autenticação via Keycloak",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = detalhes_swagger

