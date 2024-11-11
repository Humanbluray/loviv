import flet as ft
from pages.landing_page import LandingPage
from pages.first_login_page import FirstLoginPage
from pages.accueil import Welcome


def main(page: ft.Page):
    page.title = "Loviv Food App"
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
    page.theme = ft.Theme(
        font_family="Poppins-Medium",
        # color_scheme_seed=ft.colors.BLACK
    )
    page.theme_mode = ft.ThemeMode.DARK
    # page.splash = ft.Image(src="Ovive LOGO.png")

    def route_change(route):
        # initial route ...
        page.views.clear()
        page.views.append(LandingPage(page))
        page.update()

        if page.route == '/first-login':
            page.views.append(FirstLoginPage(page))
            page.update()

        elif page.route =="/welcome":
            page.views.append(Welcome(page))
            page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=main, assets_dir="assets", route_url_strategy="default")