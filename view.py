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

    page.add(
        Task(text="Do laundry"),
        Task(text="Cook dinner"),
    )   

class Task(ft.Row):
    def __init__(self, text):
        super().__init__()
        self.text_view = ft.Text(text)
        self.text_edit = ft.TextField(text, visible=False)
        self.edit_button = ft.IconButton(icon=ft.icons.EDIT, on_click=self.edit)
        self.save_button = ft.IconButton(
            visible=False, icon=ft.icons.SAVE, on_click=self.save
        )
        self.controls = [
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button,
        ]

    def edit(self, e):
        self.edit_button.visible = False
        self.save_button.visible = True
        self.text_view.visible = False
        self.text_edit.visible = True
        self.update()

    def save(self, e):
        self.edit_button.visible = True
        self.save_button.visible = False
        self.text_view.visible = True
        self.text_edit.visible = False
        self.text_view.value = self.text_edit.value
        self.update()

class MyButton(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor = ft.colors.ORANGE_300
        self.color = ft.colors.GREEN_800
        self.text = text
        self.on_click = on_click