from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId
import bcrypt

def get_database():
    CONNECTION_STRING = "mongodb://localhost:27017/"
    client = MongoClient(CONNECTION_STRING)
    return client['debitman']

def create_user(db, first_name, last_name, email, password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": hashed_password,
        "created_at": datetime.now()
    }
    users_collection = db['users']
    result = users_collection.insert_one(user)
    return result.inserted_id

def validate_login(db, email, password):
    users_collection = db['users']
    user = users_collection.find_one({"email": email})  # Verifica pelo campo de email
    if user and bcrypt.checkpw(password.encode(), user['password']):
        return user  # Retorna o objeto user completo se o login for válido
    return None  # Retorna None se o login for inválido


def add_debit(db, amount, description, due_date, user_id, status="pendente"):
    try:
        due_date = datetime.strptime(due_date, "%d/%m/%Y")
    except ValueError:
        raise Exception("Data de vencimento inválida")

    debit = {
        "user_id": user_id,
        "amount": float(amount),
        "description": description,
        "due_date": due_date,
        "status": status,
        "created_at": datetime.now()
    }
    
    debits_collection = db['debits']
    result = debits_collection.insert_one(debit)
    print(f"Dívida inserida com ID: {result.inserted_id}")  # Adicione este print
    return result.inserted_id


def get_debits(db):
    collection = db['debits']
    debits = list(collection.find())  # Obtém todas as dívidas
    for debit in debits:
        debit['due_date'] = debit['due_date'].strftime("%d/%m/%Y")  # Formata a data
    return debits

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
