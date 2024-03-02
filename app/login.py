import flet as ft
from useaction_table import create_table
import sqlite3
conn = sqlite3.connect("db/dbcad.db", check_same_thread= False)

def main(page: ft.Page):
    # create_table
    page.title = 'Login'
    page.bgcolor = '#2F6DE3'
    page.window_width = 500
    page.window_height = 300
    page.window_maximizable = True
    page.window_resizable = True
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.scroll = 'AUTO'
    
    def cadastro(e):
        try:
            c = conn.cursor()
            c.execute('INSER INTO users(email,senha) VALUES(?,?)',(email.value,senha.value))
            conn.commit()
            
        except Exception as es:
            print(e)
    
    
    def login(e):
        page.snack_bar = ft.SnackBar(
           ft.Text('Login realizado com sucesso'),
            bgcolor= 'green'
        )
        page.snack_bar.open = True
        page.update()
        
    email = ft.TextField(
                label= 'Digite seu email',
                width= 300,
                height= 50,
                text_align= 'Left',
                color= 'Black',
                border_radius= 15
                        )
    senha = ft.TextField(
                label= 'Digite sua senha',
                width= 300,
                height= 50,
                text_align= 'Left',
                color= 'Black',
                border_radius= 15,
                password= True,
                can_reveal_password= True
                        )
    dlg = ft.AlertDialog(
        title=ft.Text("Login realizado com sucesso!")
    )
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
                    email,
                    senha,
                ft.Container(
                    content= ft.Row(
                        alignment= 'center',
                        controls=[
                            ft.ElevatedButton(
                                text= 'Cadastrar',
                                width= 150,
                                height= 30,
                                on_click= cadastro
                            ),
                            ft.ElevatedButton(
                                text= 'Login',
                                width= 150,
                                height= 30,
                                on_click= login),
        ]
    )
)
                    ])))
    page.update()
ft.app(target=main)