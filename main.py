import flet as ft
from controller import Controller

def main(page: ft.Page):
    controller = Controller(page)
    controller.build()

if __name__ == "__main__":
    ft.app(target=main)
