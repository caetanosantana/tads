# API de Gerenciamento de Itens

Este projeto é uma API simples para gerenciar itens, construída com **FastAPI**. A API permite listar, criar, atualizar e excluir itens.


##  Pré-requisitos

- Python 3.10 ou superior instalado.
- Biblioteca **pip** para gerenciamento de dependências.

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/caetanosantana/tads.git
   ```
2. **Vá ao diretório 'app'**:   
    ```bash
    cd app
    ```
2. **Utilize o comando pip para baixar as dependências**:
    ```bash
    pip install fastapi uvicorn pydantic
    ```

## Execução

1. **Inicie o cliente**:
    ```bash
    python -m fastapi dev main.py
    ```
2. **Acesse a documentação do Swagger** em:
   http://127.0.0.1:8000/docs
    