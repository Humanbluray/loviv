# from dotenv import load_dotenv
# import os
# import datetime, time
# from supabase import create_client
#
# load_dotenv()
# url = os.environ.get("SUPABASE_URL")
# key = os.environ.get("SUPABASE_KEY")
# supabase = create_client(url, key)
#
# # datas = supabase.table("users").select('login, password').execute()
# # print(datas)
#
# self.content = ft.Container(
#             padding=ft.padding.only(20, 10, 20 ,10),
#             content=ft.Column(
#                 controls=[
#                     ft.Row(
#                         controls=[
#                             ft.Text(name, size=13, font_family="Poppins-Regular"),
#                             ft.Text(f"{price} F", size=14, font_family="Poppins-Bold"),
#                         ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
#                     ),
#                     ft.Divider(height=1, thickness=1),
#                     ft.Row(
#                         controls=[
#                             ft.Image(src=image, height=50, width=50, fit=ft.ImageFit.FILL),
#                             ft.Icon(view_icon, color=ft.colors.WHITE70),
#                             ft.Column(
#                                 controls=[
#                                     ft.Text("Quantité", size=12, font_family="Poppins-MediumItalic", color=ft.colors.WHITE54),
#                                     ft.Row(
#                                         controls=[
#                                             ft.IconButton(
#                                                 ft.icons.REMOVE, icon_size=18, icon_color=ft.colors.WHITE60, on_click=self.remove_qty,
#                                             ),
#                                             self.order_quantity,
#                                             ft.IconButton(
#                                                 ft.icons.ADD, icon_size=18, icon_color=ft.colors.WHITE60, on_click=self.add_qty,
#                                             )
#                                         ], spacing=2
#                                     )
#                                 ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
#                             ),
#                             ft.IconButton(
#                                 ft.icons.ADD_SHOPPING_CART_OUTLINED, icon_color=ft.colors.WHITE54, icon_size=18, on_click=self.validate_order,
#                                 data={"image": image, "name": name, "price": price, "type": prod_type}
#                             )
#                         ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
#                     )
#                 ]
#             )
#         )



