import flet as ft


def ProfilePage(page: ft.Page):
    page.title = "Profile"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    imagen = ft.Image(src=f"https://i.pinimg.com/736x/c6/cf/83/c6cf83c46420bc65b423a788dbe3eb8e.jpg",
                      height=500, width=500, fit=ft.ImageFit.CONTAIN

                      )

    page.add(
        ft.Column(
            [ft.Row([
                imagen
                 ],
                    alignment=ft.MainAxisAlignment.CENTER,),
                ft.Row([
                    ft.Text("HGola", size=16),
                ],
                       alignment=ft.MainAxisAlignment.CENTER,
                       ),

                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        

    )
