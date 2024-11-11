from utils import *
from pages.ventes import Sales
from pages.stock import Stock


class HeaderItem(ft.Container):
    def __init__(self, my_name: str, my_icon: str, is_selected: bool):
        super().__init__(
            padding=10, border_radius=24, on_hover=self.hover_func,
            scale=ft.transform.Scale(1),
            animate_scale=ft.animation.Animation(300, ft.AnimationCurve.DECELERATE)
        )
        self.my_name = my_name
        self.my_icon = my_icon
        self.is_selected = is_selected

        if self.is_selected:
            my_color = SECOND_COLOR
        else:
            my_color = ft.colors.WHITE70

        self.image_icon = ft.Icon(my_icon, size=18, color=my_color)
        self.title = ft.Text(my_name, size=12, font_family="Poppins-Medium", color=my_color)

        self.content = ft.Row(
            controls=[
                self.image_icon, self.title
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

    def hover_func(self, e):
        if e.data == "true":
            self.bgcolor = ft.colors.BLACK26
            self.scale = 1.1
            self.update()
        else:
            if self.is_selected:
                self.bgcolor = None
                self.scale = 1
                self.image_icon.color = SECOND_COLOR
                self.title.color = SECOND_COLOR
                self.image_icon.update()
                self.title.update()
                self.update()
            else:
                self.bgcolor = None
                self.scale = 1
                self.image_icon.color = ft.colors.WHITE70
                self.title.color = ft.colors.WHITE70
                self.image_icon.update()
                self.title.update()
                self.update()

    def set_selected(self):
        self.is_selected = True
        self.image_icon.color = SECOND_COLOR
        self.title.color = SECOND_COLOR

    def set_unselected(self):
        self.is_selected = False
        self.image_icon.color = ft.colors.WHITE70
        self.title.color = ft.colors.WHITE70


class HeaderMenu(ft.Card):
    def __init__(self, cp: object):
        super().__init__(
            elevation=10, clip_behavior=ft.ClipBehavior.HARD_EDGE,
        )
        self.cp = cp
        self.items = HeaderItem("Articles", ft.icons.FASTFOOD_OUTLINED, False)
        self.stock = HeaderItem("Stock", ft.icons.WAREHOUSE_OUTLINED, False)
        self.inventory = HeaderItem("Inventaire", ft.icons.INVENTORY_OUTLINED, False)
        self.entry = HeaderItem("Entrées", ft.icons.SMART_BUTTON_OUTLINED, False)
        self.bills = HeaderItem("Factures", ft.icons.ATTACH_MONEY_OUTLINED, False)
        self.transactions = HeaderItem("Historique", ft.icons.HISTORY_TOGGLE_OFF_OUTLINED, False)
        self.profile = HeaderItem("Profil", ft.icons.PERSON_OUTLINED, False)

        self.children = [self.items, self.stock, self.inventory, self.entry, self.bills, self.transactions, self.profile]

        self.content = ft.Container(
            padding=10, border_radius=16,
            content=ft.Row(
                [self.items, self.stock, self.inventory, self.entry, self.bills, self.transactions, self.profile],
                alignment=ft.MainAxisAlignment.SPACE_AROUND
            )
        )
        for child in self.children:
            child.on_click = self.click_on_item

    def click_on_item(self, e):
        for child in self.children:
            child.set_unselected()
            child.update()

        e.control.set_selected()
        e.control.title.update()
        e.control.image_icon.update()
        e.control.update()

        if e.control.title.value == "Articles":
            for widget in self.cp.precise_content.content.controls[:]:
                self.cp.precise_content.content.controls.remove(widget)

            self.cp.precise_content.content.controls.append(Sales(self.cp))
            self.cp.precise_content.update()

        elif e.control.title.value == "Stock":
            for widget in self.cp.precise_content.content.controls[:]:
                self.cp.precise_content.content.controls.remove(widget)

            self.cp.precise_content.content.controls.append(Stock(self.cp))
            self.cp.precise_content.update()
