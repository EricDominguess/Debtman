import flet as ft

def main(page: ft.Page):
    def on_change(e):
        selected_index = e.control.selected_index
        
        # Limpar o conteúdo da coluna antes de adicionar novo conteúdo
        content_column.controls.clear()
        
        # Exibir conteúdo baseado na seleção
        if selected_index == 0:
            content_column.controls.append(ft.Text("Conteúdo da primeira opção"))
        elif selected_index == 1:
            content_column.controls.append(ft.Text("Conteúdo da segunda opção"))
        elif selected_index == 2:
            # Adicionar DataTable na opção de configurações
            content_column.controls.append(
                ft.DataTable(
                    width=700,
                    bgcolor="white",
                    border=ft.border.all(2, "red"),
                    border_radius=10,
                    vertical_lines=ft.BorderSide(3, "blue"),
                    horizontal_lines=ft.BorderSide(1, "green"),
                    sort_column_index=0,
                    sort_ascending=True,
                    heading_row_color=ft.colors.BLACK12,
                    heading_row_height=100,
                    data_row_color={ft.ControlState.HOVERED: "0x30FF0000"},
                    show_checkbox_column=True,
                    divider_thickness=0,
                    column_spacing=200,
                    columns=[
                        ft.DataColumn(
                            ft.Text("Column 1"),
                            on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                        ),
                        ft.DataColumn(
                            ft.Text("Column 2"),
                            tooltip="This is a second column",
                            numeric=True,
                            on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                        ),
                    ],
                    rows=[
                        ft.DataRow(
                            [ft.DataCell(ft.Text("A")), ft.DataCell(ft.Text("1"))],
                            selected=True,
                            on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                        ),
                        ft.DataRow([ft.DataCell(ft.Text("B")), ft.DataCell(ft.Text("2"))]),
                    ],
                )
            )
        
        # Atualizar a coluna e a página
        content_column.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="First"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Second",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ],
        on_change=on_change,
        expand=True,  # Permite que o NavigationRail ocupe todo o espaço vertical disponível
    )

    content_column = ft.Column(
        expand=True,  # Permite que a coluna se expanda e ocupe o espaço disponível
    )

    # Organizar o layout em uma linha com o rail à esquerda e o conteúdo à direita
    page.add(
        ft.Row(
            [
                rail,
                content_column,
            ],
            expand=True  # Expande a linha para ocupar todo o espaço da página
        )
    )

    # Exibir o conteúdo inicial
    content_column.controls.append(ft.Text("Conteúdo da primeira opção"))
    page.update()

ft.app(target=main)
