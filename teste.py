import flet as ft

def main(page: ft.Page):
    # Botão alinhado ao centro dentro do Container
    container_center = ft.Container(
        content=ft.ElevatedButton("Centralizado"),
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.colors.LIGHT_BLUE
    )
    
    # Botão alinhado à direita e no topo dentro do Container
    container_right_top = ft.Container(
        content=ft.ElevatedButton("Direita Topo"),
        alignment=ft.alignment.top_right,
        width=200,
        height=200,
        bgcolor=ft.colors.LIGHT_GREEN
    )
    
    # Botão com padding e margin dentro do Container
    container_custom = ft.Container(
        content=ft.ElevatedButton("Customizado"),
        padding=10,
        margin=20,
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.colors.GREEN
    )
    
    # Adiciona os containers na página
    page.add(container_center, container_right_top, container_custom)

ft.app(target=main)
