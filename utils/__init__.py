import flet as ft

MAIN_COLOR = "#C23028"
SECOND_COLOR = ft.colors.DEEP_ORANGE
THIRD_COLOR = "#C5C5C6"
FOURTH_COLOR = "#EBB016"

def write_date(string_date: str):
    """This function writes the _date of the day"""

    def find_month_name(month_number):
        year_months = [
            'janvier', "Février", "Mars", "Avril", "Mai", "Juin",
            "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
        ]
        return year_months[month_number - 1]

    the_year = string_date[0: 4]
    the_month = string_date[5: 7]
    the_day = string_date[8:10]
    month_name = find_month_name(int(the_month))
    return str(the_day) + " " + month_name + " " + str(the_year)


def separate(my_number: int):
    string_number = str(my_number)[::-1]
    result = ""
    for i, string_number in enumerate(string_number, 1):
        formatted_number = string_number + " " if i % 3 == 0 and i != len(string_number) else string_number
        result += formatted_number

    return result[::-1]


class MyTextField(ft.TextField):
    def __init__(self, my_label: str, my_icon, view_pass: bool, reveal_pass: bool, on_change_function):
        super().__init__(
            label=my_label, prefix_icon=my_icon,
            label_style=ft.TextStyle(size=12, ), border_radius=12,
            focused_border_color="#cf362b", cursor_color="#cf362b",
            focused_border_width=1, border_width=1,
            height=45, dense=True, width=220,
            text_style=ft.TextStyle(font_family="Poppins-Medium", size=12),
            password=view_pass, can_reveal_password=reveal_pass,
            on_change=on_change_function
        )


class MyTextField2(ft.TextField):
    def __init__(self, my_label: str, my_icon, view_pass: bool, reveal_pass: bool, on_change_function):
        super().__init__(
            label=my_label, prefix_icon=my_icon,
            label_style=ft.TextStyle(size=12, color="white"), border_radius=12,
            focused_border_color=SECOND_COLOR, cursor_color=SECOND_COLOR,
            focused_border_width=1, border_width=1,
            height=45, dense=True, width=350,
            text_style=ft.TextStyle(font_family="Poppins-Medium", size=12),
            password=view_pass, can_reveal_password=reveal_pass,
            on_change=on_change_function,
            capitalization=ft.TextCapitalization.CHARACTERS,
        )


class MyElevButton(ft.ElevatedButton):
    def __init__(self, my_text: str, on_click_function):
        super().__init__(
            height=45, width=220,
            style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=24)),
            bgcolor=MAIN_COLOR, elevation=5,
            scale=ft.transform.Scale(1),
            animate_scale=ft.animation.Animation(300, ft.AnimationCurve.DECELERATE),
            on_hover=self.button_hover,
            on_click=on_click_function,
            content=ft.Row(
                controls=[
                    ft.Text(my_text, size=12, color=ft.colors.WHITE)
                ], alignment=ft.MainAxisAlignment.CENTER
            )
        )

    def button_hover(self, e):
        if e.data == "true":
            self.scale = 1.1
            self.update()
        else:
            self.scale = 1
            self.update()


class MyTextButton(ft.TextButton):
    def __init__(self, my_text: str, on_click):
        super().__init__(
            content=ft.Row(
                [ft.Text(my_text, size=13, font_family="Poppins Medium", color=MAIN_COLOR)],
                alignment=ft.MainAxisAlignment.CENTER
            ), width=220, on_click=on_click
        )


class MyTextButton2(ft.TextButton):
    def __init__(self, my_text: str, my_icon: str, on_click):
        super().__init__(
            content=ft.Row(
                [
                    ft.Icon(my_icon, size=18, color=SECOND_COLOR),
                    ft.Text(my_text, size=14, font_family="Poppins Medium", color=SECOND_COLOR)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ), width=220, on_click=on_click
        )


class ItemMenu(ft.Card):
    def __init__(self, cp: object, image: str, name: str, price: int, quantity: int, prod_type: str):
        super().__init__(
            elevation=5
            # col={"sm": 6, "md": 4, "xl": 2},
        )
        self.cp = cp  # parent object
        self.image = image
        self.name = name
        self.price = price
        self.quantity = quantity
        self.prod_type = prod_type
        self.order_quantity = ft.Text("0", size=18, font_family="Poppins-Light", color=ft.colors.WHITE54)

        if self.prod_type == "food":
            view_icon = ft.icons.RESTAURANT_OUTLINED
        else:
            view_icon = ft.icons.LOCAL_DRINK_OUTLINED

        self.content = ft.Container(
            padding=10, border_radius=20,
            content=ft.Column(
                controls=[
                    ft.Container(
                        border_radius=20, width=200,  height=150,
                        content=ft.Image(src=image, fit=ft.ImageFit.COVER)
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Column(
                                    [
                                        ft.Text(name, size=12, font_family="Poppins-Medium"),
                                        ft.Text(f"{separate(price)}", size=12, font_family="Poppins-Bold", color=SECOND_COLOR),
                                    ], spacing=1
                                ),
                                ft.Divider(height=1, thickness=1),
                                ft.Row(
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.IconButton(ft.icons.KEYBOARD_ARROW_LEFT_OUTLINED, scale=0.7, icon_color=ft.colors.WHITE54,
                                                              on_click=self.remove_qty),
                                                self.order_quantity,
                                                ft.IconButton(ft.icons.KEYBOARD_ARROW_RIGHT_OUTLINED, scale=0.7, icon_color=ft.colors.WHITE54,
                                                              on_click=self.add_qty)
                                            ], spacing=2
                                        ),
                                        ft.IconButton(
                                            ft.icons.ADD_OUTLINED,
                                            icon_size=18,
                                            on_click=self.validate_order,
                                            data={"image": image, "name": name, "price": price, "type": prod_type}
                                        )
                                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                )
                            ]
                        )
                    )
                ]
            )
        )

    def add_qty(self, e):
        qty = int(self.order_quantity.value)
        new_qty = qty + 1
        self.order_quantity.value  = new_qty
        self.order_quantity.update()

    def remove_qty(self, e):
        if int(self.order_quantity.value) > 0:
            qty = int(self.order_quantity.value)
            new_qty = qty - 1
            self.order_quantity.value  = new_qty
            self.order_quantity.update()

    def validate_order(self, e):
        if int(self.order_quantity.value) > 0:
            e.control.data["order_quantity"] = self.order_quantity.value
            self.cp.order_list.controls.append(
                OrderItem(self.cp, e.control.data)
            )
            self.cp.order_list.update()

            total = 0
            for widget in self.cp.order_list.controls:
                total += widget.order_data['price'] * widget.order_data["order_quantity"]

            self.cp.total.value = f"Montant Total: \n{separate(total)} XAF"
            self.cp.total.update()

            self.order_quantity.value = "0"
            self.order_quantity.update()

            # Alert message
            self.cp.cp.box.content.value = "Ajouté!"
            self.cp.cp.box.title.value = "Confirmé"
            self.cp.cp.box.open = True
            self.cp.cp.box.update()

        else:
            # Alert message
            self.cp.cp.box.content.value = "La quantité est nulle!"
            self.cp.cp.box.title.value = "Attention"
            self.cp.cp.box.open = True
            self.cp.cp.box.update()


class OrderItem(ft.Card):
    def __init__(self, cp: object, order_data: dict):
        super().__init__(
            elevation=5,
            content=ft.Container(
                width=400, padding=ft.padding.only(10, 5, 10, 5), border_radius=16,
                content=ft.Column(
                    controls=[
                        ft.Row(
                            [
                                ft.Text(order_data["name"], size=12, font_family="Poppins-Bold"),
                            ], alignment=ft.MainAxisAlignment.START
                        ),
                        ft.Divider(height=1, thickness=1),
                        ft.Row(
                            controls=[
                                ft.Image(order_data["image"], height=35, width=35, fit=ft.ImageFit.FILL),
                                ft.Row(
                                    controls=[
                                        ft.Text("Total", size=12, font_family="Poppins-Italic",),
                                        ft.Text(
                                            f"{order_data['price']} x {order_data['order_quantity']}", size=12, font_family="Poppins-Medium",
                                        ),
                                    ]
                                ),
                                ft.IconButton(ft.icons.DELETE_OUTLINED, icon_size=24, icon_color=MAIN_COLOR, on_click=self.remove)
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    ], spacing=3
                ),
            )
        )
        self.cp = cp
        self.order_data = order_data

    def remove(self, e):
        self.cp.order_list.controls.remove(self)
        self.cp.order_list.update()

        total = 0
        for wid in self.cp.order_list.controls[:]:
            total += 1

        total_facture = 0
        for widget in self.cp.order_list.controls:
            total_facture += widget.order_data['price'] * widget.order_data["order_quantity"]

        self.cp.total.value = f"Montant Total: \n{separate(total_facture)} XAF"
        self.cp.total.update()


class CtIconButton(ft.Container):
    def __init__(self, my_icon: str, on_click_function):
        super().__init__(
            scale= ft.transform.Scale(1),
            animate_scale=ft.animation.Animation(300, ft.AnimationCurve.FAST_OUT_SLOWIN),
            shape=ft.BoxShape.CIRCLE,
            height=45, width=45, padding=10,
            on_hover=self.hover_function,
            on_click=on_click_function
        )
        self.my_icon = ft.Icon(my_icon, size=24, color=ft.colors.WHITE60)
        self.content = ft.Row(
            [
                self.my_icon
            ], alignment=ft.MainAxisAlignment.CENTER
        )

    def hover_function(self, e):
        if e.data == "true":
            self.scale = 1.2
            self.my_icon.color = SECOND_COLOR
            self.my_icon.update()
            self.update()
        else:
            self.scale = 1.
            self.my_icon.color = ft.colors.WHITE60
            self.my_icon.update()
            self.update()


class StockItem(ft.Card):
    def __init__(self, cp: object, image: str, name: str, price: int, quantity: int, prod_type: str):
        super().__init__(
            elevation=10
        )
        self.cp = cp  # parent object
        self.image = image
        self.name = name
        self.price = price
        self.quantity = quantity
        self.prod_type = prod_type

        if self.prod_type == "food":
            view_icon = ft.icons.RESTAURANT_OUTLINED
        else:
            view_icon = ft.icons.LOCAL_DRINK_OUTLINED

        self.content = ft.Container(
            padding=ft.padding.only(10, 7, 10, 7), border_radius=20,
            content=ft.ListTile(
                title=ft.Text(name, size=13, font_family="Poppins-Bold"),
                subtitle=ft.Row(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Text("Type de produit :", size=12, font_family="Poppins-Italic", color="grey"),
                                ft.Text(f"{prod_type}", size=12, font_family="Poppins-Bold", color=SECOND_COLOR)
                            ]
                        ),
                        ft.Row(
                            controls=[
                                ft.Text("Qté", size=12, font_family="Poppins-Italic", color="grey"),
                                ft.Text(f"{quantity}", size=12, font_family="Poppins-Bold", color=SECOND_COLOR)
                            ]
                        )
                    ]
                ),
                leading=ft.Image(src=image, height=35, width=35),
                trailing=ft.IconButton(
                    ft.icons.HISTORY_TOGGLE_OFF_OUTLINED, icon_color=ft.colors.WHITE60
                )
            )
        )


class Products(ft.Card):
    def __init__(self, name: str, price: int, image: str):
        super().__init__(
            elevation=5,
            data={"name": name, "price": price, "image": image}
        )
        self.price = price
        self.name = name
        self.image = image
        self.content = ft.Container(
            padding=0, height=300, width=200, data={"name": name, "price": price, "image": image},
            content=ft.Column(
                controls=[
                    ft.Container(
                        padding=0, height=300, width=200,
                        border_radius=ft.border_radius.only(bottom_left=16, bottom_right=16),
                        content=ft.Image(src=image, fit=ft.ImageFit.FIT_HEIGHT),
                    ),
                    ft.Container(
                        padding=10,
                        content=ft.Column(
                            controls=[
                                ft.Text(name, size=12, font_family="Poppins-Bold"),
                                ft.Text(f"{price}", size=12, font_family="Poppins-Bold")
                            ]
                        )
                    )
                ]
            )
        )
