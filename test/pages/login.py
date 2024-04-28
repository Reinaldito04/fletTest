import flet as ft







def logear(event):
    # Aquí puedes realizar la lógica de autenticación
    # Por ejemplo, puedes verificar si el usuario y la contraseña son válidos
    nombre = inputUser.value
    password = txt_password.value
    if (nombre =="reinaldo" and password=="1234"):
        from .routers import Ruta
        print("logeado")
        Ruta(event.page, "Home")
    else:
        print("datos erroneos")

def registro(event):
        from .routers import Ruta
        Ruta(event.page, "Registro")
    
inputUser = ft.TextField(label="Usuario", text_align=ft.TextAlign.START, border_radius=15,
                         height=50,
                         tooltip="Ingrese su usuario para logear",
                         width=500,
                         )
txt_password = ft.TextField(label="Contraseña", text_align=ft.TextAlign.START, border_radius=15,
                            height=50,
                            width=500,
                            tooltip="Ingrese su contraseña para logear",
                            )
botonLogin = ft.ElevatedButton(text="ingresar",
                               width=150,
                               height=50,
                               bgcolor="blue",
                               color="white",
                               # Llama a la función logear con los valores de usuario y con
                               on_click=logear,
                               )
botonRegistro = ft.ElevatedButton(text="Registrar",
                                  width=150,
                                  height=50,
                                  bgcolor="pink",
                                  color="white",
                                  on_click=registro,
                                  )


def LoginPage(page: ft.Page):
    page.title = "Login"

    login_content = [
        ft.Column([

            ft.Row([inputUser,
                    ],
                   alignment=ft.MainAxisAlignment.CENTER,

                   ),

            ft.Row([txt_password,
                    ],
                   alignment=ft.MainAxisAlignment.CENTER,
                   ),


        ],


            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row([
            botonLogin,
            botonRegistro,
        ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    ]

    for item in login_content:
        page.add(ft.SafeArea(item))
