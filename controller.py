import flet as ft
from view import *

class Controller:
    def __init__(self):
        self.views = {
            "home": HomeView(),
            "registrar_div": RegistrarDiv(),
            "atualizar_div": AtualizarDiv(),
            "view_div": ViewDiv(),
            "perfil": Perfil(),
            "main_empresa": MainEmpresa(),
            "main_pessoal": MainPessoal(),
        }
        self.current_view = self.views["home"]

    def build(self, screen_name):
        if screen_name in self.views:
            self.current_view = self.views[screen_name]
            return self.current_view  # Retorna a tela renderizada
        else:
            raise ValueError(f"Tela '{screen_name}' não encontrada!")

    def transition_to(self, screen_name, main_view):
        # Limpa a tela anterior e carrega a nova
        main_view.controls.clear()  # Limpa os controles existentes
        new_screen = self.build(screen_name)
        main_view.controls.append(main_view.render_drawer())  # Reinsere o drawer
        main_view.controls.append(new_screen)  # Adiciona a nova tela
        main_view.update()  # Atualiza a UI
