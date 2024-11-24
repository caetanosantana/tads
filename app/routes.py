from fastapi import APIRouter, HTTPException
from database import Item, create_item, get_items, update_item, delete_item

router = APIRouter()

@router.get("/")
def root():
    return {"message": "API funcionando!"}

@router.get("/items", tags=["Itens"])
def exibir_items():
    return get_items()

@router.post("/itens", tags=["Itens"])
def criar_item(item: Item):
    try:
        return create_item(item)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/itens/{item_id}", tags=["Itens"])
def atualizar_item(item_id: int, item: Item):
    updated_item = update_item(item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item não encontrado.")
    return updated_item

@router.delete("/itens/{item_id}", tags=["Itens"])
def deletar_item(item_id: int):
    if not any(item.id == item_id for item in get_items()):
        raise HTTPException(status_code=404, detail="Item não encontrado.")
    delete_item(item_id)
    return {"mensagem": "Item deletado com sucesso."}
