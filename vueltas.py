import flet as ft
import math

def main(page: ft.Page):
    page.title = "Contador Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    t = ft.Text(value="Contador de Vueltas", size=30, weight="bold", color="green", text_align=ft.TextAlign.CENTER)
    page.add(
        ft.Row(
            [t],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    
    image_angle = 0
    
    image_to_rotate = ft.Image(
        src="woolen_roll.jpg",
        width=70,
        height=70,
        rotate=ft.Rotate(image_angle)
    )

    page.add(
        ft.Row(
            [image_to_rotate],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    def minus_click(e):
        nonlocal image_angle
        txt_number.value = str(int(txt_number.value) - 1)
        
        image_angle -= 15
        image_to_rotate.rotate.angle = math.radians(image_angle)
        
        page.update()

    def plus_click(e):
        nonlocal image_angle
        txt_number.value = str(int(txt_number.value) + 1)
        
        image_angle += 15
        image_to_rotate.rotate.angle = math.radians(image_angle)
        
        page.update()

    page.add(
        ft.Row(
            [ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
             txt_number,
             ft.IconButton(ft.Icons.ADD, on_click=plus_click)],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

# The Flet application is now directly defined here, making it ready for deployment.
app = ft.app(target=main, view=ft.WEB_BROWSER)