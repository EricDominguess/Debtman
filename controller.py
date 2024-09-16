# controller.py
import flet as ft
from view import *
from model import create_user, validate_login
from bson.objectid import ObjectId


class Controller:
    def __init__(self, page: ft.Page):
        self.page = page
        self.session = {}

        self.views = {
            "home": HomeView(self),
            "registrar_div": RegistrarDiv(self),
            "atualizar_div": AtualizarDiv(self),
            "view_div": ViewDiv(self),
            "perfil": Perfil(self),
            "login": LoginView(self),
            "register": RegisterView(self),
            "reset_pass": ResetpassView(self),
            "reset_pass_loged": ResetpassViewInLog(self),
            "Atualizar_Perfil": AtualizarPerfil(self)
        }
        self.current_view = self.views["home"]

    def logout(self):
        self.session.clear()
        print("Usuário deslogado com sucesso!")
        self.transition_to("login")

    def build(self, screen_name):
        if screen_name in self.views:
            view = self.views[screen_name]
            return view.render_screen()
        else:
            raise ValueError(f"Tela '{screen_name}' não encontrada!")

    def transition_to(self, screen_name):
        # Limpa a tela anterior e carrega a nova
        self.page.controls.clear()  # Limpa os controles existentes
        new_screen = self.build(screen_name)
        self.page.controls.append(new_screen)  # Adiciona a nova tela
        self.page.update()  # Atualiza a UI

    def register_user(self, first_name, last_name, email, password):
        # Aqui você pode adicionar a lógica para criar um novo usuário
        db = get_database()
        user_id = create_user(db, first_name, last_name, email, password)
        if user_id:
            # Sucesso no registro
            self.transition_to("login")
        else:
            self.transition_to("Register")

    def login_user(self, email, password):
        db = get_database()
        user = validate_login(db, email, password)  # Recebe o objeto do usuário validado
        if user:
            self.session['user_id'] = str(user['_id'])  # Armazena o ID do usuário na sessão
            print(f"Usuário logado com sucesso! ID: {self.session['user_id']}")
            self.transition_to("home")  # Redireciona para a tela principal
        else:
            print("Email ou senha incorretos.")
            self.transition_to("login")

    def register_debt(self, description, amount, due_date, status="pendente"):
        db = get_database()

        if 'user_id' not in self.session:
            print("Usuário não está logado")
            return

        try:
            debit_id = add_debit(db, amount, description, due_date, self.session['user_id'], status)
            if debit_id:
                print(f"Dívida registrada com sucesso, ID: {debit_id}")
                self.transition_to("home")
            else:
                print("Falha ao registrar a dívida.")
        except Exception as e:
            print(f"Erro ao registrar dívida: {e}")

    def get_debits(self):
        db = get_database()
        debits = get_debits(db)  # Obtém todas as dívidas do banco de dados
        print(f"Débitos obtidos: {debits}")  # Mensagem de depuração
        return debits
    
    def get_user_info(self):
        db = get_database()
        if 'user_id' in self.session:
            user = db['users'].find_one({"_id": ObjectId(self.session['user_id'])})
            return user
        return None
    
    def updated_first_name(self, first_name):
        self.first_name = first_name

    def updated_last_name(self, last_name):
        self.last_name = last_name

    def updated_email(self, email):
        self.email = email

    def update_user_profile(self, user_id):
        print(f"Atualizando perfil para o usuário: {user_id}")
        db = get_database()
        users_collection = db['users']
        update_result = users_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "email": self.email
            }}
        )
        if update_result.matched_count > 0:
            print("Perfil atualizado com sucesso!")
            self.transition_to("perfil")
        else:
            print("Erro ao atualizar perfil.")

    def get_user_info(self, user_id):
        db = get_database()
        users_collection = db['users']
        return users_collection.find_one({"_id": ObjectId(user_id)})