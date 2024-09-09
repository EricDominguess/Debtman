import flet as ft

class View:
    def __init__(self, page, controller):
        self.page = page
        self.controller = controller
        self.page.horizontal_alignment = 'center'
        self.page.vertical_alignment = 'center'
        self.page.window_maximized = True
        self.page.window_resizable = False

    def display_login(self):
        # Define o layout da tela de login
        login = ft.Column([
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
                                content=ft.Text(value='Sign-In', weight='bold', size=20)
                            ),
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
                                on_click=lambda e: self.controller.logar(
                                    email=self.page.controls[0].content.controls[1].value,  # Email field
                                    password=self.page.controls[0].content.controls[2].value  # Password field
                                ),
                                width=300,
                                height=40
                            ),
                            ft.Row([
                                ft.TextButton(
                                    text='Esqueci minha Senha',
                                    on_click=lambda e: self.display_redefinir_senha()
                                ),
                                ft.TextButton(
                                    text='Criar nova Conta',
                                    on_click=lambda e: self.controller.registrar(e)  # Aqui vai para o registro
                                )
                            ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                        ], horizontal_alignment='center')
                    )
                ], horizontal_alignment='center', alignment='center')
            )
        ])

        self.page.controls.clear()
        self.page.add(login)
        self.page.update()

    def display_register(self):
        # Define o layout da tela de registro
        register = ft.Column([
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
                                content=ft.Text(value='Register', weight='bold', size=20)
                            ),
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
                                hint_text='Segundo Nome',
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
                                on_click=lambda e: self.controller.realizar_registro(
                                    first_name=self.page.controls[0].content.controls[1].value,  # Primeiro nome
                                    last_name=self.page.controls[0].content.controls[2].value,   # Segundo nome
                                    email=self.page.controls[0].content.controls[3].value,      # Email
                                    password=self.page.controls[0].content.controls[4].value    # Senha
                                ),
                                width=300,
                                height=40
                            ),
                            ft.Row([
                                ft.TextButton(
                                    text='Já tenho uma Conta',
                                    on_click=lambda e: self.display_login()
                                )
                            ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                        ], horizontal_alignment='center')
                    )
                ], horizontal_alignment='center', alignment='center')
            )
        ])

        self.page.controls.clear()
        self.page.add(register)
        self.page.update()

    def display_redefinir_senha(self):
        # Define o layout da tela de redefinição de senha
        redefinir_senha = ft.Column([
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
                            ft.Text(value='Recuperar Senha', weight='bold', size=20),
                            ft.Text(value='Digite o Email registrado', weight='bold', size=15),
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
                                on_click=lambda e: self.controller.enviar_email_reset(),
                                width=300,
                                height=40
                            ),
                            ft.Row([
                                ft.TextButton(
                                    text='Já tenho uma Conta',
                                    on_click=lambda e: self.display_login()
                                ),
                                ft.TextButton(
                                    text='Criar nova Conta',
                                    on_click=lambda e: self.controller.registrar(e)
                                )
                            ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                        ], spacing=10, horizontal_alignment='center')
                    )
                ], horizontal_alignment='center', alignment='center')
            )
        ])

        self.page.controls.clear()
        self.page.add(redefinir_senha)
        self.page.update()

    def display_home_page(self):
        # Define o layout da home page
        home_page = ft.Column([
            ft.Container(
                bgcolor=ft.colors.GREY_500,
                width=1910,
                height=820,
                border_radius=10,
                content=ft.Column([
                    ft.Text("Bem-vindo à Home Page", size=30, weight="bold"),
                    # Outros componentes que quiser adicionar
                ], horizontal_alignment='center', alignment='center')
            )
        ])

        self.page.controls.clear()
        self.page.add(home_page)
        self.page.update()

    def show_message(self, title, message):
        # Exibir mensagem na interface
        dlg = ft.AlertDialog(title=ft.Text(title), content=ft.Text(message), on_dismiss=lambda e: self.page.update())
        self.page.dialog = dlg
        dlg.open = True
        self.page.update()
