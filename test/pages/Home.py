import flet as ft
from .Profile import ProfilePage

def HomePage(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()
        
    def on_tab_change(event):
        selected_index = event.control.selected_index
        page.clean()
        if selected_index == 0:
            HomePage(page)
        elif selected_index == 1:
           ProfilePage(page)
        
    destinations = [
        ft.NavigationDestination(icon=ft.icons.TASK, label="Tareas"),
        ft.NavigationDestination(icon=ft.icons.PEOPLE, label="Perfil"),
         ft.NavigationDestination(icon=ft.icons.ADJUST, label="Configuracion"),
    ]
    page.navigation_bar = ft.CupertinoNavigationBar(
        bgcolor=ft.colors.BLUE_500,
        inactive_color=ft.colors.WHITE,
        active_color=ft.colors.BLACK,
        destinations=destinations,
        on_change=on_tab_change,
       
    )
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

