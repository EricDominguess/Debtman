import flet as ft
from model import add_debit, get_database, get_debits

class MainEmpresa:
    def render_screen(self):
        return ft.Column([
            ft.Text("Conta Empresarial", size=30, weight="bold"),
            # Colocar os componentes da tela Empresarial
        ])

class MainPessoal:
    def render_screen(self):
        return ft.Column([
            ft.Text("Conta Pessoal", size=30, weight="bold"),
            # Colocar os componentes da tela Pessoal
        ])

class MainView(ft.Column):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.current_view = HomeView().render_screen()
        self.update_ui()

    def update_ui(self):
        self.controls = [
            self.render_drawer(),
            self.current_view
        ]
        self.update()

    def render_drawer(self):
        drawer = ft.NavigationDrawer(
            bgcolor=ft.colors.GREEN_300,
            controls=[
                ft.Container(height=50),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.HOME,
                    label="Home",
                    on_click=lambda _: self.controller.transition_to("home", self)
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.ATTACH_MONEY,
                    label="Registrar Dívidas",
                    on_click=lambda _: self.controller.transition_to("registrar_div", self)
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.PRICE_CHECK,
                    label="Registrar Pagamento",
                    on_click=lambda _: self.controller.transition_to("atualizar_div", self)
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.MENU_BOOK_ROUNDED,
                    label="Livro de Gastos",
                    on_click=lambda _: self.controller.transition_to("view_div", self)
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.PERSON,
                    label="Conta",
                    on_click=lambda _: self.controller.transition_to("perfil", self)
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.APARTMENT,
                    label="Conta Empresarial",
                    on_click=lambda _: self.controller.transition_to("main_empresa", self)
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.MAN,
                    label="Conta Pessoal",
                    on_click=lambda _: self.controller.transition_to("main_pessoal", self)
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.LOGOUT,
                    label="Logout",
                    on_click=lambda _: self.controller.transition_to("logout", self)
                )
            ]
        )
        return drawer

class LoginView:
    def render_screen(self):
        return ft.Column([
            ft.Container(
                bgcolor=ft.colors.GREY_500,
                width=1910,
                height=820,
                border_radius=10,
                content=ft.Column([
                    ft.Container(
                        bgcolor=ft.colors.GREEN_200,
                        width=400,
                        height=350,
                        border_radius=10,
                        content=ft.Column([
                            ft.Container(
                                padding=ft.padding.only(top=10, bottom=32),
                                content=ft.Text("Sign-In", weight="bold", size=20)
                            ),
                            ft.Column([
                                ft.TextField(
                                    hint_text='Digite o seu email',
                                    width=300,
                                    height=40,
                                    border_radius=40,
                                    prefix_icon=ft.icons.PERSON,
                                    text_vertical_align=1,
                                    keyboard_type=ft.KeyboardType.EMAIL
                                ),
                                ft.TextField(
                                    hint_text='Digite a sua senha',
                                    width=300,
                                    height=40,
                                    border_radius=40,
                                    prefix_icon=ft.icons.LOCK,
                                    text_vertical_align=1,
                                    password=True,
                                    can_reveal_password=True,
                                    keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD
                                ),
                                ft.ElevatedButton(
                                    text='Sign in',
                                    bgcolor=ft.colors.GREEN_500,
                                    on_hover=ft.colors.GREEN_400,
                                    width=300,
                                    height=40
                                ),
                                ft.Row([
                                    ft.TextButton(
                                        text='Esqueci minha Senha',
                                        on_click=lambda e: controller.transition_to("reset_pass")
                                    ),
                                    ft.TextButton(
                                        text='Criar nova Conta',
                                        on_click=lambda e: controller.transition_to("register")
                                    )
                                ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                            ], spacing=10),
                            ft.Row([ft.IconButton(icon=ft.icons.EMAIL), ft.IconButton(icon=ft.icons.FACEBOOK)], alignment='center')
                        ], horizontal_alignment='center')
                    )
                ], horizontal_alignment='center', alignment='center')
            )
        ])

class RegisterView:
    def render_screen(self):
        return ft.Column([
            ft.Container(
                bgcolor=ft.colors.GREY_500,
                width=1910,
                height=820,
                border_radius=10,
                content=ft.Column([
                    ft.Container(
                        bgcolor=ft.colors.GREEN_200,
                        width=400,
                        height=450,
                        border_radius=10,
                        content=ft.Column([
                            ft.Container(
                                padding=ft.padding.only(top=10, bottom=32),
                                content=ft.Text("Register", weight="bold", size=20)
                            ),
                            ft.Column([
                                ft.TextField(
                                    hint_text='Primeiro Nome',
                                    width=300,
                                    height=40,
                                    border_radius=40,
                                    prefix_icon=ft.icons.PERSON,
                                    text_vertical_align=1,
                                    keyboard_type=ft.KeyboardType.NAME
                                ),
                                ft.TextField(
                                    hint_text='Segundo nome',
                                    width=300,
                                    height=40,
                                    border_radius=40,
                                    prefix_icon=ft.icons.PERSON,
                                    text_vertical_align=1,
                                    keyboard_type=ft.KeyboardType.NAME
                                ),
                                ft.TextField(
                                    hint_text='Digite o seu email',
                                    width=300,
                                    height=40,
                                    border_radius=40,
                                    prefix_icon=ft.icons.EMAIL,
                                    text_vertical_align=1,
                                    keyboard_type=ft.KeyboardType.EMAIL
                                ),
                                ft.TextField(
                                    hint_text='Digite a senha',
                                    width=300,
                                    height=40,
                                    border_radius=40,
                                    prefix_icon=ft.icons.LOCK,
                                    text_vertical_align=1,
                                    password=True,
                                    can_reveal_password=True,
                                    keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD
                                ),
                                ft.TextField(
                                    hint_text='Digite a senha novamente',
                                    width=300,
                                    height=40,
                                    border_radius=40,
                                    prefix_icon=ft.icons.LOCK,
                                    text_vertical_align=1,
                                    password=True,
                                    can_reveal_password=True,
                                    keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD
                                ),
                                ft.ElevatedButton(
                                    text='Register',
                                    bgcolor=ft.colors.GREEN_500,
                                    on_hover=ft.colors.GREEN_400,
                                    width=300,
                                    height=40
                                ),
                                ft.Row([
                                    ft.TextButton(text='Esqueci minha Senha'),
                                    ft.TextButton(text='Já tenho uma Conta')
                                ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                            ], spacing=8)
                        ], horizontal_alignment='center')
                    )
                ], horizontal_alignment='center', alignment='center')
            )
        ])

class ResetpassView:
    def render_screen(self):
        return ft.Column([
            ft.Container(
                bgcolor=ft.colors.GREY_500,
                width=1910,
                height=820,
                border_radius=10,
                content=ft.Column([
                    ft.Container(
                        bgcolor=ft.colors.GREEN_200,
                        width=400,
                        height=280,
                        border_radius=10,
                        content=ft.Column([
                            ft.Container(
                                padding=ft.padding.only(top=10, bottom=25),
                                content=ft.Column([
                                    ft.Text("Recuperar Senha", weight='bold', size=20),
                                    ft.Text("Digite o Email registrado", weight='bold', size=15)
                                ], horizontal_alignment='center')
                            ),
                            ft.Column([
                                ft.TextField(
                                    hint_text='Digite seu email',
                                    width=300,
                                    height=40,
                                    border_radius=40,
                                    prefix_icon=ft.icons.EMAIL,
                                    text_vertical_align=1,
                                    keyboard_type=ft.KeyboardType.EMAIL
                                ),
                                ft.ElevatedButton(
                                    text='Send Email',
                                    bgcolor=ft.colors.GREEN_500,
                                    on_hover=ft.colors.GREEN_400,
                                    width=300,
                                    height=40
                                ),
                                ft.Row([
                                    ft.TextButton(text='Já tenho uma Conta'),
                                    ft.TextButton(text='Criar nova Conta')
                                ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                            ], spacing=10)
                        ], horizontal_alignment='center')
                    )
                ], horizontal_alignment='center', alignment='center')
            )
        ])

class HomeView:
    def render_screen(self):
        return ft.Column([
            ft.Container(
                bgcolor=ft.colors.GREY_500,
                width=1910,
                height=820,
                border_radius=10,
                content=ft.Column([
                    ft.Text("Bem-vindo à Home Page", size=30, weight="bold"),
                    ft.ElevatedButton("Abrir Drawer"),
                    # Outros componentes que quiser adicionar
                ], horizontal_alignment='center', alignment='center')
            )
        ])

class RegistrarDiv:
    def render_screen(self):
        dividas = add_debit(get_database())
        rows = [ft.DataRow(cells=[
            ft.DataCell(ft.Text(divida['description'])),
            ft.DataCell(ft.Text(f"R${divida['amount']}")),
            ft.DataCell(ft.Text(divida['due_date']))
        ]) for divida in dividas]

        return ft.Column([
            ft.Container(
                content=ft.DataTable(columns=[
                    ft.DataColumn(ft.Text("Descrição")),
                    ft.DataColumn(ft.Text("Valor")),
                    ft.DataColumn(ft.Text("Data Limite"))
                ], rows=rows),
                alignment='center'
            )
        ])

    def __init__(self):
        self.db = get_database

    def __init__(self):
        super().__init__()
        self.db = get_database
        self.update_table()

    def update_table(self):
        dividas = add_debit(self.db)
        rows = [ft.DataRow(cells=[
            ft.DataCell(ft.Text(divida['description'])),
            ft.DataCell(ft.Text(f"R$ {divida['amount']}")),
            ft.DataCell(ft.Text(divida['date'].strftime('%d/%m/%Y')))
        ]) for divida in dividas]
        self.content = ft.Column([
            ft.Text("Caderno de Dívidas", size=30, weight="bold"),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Descrição")),
                    ft.DataColumn(ft.Text("Valor")),
                    ft.DataColumn(ft.Text("Data"))
                ],
                rows=rows
            )
        ])
    
class AtualizarDiv:
    def render_screen(self):
        # Estrutura para a tela de Atualizar Dívida
        return ft.Column([
            ft.Container(
                bgcolor=ft.colors.GREY_500,
                width=1910,
                height=820,
                border_radius=10,
                content=ft.Column([
                    ft.Text("Atualizar Dívida", size=30, weight="bold"),
                    ft.TextField(
                        hint_text='Digite a descrição da dívida',
                        width=300,
                        height=40,
                        border_radius=40,
                        prefix_icon=ft.icons.DESCRIPTION
                    ),
                    ft.TextField(
                        hint_text='Digite o valor atualizado',
                        width=300,
                        height=40,
                        border_radius=40,
                        prefix_icon=ft.icons.MONEY,
                        keyboard_type=ft.KeyboardType.NUMBER
                    ),
                    ft.TextField(
                        hint_text='Digite a nova data de vencimento',
                        width=300,
                        height=40,
                        border_radius=40,
                        prefix_icon=ft.icons.DATE_RANGE,
                        keyboard_type=ft.KeyboardType.DATETIME
                    ),
                    ft.ElevatedButton(
                        text='Atualizar Dívida',
                        bgcolor=ft.colors.GREEN_500,
                        on_hover=ft.colors.GREEN_400,
                        width=300,
                        height=40
                    )
                ], horizontal_alignment='center', alignment='center')
            )
        ])
    
class ViewDiv:
    def render_screen(self):
        # Função correta para obter as dívidas do banco de dados
        dividas = get_debits(get_database())  # Ajuste para obter as dívidas já registradas
        
        rows = [ft.DataRow(cells=[
            ft.DataCell(ft.Text(divida['description'])),
            ft.DataCell(ft.Text(f"R$ {divida['amount']}")),
            ft.DataCell(ft.Text(divida['due_date'].strftime('%d/%m/%Y')))
        ]) for divida in dividas]

        return ft.Column([
            ft.Container(
                content=ft.Column([
                    ft.Text("Tabela de Dívidas", size=30, weight="bold"),
                    ft.DataTable(columns=[
                        ft.DataColumn(ft.Text("Descrição")),
                        ft.DataColumn(ft.Text("Valor")),
                        ft.DataColumn(ft.Text("Data de Vencimento"))
                    ], rows=rows)
                ]),
                alignment='center'
            )
        ])
class Perfil:
    def render_screen(self):
        # Estrutura para a tela do perfil do usuário
        return ft.Column([
            ft.Container(
                bgcolor=ft.colors.GREY_500,
                width=1910,
                height=820,
                border_radius=10,
                content=ft.Column([
                    ft.Text("Perfil do Usuário", size=30, weight="bold"),
                    ft.TextField(
                        hint_text='Primeiro Nome',
                        width=300,
                        height=40,
                        border_radius=40,
                        prefix_icon=ft.icons.PERSON
                    ),
                    ft.TextField(
                        hint_text='Sobrenome',
                        width=300,
                        height=40,
                        border_radius=40,
                        prefix_icon=ft.icons.PERSON
                    ),
                    ft.TextField(
                        hint_text='Email',
                        width=300,
                        height=40,
                        border_radius=40,
                        prefix_icon=ft.icons.EMAIL
                    ),
                    ft.ElevatedButton(
                        text='Atualizar Perfil',
                        bgcolor=ft.colors.GREEN_500,
                        on_hover=ft.colors.GREEN_400,
                        width=300,
                        height=40
                    ),
                    ft.ElevatedButton(
                        text='Alterar Senha',
                        bgcolor=ft.colors.BLUE_500,
                        on_hover=ft.colors.BLUE_400,
                        width=300,
                        height=40
                    )
                ], horizontal_alignment='center', alignment='center')
            )
        ])