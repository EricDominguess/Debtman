from view import *

class Controller:
    def __init__(self):
        self.views = {
            "home": HomeView(),
            "login": LoginView(),
            "register": RegisterView(),
            "reset_pass": ResetpassView()
        }
        self.current_view = self.views["login"]  # Define a view inicial

    def build(self, screen_name):
        if screen_name in self.views:
            self.current_view = self.views[screen_name]
            return self.current_view.render_screen()  # Retorna a tela renderizada
        else:
            raise ValueError(f"Tela '{screen_name}' não encontrada!")

    def transition_to(self, screen_name):
        """
        Faz a transição para uma nova tela.
        """
        return self.build(screen_name)
