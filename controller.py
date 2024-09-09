from view import *

class Controller:
    def __init__(self):
        self.view = {
            "home": HomeView(),
            "login": LoginView*(),
            "Register": RegisterView(),
            "Reset_pass": ResetpassView()
        }
        self.current.view = None

    def build(self, screen_name):
        if screen_name in self.views:
            self.current_view = self.views[screen_name]
            return self.current_view.render_screen()
        else:
            raise ValueError(f"Tela '{screen_name}' não encontrada!")
        
    def transition_to(self, screen_name):
        return self.build(screen_name)