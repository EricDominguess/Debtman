from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId
import hashlib

# Simulação de uma sessão
session = {}

def get_database():
    CONNECTION_STRING = "mongodb+srv://user:pass@cluster.mongodb.net/myFirstDatabase"
    client = MongoClient(CONNECTION_STRING)
    return client['user_shopping_list']

def create_user(db, username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user = {
        "username": username,
        "password": hashed_password,
        "created_at": datetime.now()
    }
    users_collection = db['users']
    result = users_collection.insert_one(user)
    return result.inserted_id

def validate_login(db, username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users_collection = db['users']
    user = users_collection.find_one({"username": username, "password": hashed_password})
    if user:
        session['user_id'] = user['_id']  # Armazena o ID do usuário na sessão
        return True
    return False

def add_debit(db, amount, description, due_date):
    if 'user_id' not in session:
        raise Exception("Usuário não está logado")
    
    debit = {
        "user_id": session['user_id'],  # Associa o débito ao usuário logado
        "amount": amount,
        "description": description,
        "due_date": due_date,  # Adiciona a data de vencimento fornecida
        "created_at": datetime.now()  # Adiciona a data de criação da dívida
    }
    
    debits_collection = db['debits']
    result = debits_collection.insert_one(debit)
    return result.inserted_id

def get_debits(db):
    # Exemplo de consulta ao banco de dados para obter dívidas
    collection = db['debits']
    return list(collection.find())  # Retorna todas as dívidas

if __name__ == "__main__":   
    dbname = get_database()
    
    # Criar um novo usuário
    user_id = create_user(dbname, "username", "password123")
    print(f"User created with ID: {user_id}")
    
    # Validar login
    is_valid = validate_login(dbname, "username", "password123")
    print(f"Login válido: {is_valid}")
    
    if is_valid:
        # Inserir um débito
        debit_id = add_debit(dbname, 100, "Compra no supermercado")
        print(f"Debit inserted with ID: {debit_id}")
