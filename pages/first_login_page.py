from dotenv import load_dotenv
import os
from utils import *
from supabase import create_client


load_dotenv()
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


class FirstLoginPage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            route='/first-login',
        )
        self.page = page

        self.login = MyTextField("Login", ft.icons.PERSON_OUTLINED, False, False, None)
        self.password = MyTextField("Mot de passe", ft.icons.LOCK_OUTLINED, True, True, None)
        self.confirm = MyTextField("Confirmer", ft.icons.LOCK_OUTLINED, True, True, None)
        self.connect_button = MyElevButton('Connecter', self.validate_user)
        self.go_to_landing_button = MyTextButton("Page de connexion", self.back_to_landing)

        self.infos_ct = ft.Column(
            controls=[
                ft.Text("Valider son compte".upper(), size=22, font_family="Poppins-Black"),
                ft.Divider(height=3, color=ft.colors.TRANSPARENT),
                ft.Text("Your informations Below", size=12),
                ft.Container(
                    padding=ft.padding.all(20), width=260,
                    border=ft.border.all(1, "#ebebeb"), border_radius=16,
                    content=ft.Column(
                        controls=[
                            self.login,
                            ft.Divider(height=1, thickness=1),
                            ft.Text("Choisir un mot de passe", size=12),
                            self.password, self.confirm,
                            ft.Divider(height=1, thickness=1),
                            self.connect_button, self.go_to_landing_button
                        ], spacing=20
                    )
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER
        )

        self.controls = [
            ft.Row(
                expand=True,
                controls=[
                    ft.Container(
                        expand=True, bgcolor="white", padding=50,
                        content=self.infos_ct
                    ),
                    ft.Container(
                        bgcolor=None, padding=50, expand=True,
                        content=ft.Image(src="../assets/plats/logo/Ovive LOGO.png", height=500, width=500)
                    ),
                ]
            )
        ]

    def validate_user(self, e):
        pass

    def back_to_landing(self, e):
        self.page.go('/')

