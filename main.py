import flet as ft
from controller import Controller
from view import MainView

def main(page: ft.Page):
    # Inicializando o controller e a view
    controller = Controller()
    main_view = MainView()

    # Configura o drawer da página
    page.navigation_drawer = main_view.render_drawer()

    # Renderiza a primeira tela (Login)
    current_view = controller.build("login")
    page.add(main_view.render_screen(current_view))

    # Função de callback para o clique no drawer
    def on_drawer_click(e):
        screen_name = e.control.label.lower().replace(" ", "_")
        controller.transition_to(screen_name)
        page.clean()  # Limpa a página para atualizar
        page.add(main_view.render_screen(controller.build(screen_name)))  # Atualiza com a nova tela

    # Associa os destinos do drawer ao clique
    for control in page.navigation_drawer.controls:
        if isinstance(control, ft.NavigationDrawerDestination):
            control.on_click = on_drawer_click

# Chamando a função principal do Flet
ft.app(target=main)
