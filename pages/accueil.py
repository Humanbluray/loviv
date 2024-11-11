import datetime
import time
from pages.menu import plats
from utils import *
from pages.headers import HeaderMenu


class Welcome(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, route="/welcome",
        )
        self.page = page
        self.menu_ct = ft.Container(
            content=HeaderMenu(self)
        )
        self.precise_content = ft.Container(
            expand=True,
            content=ft.Column()
        )
        self.controls=[
            ft.Container(
                expand=True,
                content=ft.Column(
                    expand=True,
                    controls=[self.menu_ct, self.precise_content]
                )
            )
        ]
        self.box = ft.AlertDialog(
            title=ft.Text(size=18, font_family="Poppins-Light"),
            content=ft.Text(size=13, font_family="Poppins-Medium"),
            actions=[
                ft.TextButton("Quitter", on_click=self.close_box)
            ]
        )
        self.page.overlay.append(self.box)

    def close_box(self, e):
        self.box.open = False
        self.box.update()
