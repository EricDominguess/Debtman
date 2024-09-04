import flet as ft

def main(page: ft.Page):
    t = ft.Text(value = "Hello, World", color = "green")
    page.controls.append(t)
    page.update()

    page.add(
        ft.Row(controls= [
            ft.Text("A"),
            ft.Text("B"),
            ft.Text(value = "C", color = "blue")
        ])
    )

    def button_clicked(e):
        page.add(ft.Text("Clicked!"))

    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

    first_name = ft.TextField()
    last_name = ft.TextField()
    c = ft.Column(controls=[
        first_name,
        last_name
    ])
    c.disabled = False
    page.add(c)

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}!"))

    txt_name = ft.TextField(label="Your name")

    page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))

    def checkbox_changed(e):
        output_text.value = (
            f"You have learned how to ski :  {todo_check.value}."
        )
        page.update()

    output_text = ft.Text()
    todo_check = ft.Checkbox(label="To Do: Learn how to use ski", value=False, on_change=checkbox_changed)
    page.add(todo_check, output_text)

    def ok_clicked(e):
        print("OK clicked")
    
    def cancel_clicked(e):
        print("Cancel clicked")

    page.add(
        MyButton(text="OK", on_click=ok_clicked),
        MyButton(text="Cancel", on_click=cancel_clicked),
    )

    # Botão dentro de um container com alinhamento ao centro
    container_center = ft.Container(
        content=ft.Button("Centralizado"),
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.colors.LIGHT_BLUE
    )
    
    # Botão dentro de um container com alinhamento à direita e no topo
    container_right_top = ft.Container(
        content=ft.Button("Direita Topo"),
        alignment=ft.alignment.top_right,
        width=200,
        height=200,
        bgcolor=ft.colors.LIGHT_GREEN
    )
    
    # Botão dentro de um container com margem e padding personalizados
    container_custom = ft.Container(
        content=ft.Button("Customizado"),
        padding=ft.EdgeInsets(10),
        margin=ft.EdgeInsets.all(20),
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.colors.LIGHT_CORAL
    )

    page.add(container_center, container_right_top, container_custom)

class MyButton(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor = ft.colors.ORANGE_300
        self.color = ft.colors.GREEN_800
        self.text = text
        self.on_click = on_click