import flet as ft
from controller import Controller

def main(page: ft.Page):
    controller = Controller(page)
    page.controls.append(controller.build("register"))
    page.update()

ft.app(target=main)