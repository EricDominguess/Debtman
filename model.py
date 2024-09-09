import pymongo
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel:
    def __init__(self):
        # Conexão com o MongoDB
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client['meu_banco_de_dados']
        self.collection = self.db['usuarios']

    def create_user(self, first_name, last_name, email, password):
        # Criação de um novo usuário no banco de dados
        user = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": generate_password_hash(password)
        }
        self.collection.insert_one(user)

    def get_user(self, email):
        # Busca um usuário no banco de dados pelo email
        return self.collection.find_one({"email": email})

    def verify_password(self, password_input, stored_password_hash):
        # Verifica se a senha informada corresponde ao hash armazenado
        return check_password_hash(stored_password_hash, password_input)
