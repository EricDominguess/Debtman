import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window_maximized = True
    page.window_resizable = False

    def logar(e):
        page.remove(register)
        page.add(login)
        page.update()

    def registrar(e):
        page.remove(login)
        page.add(register)
        page.update()

    login = ft.Column([
        ft.Container(
            bgcolor = ft.colors.GREY_500,
            width = 1910,
            height = 1030,
            border_radius = 10,

            content= ft.Column([
                ft.Container(
                    bgcolor = ft.colors.GREEN_200,
                    width = 400,
                    height = 350,
                    border_radius = 10,

                    content = ft.Column([
                        ft.Container(
                            padding = ft.padding.only(
                                top = 10,
                                bottom = 32
                            ),   
                        
                            content = ft.Column([
                                ft.Text(
                                    value = 'Sign-In',
                                    weight = 'bold',
                                    size = 20
                                ) 
                            ])
                        ),

                        ft.Column([
                            ft.TextField(
                                hint_text = 'Digite o seu email',
                                width = 300,
                                height = 40,
                                border_radius = 40,
                                prefix_icon = ft.icons.PERSON,
                                text_vertical_align= 1,
                                keyboard_type = ft.KeyboardType.EMAIL
                            ),

                            ft.TextField(
                                hint_text = 'Digite a sua senha',
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
                                text = 'Sign in',
                                bgcolor = ft.colors.GREEN_500,
                                on_hover = ft.colors.GREEN_400,
                                width = 300,
                                height = 40
                            ),

                            ft.Row([
                                ft.TextButton('Esqueci minha Senha'),
                                ft.TextButton(
                                    text = 'Criar nova Conta',
                                    on_click = registrar)                   
                            ], width = 300, alignment = ft.MainAxisAlignment.SPACE_BETWEEN)

                        ], spacing = 10),

                        ft.Row([
                            ft.IconButton(icon = ft.icons.EMAIL),
                            ft.IconButton(icon = ft.icons.FACEBOOK),
                            ft.IconButton(icon = ft.icons.TELEGRAM)
                        ], alignment = 'center' )

                    ], horizontal_alignment = 'center')
                )

            ],horizontal_alignment = 'center', alignment = 'center')

        )
    ])

    register = ft.Column([       
        
        ft.Container(
            bgcolor = ft.colors.GREY_500,
            width = 1910,
            height = 1030,
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
                                ft.TextButton('Esqueci minha Senha'),
                                ft.TextButton(
                                    text = 'Já tenho uma Conta',
                                    on_click = logar)
                            ], width = 300, alignment = ft.MainAxisAlignment.SPACE_BETWEEN)

                        ], spacing = 8),
                    
                    ], horizontal_alignment = 'center')
                )

            ],horizontal_alignment = 'center', alignment = 'center')

        )
    ])

    page.add(login)

if __name__ == "__main__":
    ft.app(target=main)
