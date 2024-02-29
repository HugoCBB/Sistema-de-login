import flet as ft

def main(page: ft.Page):
    page.title = 'Login'
    page.bgcolor = '#2F6DE3'
    page.window_width = 500
    page.window_height = 300
    page.window_maximizable = True
    page.window_resizable = True
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    dlg = ft.AlertDialog(
        title=ft.Text("Login realizado com sucesso!")
    )
    def login(e):
        page.dialog = dlg
        dlg.open = True
        page.update()
        
    page.add(
        ft.Container(
            width= 470,
            height= 240,
            bgcolor= 'WHITE',
            border_radius= 5,
            content= ft.Column(
                horizontal_alignment= 'center',
                alignment= 'center',
                controls= [
                    ft.TextField(
                        label= 'Digite seu email',
                        width= 300,
                        height= 50,
                        text_align= 'Left',
                        color= 'Black',
                        border_radius= 15
                        ),
                        
                    ft.TextField(
                        label= 'Digite sua senha',
                        width= 300,
                        height= 50,
                        text_align= 'Left',
                        color= 'Black',
                        border_radius= 15,
                        password= True,
                        can_reveal_password= True
                        ),
                    ft.ElevatedButton(
                        text= 'Login',
                        on_click= login
                    )
                    ])))
    page.update()
ft.app(target=main)