import flet as ft
from dotenv import load_dotenv
import os
from supabase import create_client
import time
import requests

load_dotenv()
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

class MyField(ft.TextField):
    def __init__(self, my_label: str, my_icon, view_pass: bool, reveal_pass: bool, on_change_function, my_width: int):
        super().__init__(
            label=my_label, prefix_icon=my_icon,
            label_style=ft.TextStyle(size=12, color="black"), border_radius=12,
            focused_border_color="#cf362b", cursor_color="#cf362b",
            focused_border_width=1, border_width=1,
            height=45, dense=True, width=my_width,
            text_style=ft.TextStyle(font_family="Poppins-Medium", size=12),
            password=view_pass, can_reveal_password=reveal_pass,
            on_change=on_change_function, capitalization=ft.TextCapitalization.CHARACTERS
        )


class MyNumberField(ft.TextField):
    def __init__(self, my_label: str, my_icon, view_pass: bool, reveal_pass: bool, on_change_function, my_width: int):
        super().__init__(
            label=my_label, prefix_icon=my_icon,
            label_style=ft.TextStyle(size=12, color="black"), border_radius=12,
            focused_border_color="#cf362b", cursor_color="#cf362b",
            focused_border_width=1, border_width=1,
            height=45, dense=True, width=my_width,
            text_style=ft.TextStyle(font_family="Poppins-Medium", size=12),
            password=view_pass, can_reveal_password=reveal_pass,
            on_change=on_change_function, input_filter=ft.NumbersOnlyInputFilter()
        )


class AddProduct(ft.Container):
    def __init__(self):
        super().__init__(
            padding=20, width=500,
        )
        self.ref = MyField("Reference", ft.icons.NATURE, False, False, None, 200)
        self.name = MyField("Nom du produit", ft.icons.NATURE, False, False, None, 300)
        self.prod_type = MyField("Type", ft.icons.NATURE, False, False, None, 130)
        self.price = MyNumberField("Prix", ft.icons.MONEY_OUTLINED, False, False, None, 130)
        self.confirm = ft.Text(size=14, font_family="Poppins-Medium", color="green")

        self.content = ft.Column(
            [
                ft.Text("ADD PRODUCT", size=18, font_family="Poppins-ExtraBold"),
                ft.Divider(height=3, thickness=1),
                self.name, self.ref, self.prod_type, self.price,
                ft.ElevatedButton(
                    content=ft.Row(
                        [ft.Text("Valider", size=13, font_family="Poppins-Medium", color="white")],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    bgcolor="red", elevation=5, height=50, width=300,
                    style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=16)),
                    on_click=self.check_internet_connection
                ),
                ft.Divider(height=3, thickness=1),
                self.confirm
            ], spacing=15
        )


    def check_internet_connection(self, e):
        try:
            response = requests.get('http://www.google.com', timeout=2)
            if response.status_code == 200:
                self.add_new_product()
                return True
        except requests.ConnectionError:
            self.confirm.value = "Pas de connexion internet"
            self.confirm.update()
        except requests.Timeout:
            self.confirm.value = "La requête a dépassé le temps imparti."
            self.confirm.update()
        except Exception as e:
            self.confirm.value = f"Une erreur s'est produite : {e}"
            self.confirm.update()
        return False

    def add_new_product(self):
        supabase.table("Produits").insert(
            {"ref": self.ref.value, "name": self.name.value, "type": self.prod_type.value, "stock": 0, "prix": self.price.value}
        ).execute()
        self.confirm.value = "Success"
        self.confirm.update()

        for widget in (self.ref, self.name, self.prod_type, self.price):
            widget.value = None
            widget.update()

        time.sleep(2)
        self.confirm.value = ""
        self.confirm.update()


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.fonts = {
        "Poppins-Medium": "fonts/Poppins-Medium.ttf",
        "Poppins-Regular": "fonts/Poppins-Regular.ttf",
        "Poppins-Bold": "fonts/Poppins-Bold.ttf",
        "Poppins-Black": "fonts/Poppins-Black.ttf",
        "Poppins-BlackItalic": "fonts/Poppins-BlackItalic.ttf",
        "Poppins-ExtraBold": "fonts/Poppins-ExtraBold.ttf",
        "Poppins-ExtraBoldItalic": "fonts/Poppins-ExtraBoldItalic.ttf",
        "Poppins-Italic": "fonts/Poppins-Italic.ttf",
        "Poppins-ExtraLight": "fonts/Poppins-ExtraLight.ttf",
        "Poppins-ExtraLightItalic": "fonts/Poppins-ExtraLightItalic.ttf",
        "Poppins-Light": "fonts/Poppins-Light.ttf",
        "Poppins-LightItalic": "fonts/Poppins-LightItalic.ttf",
        "Poppins-MediumItalic": "fonts/Poppins-MediumItalic.ttf",
        "Poppins-SemiBold": "fonts/Poppins-SemiBold.ttf",
        "Poppins-SemiBoldItalic": "fonts/Poppins-SemiBoldItalic.ttf",
        "Poppins-Thin": "fonts/Poppins-Thin.ttf",
        "Poppins-ThinItalic": "fonts/Poppins-ThinItalic.ttf",
    }

    page.add(
        AddProduct()
    )
    page.update()


ft.app(main, assets_dir="../assets")