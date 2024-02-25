import flet as ft
def main(page: ft.Page):
    page.title = 'Login'
    page.bgcolor = '#2F6DE3'
    page.window_width = 500
    page.window_height = 300
    page.window_maximizable = False
    page.window_resizable = False
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    
    page.add(
        ft.Container(
            width= 470,
            height= 240,
            bgcolor= 'WHITE',
            border_radius= 5,
            content= ft.Column(
                controls=[
                ft.TextField(
                    label= 'Digite seu email',
                    width= 300,
                    height= 50,
                    bgcolor= None,
                    text_align= 'Left',
                    color= 'Black',
                    ),
                ft.TextField(
                    label= 'Digite sua senha',
                    width= 300,
                    height= 50,
                    bgcolor= None,
                    text_align= 'Left',
                    color= 'Black'
                    ),
                ft.ElevatedButton(
                    text= 'Enter',
                    )
                    ])))
    page.update()
ft.app(target=main)