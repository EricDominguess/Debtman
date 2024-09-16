# controller.py
import flet as ft
from view import *
from model import create_user

class Controller:
    def __init__(self, page: ft.Page):
        self.page = page

        self.views = {
            "home": HomeView(self),
            "registrar_div": RegistrarDiv(self),
            "atualizar_div": AtualizarDiv(self),
            "view_div": ViewDiv(self),
            "perfil": Perfil(self),
            "main_empresa": MainEmpresa(self),
            "main_pessoal": MainPessoal(self),
            "login": LoginView(self),
            "register": RegisterView(self),
            "reset_pass": ResetpassView(self)
        }
        self.current_view = self.views["home"]

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