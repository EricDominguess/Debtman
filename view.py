import flet as ft
class MainView:
    def render_drawer(self):
        drawer = ft.NavigationDrawer(
            bgcolor=ft.colors.GREEN_300,  # Cor do Drawer
            controls=[

                ft.Container(height = 50),
                ft.NavigationDrawerDestination(
                    icon = ft.icons.HOME,
                    label = "Home",
                ),
                ft.NavigationDrawerDestination(
                    icon = ft.icons.ATTACH_MONEY,
                    label = "Registrar Dívidas",
                ),
                ft.NavigationDrawerDestination(
                    icon = ft.icons.PRICE_CHECK,
                    label = "Registrar Pagamento",
                ),
                ft.NavigationDrawerDestination(
                    icon = ft.icons.MENU_BOOK_ROUNDED,
                    label = "Livro de Gastos",
                ),
                    ft.NavigationDrawerDestination(
                    icon = ft.icons.PERSON,
                    label = "Conta",
                ),
                ft.NavigationDrawerDestination(
                    icon = ft.icons.APARTMENT,
                    label = "Conta Empresarial",
                ),
                ft.NavigationDrawerDestination(
                    icon = ft.icons.MAN,
                    label = "Conta Pessoal",
                ),
                ft.NavigationDrawerDestination(
                    icon = ft.icons.LOGOUT,
                    label = "Logout",
                )
            ]
        )
        return drawer
    def render_screen(self, current_view):
        return current_view

class LoginView:
    def render_screen(self):
        # Estrutura da tela de login com Flet
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
                                padding=ft.padding.only(
                                    top=10,
                                    bottom=32
                                ),
                                content=ft.Column([
                                    ft.Text(
                                        value='Sign-In',
                                        weight='bold',
                                        size=20
                                    )
                                ])
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
                                        text='Esqueci minha Senha'),
                                    ft.TextButton(
                                        text='Criar nova Conta')
                                ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                            ], spacing=10),
                            ft.Row([
                                ft.IconButton(icon=ft.icons.EMAIL),
                                ft.IconButton(icon=ft.icons.FACEBOOK)
                            ], alignment='center')
                        ], horizontal_alignment='center')
                    )
                ], horizontal_alignment='center', alignment='center')
            )
        ])
        
        return login

class RegisterView:
    def render_screen(self):
        register = ft.Column([       
            
            ft.Container(
                bgcolor = ft.colors.GREY_500,
                width = 1910,
                height = 820,
                border_radius = 10,

                content= ft.Column([
                    ft.Container(
                        bgcolor = ft.colors.GREEN_200,
                        width = 400,
                        height = 450,
                        border_radius = 10,

                        content = ft.Column([
                            ft.Container(
                                padding = ft.padding.only(
                                    top = 10,
                                    bottom = 32
                                ),   
                            
                                content = ft.Column([
                                    ft.Text(
                                        value = 'Register',
                                        weight = 'bold',
                                        size = 20
                                    ) 
                                ])
                            ),

                            ft.Column([
                                ft.TextField(
                                    hint_text = 'Primeiro Nome',
                                    width = 300,
                                    height = 40,
                                    border_radius = 40,
                                    prefix_icon = ft.icons.PERSON,
                                    text_vertical_align= 1,
                                    keyboard_type = ft.KeyboardType.NAME
                                ),

                                ft.TextField(
                                    hint_text = 'Segundo nome',
                                    width = 300,
                                    height = 40,
                                    border_radius = 40,
                                    prefix_icon = ft.icons.PERSON,
                                    text_vertical_align= 1,
                                    keyboard_type = ft.KeyboardType.NAME
                                ),

                                ft.TextField(
                                    hint_text = 'Digite o seu email',
                                    width = 300,
                                    height = 40,
                                    border_radius = 40,
                                    prefix_icon = ft.icons.EMAIL,
                                    text_vertical_align= 1,
                                    keyboard_type = ft.KeyboardType.EMAIL
                                ),

                                ft.TextField(
                                    hint_text = 'Digite a senha',
                                    width = 300,
                                    height = 40,
                                    border_radius = 40,
                                    prefix_icon = ft.icons.LOCK,
                                    text_vertical_align= 1,
                                    password = True,
                                    can_reveal_password = True,
                                    keyboard_type = ft.KeyboardType.VISIBLE_PASSWORD
                                ),

                                ft.TextField(
                                    hint_text = 'Digite a senha novamente',
                                    width = 300,
                                    height = 40,
                                    border_radius = 40,
                                    prefix_icon = ft.icons.LOCK,
                                    text_vertical_align= 1,
                                    password = True,
                                    can_reveal_password = True,
                                    keyboard_type = ft.KeyboardType.VISIBLE_PASSWORD
                                ),

                                ft.ElevatedButton(
                                    text = 'Register',
                                    bgcolor = ft.colors.GREEN_500,
                                    on_hover = ft.colors.GREEN_400,
                                    width = 300,
                                    height = 40
                                ),

                                ft.Row([
                                    ft.TextButton(
                                        text ='Esqueci minha Senha'),
                                    ft.TextButton(
                                        text = 'Já tenho uma Conta')
                                ], width = 300, alignment = ft.MainAxisAlignment.SPACE_BETWEEN)

                            ], spacing = 8),
                        
                        ], horizontal_alignment = 'center')
                    )

                ],horizontal_alignment = 'center', alignment = 'center')

            )
        ])

        return register

class ResetpassView:
    def render_screen(self):
        Redefinir_senha = ft.Column([
            ft.Container(
                bgcolor = ft.colors.GREY_500,
                width = 1910,
                height = 820,
                border_radius = 10,

                content= ft.Column([
                    ft.Container(
                        bgcolor = ft.colors.GREEN_200,
                        width = 400,
                        height = 280,
                        border_radius = 10,

                        content = ft.Column([
                            ft.Container(
                                padding = ft.padding.only(
                                    top = 10,
                                    bottom = 25
                                ),   
                            
                                content = ft.Column([
                                    ft.Text(
                                        value = 'Recuperar Senha',
                                        weight = 'bold',
                                        size = 20
                                    ),
                                    ft.Text(
                                        value = 'Digite o Email registrado', 
                                        weight = 'bold',
                                        size = 15
                                    )

                                ],horizontal_alignment = 'center')
                            ),

                            ft.Column([
                                ft.TextField(
                                    hint_text = 'Digite seu email',
                                    width = 300,
                                    height = 40,
                                    border_radius = 40,
                                    prefix_icon = ft.icons.EMAIL,
                                    text_vertical_align= 1,
                                    keyboard_type = ft.KeyboardType.EMAIL
                                ),

                                ft.ElevatedButton(
                                    text = 'Send Email',
                                    bgcolor = ft.colors.GREEN_500,
                                    on_hover = ft.colors.GREEN_400,
                                    width = 300,
                                    height = 40
                                ),

                                ft.Row([
                                    ft.TextButton(
                                        text = 'Já tenho uma Conta'),
                                    ft.TextButton(
                                        text = 'Criar nova Conta')
                                ], width = 300, alignment = ft.MainAxisAlignment.SPACE_BETWEEN)

                            ], spacing = 10),
                        
                        ], horizontal_alignment = 'center')
                    )

                ],horizontal_alignment = 'center', alignment = 'center')

            )
        ])

        return Redefinir_senha

class HomeView:
    def render_screen(self):
        Home_page = ft.Column([
            ft.Container(
                bgcolor=ft.colors.GREY_500,
                width=1910,
                height=820,
                border_radius=10,

                # Definindo o conteúdo dentro do container
                content=ft.Column([
                    ft.Text("Bem-vindo à Home Page", size=30, weight="bold"),
                    ft.ElevatedButton("Abrir Drawer"),
                    # Outros componentes que quiser adicionar
                ], horizontal_alignment='center', alignment='center')
            )
        ])
        return Home_page
