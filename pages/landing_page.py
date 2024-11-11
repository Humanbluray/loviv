import flet as ft
from dotenv import load_dotenv
import os
from utils import *
from supabase import create_client


load_dotenv()
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


class LandingPage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            route="/",
        )
        self.page = page

        self.login = MyTextField("Login", ft.icons.PERSON_OUTLINED, False, False, None)
        self.password = MyTextField("Mot de passe", ft.icons.LOCK_OUTLINED, True, True, None)
        self.connect_button = MyElevButton('Connecter', self.connect)
        self.first_login_button = MyTextButton("Première connexion", self.go_to_first_login_page)

        self.infos_ct =  ft.Column(
            controls=[
                ft.Text("Connexion".upper(), size=22, font_family="Poppins-Black"),
                ft.Divider(height=3, color=ft.colors.TRANSPARENT),
                ft.Text("Your informations Below", size=12),
                ft.Container(
                    padding=ft.padding.all(20),
                    border_radius=16,
                    content=ft.Column(
                        controls=[
                            self.login, self.password, self.connect_button, self.first_login_button
                        ], spacing=20
                    )
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER
        )

        self.controls = [
            ft.Row(
                expand=True,
                controls=[
                    ft.Card(
                        elevation=10, clip_behavior=ft.ClipBehavior.HARD_EDGE,
                        content=ft.Container(padding=10, border_radius=16, content=self.infos_ct)
                    ),
                    ft.Image(src="../assets/plats/logo/Ovive LOGO.png", height=350, width=350)
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND
            )
        ]

    def connect(self, e):
        self.page.go("/welcome")
        # users = supabase.table("users").select("login, password").execute()
        # count = 0
        #
        # for couple in users.data:
        #     if (couple['login'], couple["password"]) == (self.login.value, self.password.value):
        #         count += 1
        #
        # if count == 0:
        #     print("not connected")
        # else:
        #     print("connected")

    def go_to_first_login_page(self, e):
        self.page.go('/first-login')

