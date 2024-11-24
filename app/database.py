# Banco de dados em memória para simplificar
database = []

def create_item(item):
    database.append(item)
    return item

def get_items():
    return database

def update_item(item_id, item_data):
    for index, item in enumerate(database):
        if item.id == item_id:
            database[index] = item_data
            return item_data
    return None

def delete_item(item_id):
    global database
    database = [item for item in database if item.id != item_id]
    return True
