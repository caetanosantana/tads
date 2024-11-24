from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    id: int
    userId: int
    nome: str
    descricao: str

database: List[Item] = [
    Item(id=1, userId=101, nome="Espada", descricao="Aumenta o dano do jogador"),
    Item(id=2, userId=102, nome="Escudo", descricao="Aumenta a defesa do jogador"),
]

def create_item(item: Item):
    for existing_item in database:
        if existing_item.id == item.id:
            raise ValueError("Já existe um item com este ID.")
    database.append(item)
    return item

def get_items():
    return database

def update_item(item_id: int, item_data: Item):
    for index, item in enumerate(database):
        if item.id == item_id:
            database[index] = item_data
            return item_data
    return None

def delete_item(item_id: int):
    global database
    database = [item for item in database if item.id != item_id]
    return True
