from fastapi import APIRouter, Depends
from models import Item
from database import create_item, get_items, update_item, delete_item
from auth import get_current_user

router = APIRouter()

@router.get("/items", tags=["Items"])
def read_items():
    """
    Lista todos os itens.
    Acesso permitido apenas com token presente.
    """
    return get_items()

@router.post("/items", tags=["Items"])
def create_new_item(item: Item):
    """
    Cria um novo item.
    Acesso permitido apenas com token presente.
    """
    return create_item(item)

@router.put("/items/{item_id}", tags=["Items"])
def update_existing_item(item_id: int, item: Item):
    """
    Atualiza um item existente.
    Acesso permitido apenas com token presente.
    """
    updated_item = update_item(item_id, item)
    if not updated_item:
        return {"error": "Item not found"}
    return updated_item

@router.delete("/items/{item_id}", tags=["Items"])
def delete_existing_item(item_id: int):
    """
    Deleta um item existente.
    Acesso permitido apenas com token presente.
    """
    delete_item(item_id)
    return {"message": "Item deleted"}
