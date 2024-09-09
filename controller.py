from model import UserModel
from view import View
import flet as ft

class Controller:
    def __init__(self, page):
        self.page = page
        self.user_model = UserModel()
        self.view = View(page, self)  # Chama a view e passa a referência do controller
        self.build()

    def build(self):
        # Desenha a tela inicial de login
        self.view.display_login()

    def realizar_registro(self, first_name, last_name, email, password):
        if not first_name or not last_name or not email or not password:
            self.page.snack_bar = ft.SnackBar(ft.Text("Todos os campos são obrigatórios."))
            self.page.snack_bar.open = True
            self.page.update()
        else:
            try:
                self.user_model.create_user(first_name, last_name, email, password)
                self.page.snack_bar = ft.SnackBar(ft.Text("Conta criada com sucesso!"))
                self.page.snack_bar.open = True
                self.page.update()
                self.view.display_login()  # Volta para a tela de login após o registro
            except Exception as e:
                self.page.snack_bar = ft.SnackBar(ft.Text(f"Erro ao criar conta: {e}"))
                self.page.snack_bar.open = True
                self.page.update()

    def logar(self, email, password):
        user = self.user_model.get_user(email)
        if user and self.user_model.verify_password(password, user["password"]):
            self.page.snack_bar = ft.SnackBar(ft.Text("Login efetuado com sucesso."))
            self.page.snack_bar.open = True
            self.page.update()
            self.view.display_home_page()  # Vai para a home page após o login
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Email ou senha incorretos."))
            self.page.snack_bar.open = True
            self.page.update()
