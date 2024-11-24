from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from routes import router

app = FastAPI()

# Incluindo as rotas
app.include_router(router)

# Documentação customizada
def custom_openapi():
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

app.openapi = custom_openapi
@app.get("/")
def read_root():
    return {"message": "API funcionando!"}
