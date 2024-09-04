import flet as ft

def main(page: ft.Page):
    # Define a altura e largura da página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Botão centralizado na janela do aplicativo
    central_button = ft.ElevatedButton(text="Centralizado")

    # Adiciona o botão diretamente na página
    page.add(central_button)

ft.app(target=main)
