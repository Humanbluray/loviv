from utils import *
from pages.menu import plats


class Stock(ft.Container):
    def __init__(self, cp: object):
        super().__init__(expand=True)
        self.cp = cp
        self.new_ref = ft.FloatingActionButton(
            icon=ft.icons.ADD, on_click=None, bgcolor=ft.colors.BLACK45
        )
        self.table = ft.ListView(expand=True)
        # self.table = ft.DataTable(
        #     columns=[
        #         ft.DataColumn(ft.Text("Image")),
        #         ft.DataColumn(ft.Text("Désignation")),
        #         ft.DataColumn(ft.Text("type")),
        #         ft.DataColumn(ft.Text("Qté")),
        #         ft.DataColumn(ft.Text("Prix")),
        #         ft.DataColumn(ft.Text("total")),
        #     ],
        #     data_text_style=ft.TextStyle(size=12), heading_text_style=ft.TextStyle(size=11)
        # )
        self.search = MyTextField2("Rechercher", "search", False, False, None)
        self.bt_supp_filter = CtIconButton(ft.icons.FILTER_ALT_OFF_OUTLINED, None)
        self.stock_value = ft.Text("0", size=18)
        self.number_of_ref = ft.Text("0", size=18)

        self.content = ft.Column(
            controls=[
                ft.Container(
                    padding=10,
                    content=ft.Row(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Text("Stock", size=16, font_family="Poppins-ExtraBold"),
                                    self.search, self.bt_supp_filter
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    ft.Row(
                                        [
                                            ft.Text("Nombre de référence", size=12, font_family="Poppins-Italic"),
                                            self.number_of_ref
                                        ]
                                    ),
                                    ft.Row(
                                        [
                                            ft.Text("Valeur du stock", size=12, font_family="Poppins-Italic"),
                                            self.stock_value
                                        ]
                                    ),
                                ], spacing=30
                            )
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                ),
                ft.Stack(
                    expand=True,
                    controls=[
                        ft.Column(expand=True, scroll=ft.ScrollMode.AUTO, controls=[self.table]),
                        self.new_ref
                    ], alignment=ft.alignment.bottom_right
                )
            ]
        )
        self.load_datas()

    def load_datas(self):
        stock_value = 0
        number_ref = 0
        filter_datas = list(filter(lambda x: "drink" in x['prod_type'], plats))
        for item in filter_datas:
            valeur = item["price"] * item["stock"]
            stock_value += valeur
            number_ref += 1
            self.table.controls.append(
                StockItem(
                    self.cp, item['image'], item['name'], item["price"], item["stock"], item['prod_type']
                )
            )

        self.stock_value.value = f"{separate(stock_value)}"
        self.number_of_ref.value = f"{number_ref}"

