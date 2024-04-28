import flet as ft
from flet import *



def login (event):
    from .routers import Ruta
    Ruta(event.page, "Login")

def RegistroPage(page:ft.Page):
    page.title = "Registrar"

    name = TextField(label="Email")
    password = TextField(label="contraseña",password=True)
    Registrarboton = ElevatedButton(text="Registrar")
    loginboton = ElevatedButton(text="Login", on_click=login)

    registro_content = [
        ft.Column([
            
            ft.Row([name,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    
                   ), 
            
              ft.Row([password,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                   ), 
            
            
        ],
        
        
        alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row([
            Registrarboton,
            loginboton,
           
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        )
        
    ]

    for item in registro_content:
        page.add(ft.SafeArea(item))
