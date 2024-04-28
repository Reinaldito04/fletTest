import flet as ft
from .Home import HomePage
from .registro import RegistroPage
from .login import LoginPage

def Ruta(page: ft.Page, ruta):

    page.clean()  # Limpiar el contenido existente

    if ruta == "Registro":
        RegistroPage(page)  # Mostrar la página de registro
    elif ruta == "Login":
        LoginPage(page)  # Mostrar la página de inicio de sesión
    elif ruta == "Home":
        HomePage(page)  # Mostrar la página principal
