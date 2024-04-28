import flet as ft
from pages.login import LoginPage
from pages.registro import RegistroPage




def main(page: ft.Page):
  
   
    page.title = "CupertinoNavigationBar Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
 
   

    # Contenido inicial
    LoginPage(page)  # Página de exploración por defecto

ft.app(target=main)
