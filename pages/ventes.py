from utils import *
from pages.menu import plats
import datetime


class Sales(ft.Container):
    def __init__(self, cp: object):
        super().__init__(
            expand=True,
        )
        self.cp = cp

        self.result_all = ft.Text("", size=12, font_family="Poppins-MediumItalic", color="grey")
        self.search_all = MyTextField2("recherche", ft.icons.SEARCH, False, False, self.filter_datas_tab_all)
        self.grid_all = ft.GridView(expand=1, runs_count=5, max_extent=220, child_aspect_ratio=0.7, spacing=5, run_spacing=4,)
        self.order_list = ft.ListView(spacing=5, expand=True)
        self.total = ft.Text(size=13, font_family="Poppins-Medium")
        self.bill_ct = ft.Container(
            border_radius=10, padding=10, border=ft.border.only(left=ft.BorderSide(1, "grey")),
            width=270,
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Column(
                        expand=True, controls=[
                            ft.Row(
                                controls=[
                                    ft.Icon(ft.icons.ATTACH_FILE_OUTLINED, size=24, color=ft.colors.WHITE60),
                                    ft.Text("Facture en cours", size=18, font_family="Poppins-Light"),
                                ]
                            ),
                            ft.Divider(height=1, thickness=1),
                            ft.Row(
                                controls=[
                                    ft.Text("Date", size=12, font_family="Poppins-MediumItalic"),
                                    ft.Text(write_date(str(datetime.date.today())), size=12,
                                            font_family="Poppins-Medium"),
                                ]
                            ),
                            self.order_list,
                        ]
                    ),
                    ft.Column(
                        controls=[
                            ft.Divider(height=1, thickness=1),
                            self.total,
                            ft.ElevatedButton(
                                bgcolor=MAIN_COLOR, height=45,
                                style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=16)),
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(ft.icons.CHECK, size=16, color="white"),
                                        ft.Text("Valider", size=12, font_family="Poppins-Medium", color="white")
                                    ], alignment=ft.MainAxisAlignment.CENTER
                                ),
                                on_click=None
                            )
                        ]
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
        )
        self.content = ft.Row(
            expand=True,
            controls=[
                ft.Container(
                    border_radius=10, padding=10,
                    expand=True,
                    content=ft.Column(
                        expand=True,
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Text("Articles", size=16, font_family="Poppins-ExtraBold"),
                                    self.search_all,
                                    self.result_all
                                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            ),
                            ft.Divider(height=1, thickness=1),
                            self.grid_all
                        ]
                    )
                ),
                self.bill_ct
            ], vertical_alignment=ft.CrossAxisAlignment.START, spacing=20
        )
        self.load_datas()

    def load_datas(self):
        self.result_all.value = f"{len(plats)} Résultats"
        for item in plats:
            self.grid_all.controls.append(
                ItemMenu(
                    self, item["image"], item["name"], item['price'], item['stock'], item['prod_type']
                )
            )

    def filter_datas_tab_all(self, e):
        filter_datas = list(filter(lambda x: self.search_all.value in x['name'], plats))

        for widget in self.grid_all.controls[:]:
            self.grid_all.controls.remove(widget)


        self.result_all.value = f"{len(filter_datas)} Résultats"
        self.result_all.update()

        for item in filter_datas:
            self.grid_all.controls.append(
                ItemMenu(
                    self, item["image"], item["name"], item['price'], item['stock'], item['prod_type']
                )
            )
        self.grid_all.update()

