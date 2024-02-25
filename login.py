import flet as ft
cont = ft.Container(
        width= 470,
        height= 240,
        bgcolor= '#FFFFFF',
   )
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
        cont,
        ft.Row(
            controls=[
                ft.TextField(label='Digite seu email')
            ]
        ),
    )
    
    
    
    
    
    
    
    
    
    page.update()


ft.app(target=main)