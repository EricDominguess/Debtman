import flet as ft
from model import add_debit, get_database, get_debits

class MainEmpresa:
    def __init__(self,controller):
        self.controller = controller
    
    def render_screen(self):
        return ft.Column([
            ft.Text("Conta Empresarial", size=30, weight="bold"),
            # Colocar os componentes da tela Empresarial
            ft.ElevatedButton(
                text='Ir para Home',
                on_click=lambda e: self.controller.transition_to("home")
            )
        ])

class MainPessoal:
    def __init__(self,controller):
        self.controller = controller

    def render_screen(self):
        return ft.Column([
            ft.Text("Conta Pessoal", size=30, weight="bold"),
            # Colocar os componentes da tela Pessoal
            ft.ElevatedButton(
                text='Ir para Home',
                on_click=lambda e: self.controller.transition_to("home")
            )
        ])
class LoginView:
    def __init__(self,controller):
        self.controller = controller

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
                                        on_click=lambda e: self.controller.transition_to("reset_pass")
                                    ),
                                    ft.TextButton(
                                        text='Criar nova Conta',
                                        on_click=lambda e: self.controller.transition_to("register")
                                    )
                                ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                            ], spacing=10),
                            ft.Row([ft.IconButton(icon=ft.icons.EMAIL), ft.IconButton(icon=ft.icons.FACEBOOK)], alignment='center')
                        ], horizontal_alignment='center')
                    )
                ], horizontal_alignment='center', alignment='center')
            )
        ])
class RegisterView():
    def __init__(self, controller):
        self.controller = controller
        # Inicialize os campos como None
        self.first_name = None
        self.last_name = None
        self.email = None
        self.password = None
        self.confirm_password = None

    def render_screen(self):
        # Crie os componentes TextField e atribua-os aos atributos
        self.first_name = ft.TextField(
            hint_text='Primeiro Nome',
            width=300,
            height=40,
            border_radius=40,
            prefix_icon=ft.icons.PERSON,
            text_vertical_align=1,
            keyboard_type=ft.KeyboardType.NAME
        )
        self.last_name = ft.TextField(
            hint_text='Segundo nome',
            width=300,
            height=40,
            border_radius=40,
            prefix_icon=ft.icons.PERSON,
            text_vertical_align=1,
            keyboard_type=ft.KeyboardType.NAME
        )
        self.email = ft.TextField(
            hint_text='Digite o seu email',
            width=300,
            height=40,
            border_radius=40,
            prefix_icon=ft.icons.EMAIL,
            text_vertical_align=1,
            keyboard_type=ft.KeyboardType.EMAIL
        )
        self.password = ft.TextField(
            hint_text='Digite a senha',
            width=300,
            height=40,
            border_radius=40,
            prefix_icon=ft.icons.LOCK,
            text_vertical_align=1,
            password=True,
            can_reveal_password=True,
            keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD
        )
        self.confirm_password = ft.TextField(
            hint_text='Digite a senha novamente',
            width=300,
            height=40,
            border_radius=40,
            prefix_icon=ft.icons.LOCK,
            text_vertical_align=1,
            password=True,
            can_reveal_password=True,
            keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD
        )

        return ft.Column([
            ft.Container(
                bgcolor=ft.colors.GREY_500,
                width=1920,
                height=820,
                border_radius=10,
                content=ft.Column([
                    ft.Container(
                        bgcolor=ft.colors.GREEN_200,
                        width=400,
                        height=500,
                        border_radius=10,
                        content=ft.Column([
                            ft.Container(
                                padding=ft.padding.only(top=10, bottom=32),
                                content=ft.Text("Register", weight="bold", size=20)
                            ),
                            ft.Column([
                                self.first_name,
                                self.last_name,
                                self.email,
                                self.password,
                                self.confirm_password,
                                ft.Row([
                                    ft.TextButton(text='Esqueci minha Senha',
                                        on_click=lambda e: self.controller.transition_to("reset_pass")),
                                    ft.TextButton(text='Já tenho uma Conta',
                                        on_click=lambda e: self.controller.transition_to("reset_pass"))
                                ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                ft.ElevatedButton(
                                    text='Register',
                                    bgcolor=ft.colors.GREEN_500,
                                    on_hover=ft.colors.GREEN_400,
                                    width=300,
                                    height=40,
                                    on_click=self.register_user
                                ),
                            ], horizontal_alignment='center', spacing=8)
                        ], horizontal_alignment='center')
                    )
                ], horizontal_alignment='center', alignment='center')
            )
        ])

    def register_user(self, e):
        first_name = self.first_name.value
        last_name = self.last_name.value
        email = self.email.value
        password = self.password.value
        confirm_password = self.confirm_password.value

        if password != confirm_password:
            print("As senhas não coincidem.")
            return
        
        self.controller.register_user(
            first_name, last_name, email, password
        )
class ResetpassView:
    def __init__(self,controller):
        self.controller = controller

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
                                    ft.TextButton(text='Já tenho uma Conta',
                                        on_click=lambda e: self.controller.transition_to("login")),
                                    ft.TextButton(text='Criar nova Conta',
                                        on_click=lambda e: self.controller.transition_to("register"))
                                ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                            ], spacing=10)
                        ], horizontal_alignment='center')
                    )
                ], horizontal_alignment='center', alignment='center')
            )
        ])
class HomeView:
    def __init__(self,controller):
        self.controller = controller

    def render_screen(self):
        return ft.Column([
            ft.Container(
                bgcolor=ft.colors.GREY_500,
                width=1910,
                height=820,
                border_radius=10,
                content=ft.Column([
                    ft.Text("Bem-vindo à Home Page", size=30, weight="bold"),
                    ft.ElevatedButton(
                        text='Registrar Divida',
                        bgcolor=ft.colors.GREEN_500,
                        on_hover=ft.colors.GREEN_400,
                        width=300,
                        height=40,
                        on_click=lambda e: self.controller.transition_to("registrar_div")
                        ),
                    ft.ElevatedButton(
                        text='Atuzalizar Divida',
                        bgcolor=ft.colors.GREEN_500,
                        on_hover=ft.colors.GREEN_400,
                        width=300,
                        height=40,
                        on_click=lambda e: self.controller.transition_to("atualizar_div")
                        ),
                    ft.ElevatedButton(
                        text='Vizualizar Divida',
                        bgcolor=ft.colors.GREEN_500,
                        on_hover=ft.colors.GREEN_400,
                        width=300,
                        height=40,
                        on_click=lambda e: self.controller.transition_to("view_div")
                        ),
                    ft.ElevatedButton(
                        text='Perfil',
                        bgcolor=ft.colors.GREEN_500,
                        on_hover=ft.colors.GREEN_400,
                        width=300,
                        height=40,
                        on_click=lambda e: self.controller.transition_to("perfil")
                        )
                ], horizontal_alignment='center', alignment='center')
            )
        ])
class RegistrarDiv:
    def __init__(self,controller):
        self.controller = controller

    def render_screen(self):
        return ft.Column([
            ft.Container(
                bgcolor=ft.colors.GREY_500,
                width=1910,
                height=820,
                border_radius=10,
                content=ft.Column([
                    ft.Text("Registrar Dívida", size=30, weight="bold"),
                    # Form for registering debts
                    ft.TextField(
                        hint_text='Descrição da Dívida',
                        width=300,
                        height=40,
                        border_radius=40,
                        prefix_icon=ft.icons.DESCRIPTION
                    ),
                    ft.TextField(
                        hint_text='Valor da Dívida',
                        width=300,
                        height=40,
                        border_radius=40,
                        prefix_icon=ft.icons.MONEY,
                        keyboard_type=ft.KeyboardType.NUMBER
                    ),
                    ft.TextField(
                        hint_text='Data de Vencimento',
                        width=300,
                        height=40,
                        border_radius=40,
                        prefix_icon=ft.icons.DATE_RANGE,
                        keyboard_type=ft.KeyboardType.DATETIME
                    ),
                    ft.ElevatedButton(
                        text='Registrar Dívida',
                        bgcolor=ft.colors.GREEN_500,
                        on_hover=ft.colors.GREEN_400,
                        width=300,
                        height=40
                    ),
                    ft.ElevatedButton(
                        text='Ir para Home',
                        on_click=lambda e: self.controller.transition_to("home")
                    )
                ], horizontal_alignment='center', alignment='center')
            )
        ])
class AtualizarDiv:
    def __init__(self,controller):
        self.controller = controller

    def render_screen(self):
        return ft.Column([
            ft.Container(
                bgcolor=ft.colors.GREY_500,
                width=1910,
                height=820,
                border_radius=10,
                content=ft.Column([
                    ft.Text("Atualizar Dívida", size=30, weight="bold"),
                    # Form for updating debts
                    ft.TextField(
                        hint_text='Descrição da Dívida',
                        width=300,
                        height=40,
                        border_radius=40,
                        prefix_icon=ft.icons.DESCRIPTION
                    ),
                    ft.TextField(
                        hint_text='Valor Atualizado',
                        width=300,
                        height=40,
                        border_radius=40,
                        prefix_icon=ft.icons.MONEY,
                        keyboard_type=ft.KeyboardType.NUMBER
                    ),
                    ft.TextField(
                        hint_text='Nova Data de Vencimento',
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
                    ),
                    ft.ElevatedButton(
                        text='Ir para Home',
                        on_click=lambda e: self.controller.transition_to("home")
                    )
                ], horizontal_alignment='center', alignment='center')
            )
        ])
class ViewDiv:
    def __init__(self,controller):
        self.controller = controller

    def render_screen(self):
        # Placeholder for displaying registered debts
        return ft.Column([
            ft.Container(
                bgcolor=ft.colors.GREY_500,
                width=1910,
                height=820,
                border_radius=10,
                content=ft.Column([
                    ft.Text("Tabela de Dívidas", size=30, weight="bold"),
                    # DataTable placeholder without actual data
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("Descrição")),
                            ft.DataColumn(ft.Text("Valor")),
                            ft.DataColumn(ft.Text("Data de Vencimento"))
                        ],
                        rows=[
                            # Example row, replace with actual data rows
                            ft.DataRow(cells=[
                                ft.DataCell(ft.Text("Descrição da Dívida")),
                                ft.DataCell(ft.Text("R$ 0.00")),
                                ft.DataCell(ft.Text("00/00/0000"))
                            ])
                        ]
                    ),
                    ft.ElevatedButton(
                        text='Ir para Home',
                        on_click=lambda e: self.controller.transition_to("home")
                    )
                ], horizontal_alignment='center', alignment='center')
            )
        ])
class Perfil:
    def __init__(self,controller):
        self.controller = controller

    def render_screen(self):
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
                    ),
                    ft.ElevatedButton(
                        text='Ir para Home',
                        on_click=lambda e: self.controller.transition_to("home")
                    )
                ], horizontal_alignment='center', alignment='center')
            )
        ])