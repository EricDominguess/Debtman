import flet as ft
from model import add_debit, get_database, get_debits

class LoginView:
    def __init__(self, controller):
        self.controller = controller

        def set_email(e):
            self.email = e.control.value

        def set_password(e):
            self.password = e.control.value

        self.email_field = ft.TextField(
            hint_text='Digite o seu email',
            width=300,
            height=40,
            border_radius=40,
            prefix_icon=ft.icons.PERSON,
            text_vertical_align=1,
            keyboard_type=ft.KeyboardType.EMAIL,
            on_change=set_email
        )
        self.password_field = ft.TextField(
            hint_text='Digite a sua senha',
            width=300,
            height=40,
            border_radius=40,
            prefix_icon=ft.icons.LOCK,
            text_vertical_align=1,
            password=True,
            can_reveal_password=True,
            keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
            on_change=set_password
        )

    def render_screen(self):
        self.email_field.value = ""
        self.password_field.value = ""

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
                                self.email_field,
                                self.password_field,
                                ft.ElevatedButton(
                                    text='Sign in',
                                    bgcolor=ft.colors.GREEN_500,
                                    on_hover=ft.colors.GREEN_400,
                                    width=300,
                                    height=40,
                                    on_click=self.on_sign_in_click
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

    def on_sign_in_click(self, e):
        email = self.email_field.value
        password = self.password_field.value
        self.controller.login_user(email, password)
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
class ResetpassViewInLog:
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
                                ft.ElevatedButton(
                                    text='Ir para Home',
                                    on_click=lambda e: self.controller.transition_to("home")
                                )
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
                        text='Atualizar Divida',
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
                        ),
                    ft.ElevatedButton(
                        text='Atualizar perfil',
                        bgcolor=ft.colors.GREEN_500,
                        on_hover=ft.colors.GREEN_400,
                        width=300,
                        height=40,
                        on_click=lambda e: self.controller.transition_to("Atualizar_Perfil")
                        ),
                    ft.ElevatedButton(
                        text='Logout',
                        bgcolor=ft.colors.RED_500,
                        on_click=lambda e: self.controller.logout() 
                    )
                ], horizontal_alignment='center', alignment='center')
            )
        ])
class RegistrarDiv:
    def __init__(self, controller):
        self.controller = controller

        # Definindo os campos de texto como atributos para acessar seus valores
        self.description_field = ft.TextField(
            hint_text='Descrição da Dívida',
            width=300,
            height=40,
            border_radius=40,
            prefix_icon=ft.icons.DESCRIPTION
        )
        self.amount_field = ft.TextField(
            hint_text='Valor da Dívida',
            width=300,
            height=40,
            border_radius=40,
            prefix_icon=ft.icons.MONEY,
            keyboard_type=ft.KeyboardType.NUMBER
        )
        self.due_date_field = ft.TextField(
            hint_text='Data de Vencimento',
            width=300,
            height=40,
            border_radius=40,
            prefix_icon=ft.icons.DATE_RANGE,
            keyboard_type=ft.KeyboardType.DATETIME
        )
        self.status_field = ft.TextField(
            hint_text='Situação da Dívida',
            width=300,
            height=40,
            border_radius=40,
            prefix_icon=ft.icons.DESCRIPTION
        )

    def render_screen(self):
        self.status_field.value = ""
        self.due_date_field.value = ""
        self.description_field.value = ""
        self.amount_field.value = ""
    
        return ft.Column([
            ft.Container(
                bgcolor=ft.colors.GREY_500,
                width=1910,
                height=820,
                border_radius=10,
                content=ft.Column([
                    ft.Text("Registrar Dívida", size=30, weight="bold"),
                    self.description_field,
                    self.amount_field,
                    self.due_date_field,
                    self.status_field,
                    ft.ElevatedButton(
                        text='Registrar Dívida',
                        bgcolor=ft.colors.GREEN_500,
                        on_hover=ft.colors.GREEN_400,
                        width=300,
                        height=40,
                        on_click=self.on_register_debt_click  
                    ),
                    ft.ElevatedButton(
                        text='Ir para Home',
                        on_click=lambda e: self.controller.transition_to("home")
                    )
                ], horizontal_alignment='center', alignment='center')
            )
        ])

    def on_register_debt_click(self, e):
        # Captura os valores dos campos
        description = self.description_field.value
        amount = self.amount_field.value
        due_date = self.due_date_field.value
        status = self.status_field.value

        # Envia as informações para o controller registrar a dívida
        self.controller.register_debt(description, amount, due_date, status)
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
                    ft.TextField(
                        hint_text='Situação Atualizada',
                        width=300,
                        height=40,
                        border_radius=40,
                        prefix_icon=ft.icons.DESCRIPTION
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
    def __init__(self, controller):
        self.controller = controller

    def render_screen(self):
        debits = self.controller.get_debits()  # Obtém as dívidas do controlador

        # Cria as linhas da tabela a partir dos dados das dívidas
        rows = [
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(debit['description'])),
                ft.DataCell(ft.Text(f"R$ {debit['amount']:.2f}")),
                ft.DataCell(ft.Text(debit['due_date'])),
                ft.DataCell(ft.Text(debit['status']))
            ])
            for debit in debits
        ]

        return ft.Column([
            ft.Container(
                bgcolor=ft.colors.GREY_500,
                width=1910,
                height=820,
                border_radius=10,
                content=ft.Column([
                    ft.Text("Tabela de Dívidas", size=30, weight="bold"),
                    # DataTable com dados reais
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("Descrição")),
                            ft.DataColumn(ft.Text("Valor")),
                            ft.DataColumn(ft.Text("Data de Vencimento")),
                            ft.DataColumn(ft.Text("Situação"))
                        ],
                        rows=rows
                    ),
                    ft.ElevatedButton(
                        text='Ir para Home',
                        on_click=lambda e: self.controller.transition_to("home")
                    )
                ], horizontal_alignment='center', alignment='center')
            )
        ])
class Perfil:
    def __init__(self, controller):
        self.controller = controller

    def render_screen(self):
        # Obtém o ID do usuário da sessão através do controlador
        user_id = self.controller.session.get('user_id')
        if not user_id:
            return ft.Column([ft.Text("Usuário não está logado.", size=20)])

        # Obtenha os detalhes do usuário a partir do banco de dados através do controlador
        user = self.controller.get_user_info(user_id)
        if not user:
            return ft.Column([ft.Text("Usuário não encontrado.", size=20)])

        # Exiba as informações do usuário
        return ft.Column([
            ft.Container(
                bgcolor=ft.colors.GREY_500,
                width=1910,
                height=820,
                border_radius=10,
                content=ft.Column([
                    ft.Text("Perfil do Usuário", size=30, weight="bold"),
                    ft.TextField(
                        value=user.get('first_name', ''),
                        hint_text='Primeiro Nome',
                        width=300,
                        height=40,
                        border_radius=40,
                        prefix_icon=ft.icons.PERSON,
                        read_only=True
                    ),
                    ft.TextField(
                        value=user.get('last_name', ''),
                        hint_text='Sobrenome',
                        width=300,
                        height=40,
                        border_radius=40,
                        prefix_icon=ft.icons.PERSON,
                        read_only=True
                    ),
                    ft.TextField(
                        value=user.get('email', ''),
                        hint_text='Email',
                        width=300,
                        height=40,
                        border_radius=40,
                        prefix_icon=ft.icons.EMAIL,
                        read_only=True
                    ),
                    ft.ElevatedButton(
                        text='Ir para Home',
                        on_click=lambda e: self.controller.transition_to("home")
                    )
                ], spacing=10, horizontal_alignment='center', alignment='center')
            )
        ])   
class AtualizarPerfil:
    def __init__(self, controller):
        self.controller = controller

    def render_screen(self):
        user = self.controller.get_user_info()
        
        if not user:
            return ft.Column([ft.Text("Usuário não está logado ou não encontrado.")])

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
                        prefix_icon=ft.icons.PERSON,
                        value=user.get('first_name', '')
                    ),
                    ft.TextField(
                        hint_text='Sobrenome',
                        width=300,
                        height=40,
                        border_radius=40,
                        prefix_icon=ft.icons.PERSON,
                        value=user.get('last_name', '')
                    ),
                    ft.TextField(
                        hint_text='Email',
                        width=300,
                        height=40,
                        border_radius=40,
                        prefix_icon=ft.icons.EMAIL,
                        value=user.get('email', '')
                    ),
                    ft.ElevatedButton(
                        text='Atualizar Perfil',
                        bgcolor=ft.colors.GREEN_500,
                        on_hover=ft.colors.GREEN_400,
                        width=300,
                        height=40,
                        on_click=lambda e: self.controller.update_user_profile(
                            first_name=self.first_name, 
                            last_name=self.last_name, 
                            email=self.email
                        )
                    ),
                    ft.ElevatedButton(
                        text='Alterar Senha',
                        bgcolor=ft.colors.BLUE_500,
                        on_hover=ft.colors.BLUE_400,
                        width=300,
                        height=40,
                        on_click=lambda e: self.controller.transition_to("reset_pass_loged")
                    ),
                    ft.ElevatedButton(
                        text='Ir para Home',
                        on_click=lambda e: self.controller.transition_to("home")
                    )
                ], spacing=10, horizontal_alignment='center', alignment='center')
            )
        ])