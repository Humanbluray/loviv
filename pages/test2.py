import win32print
import win32api
import os


def print_file(filename):
    # Obtenir l'imprimante par défaut
    printer_name = win32print.GetDefaultPrinter()

    # Envoyer le fichier à l'imprimante par défaut
    print("Envoi du fichier à l'imprimante:", printer_name)

    try:
        win32api.ShellExecute(
            0,
            "print",
            filename,
            f'/d:"{printer_name}"',
            ".",
            0
        )
        print("Impression lancée avec succès.")
    except Exception as e:
        print("Erreur lors de l'impression :", e)


if __name__ == "__main__":
    # Nom du fichier à imprimer (remplace par le chemin de ton fichier)
    filename = "../bull prim.pdf"

    # Vérifie si le fichier existe avant l'impression
    if os.path.exists(filename):
        print_file(filename)
    else:
        print(f"Le fichier '{filename}' n'existe pas.")


# self.order_details = ft.AlertDialog(
        #     title=ft.Row(
        #         controls=[
        #             ft.Icon(ft.icons.ATTACH_FILE_OUTLINED, size=24, color=ft.colors.WHITE60),
        #             ft.Text("Facture en cours", size=18, font_family="Poppins-Light"),
        #         ]
        #     ),
        #     content=ft.Column(
        #         expand=True,
        #         controls=[
        #             ft.Divider(height=1, thickness=1),
        #             self.order_list,
        #             ft.Divider(height=1, thickness=1),
        #             self.total
        #         ]
        #     ),
        #     actions=[
        #         ft.ElevatedButton(
        #             bgcolor=main_color, height=45,
        #             style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=16)),
        #             content=ft.Row(
        #                 controls=[
        #                     ft.Icon(ft.icons.CHECK, size=16, color="white"),
        #                     ft.Text("Valider", size=12, font_family="Poppins-Medium", color="white")
        #                 ], alignment=ft.MainAxisAlignment.CENTER
        #             ),
        #             on_click=None
        #         )
        #     ]
        # )