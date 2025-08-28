import flet as ft
import math
import os  # Importar el módulo os para variables de entorno

def main(page: ft.Page):
    page.title = "Contador Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    t = ft.Text(value="Contador Vueltas, para Mi Bubucita ;)", size=30, weight="bold", color="green", text_align=ft.TextAlign.CENTER)
    page.add(
        ft.Row(
            [t],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    
    image_angle = 0
    image_path = os.path.join(os.path.dirname(__file__), "assets", "woolen_roll.jpg")
    image_to_rotate = ft.Image(
      
        # src="https://labsurconsultores.cl/valida_doc/woolen_roll.jpg",  # Ruta absoluta para Render
        src=image_path,
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
    def reset_click(e):
        nonlocal image_angle
        txt_number.value = "0"
        
        image_angle = 0
        image_to_rotate.rotate.angle = math.radians(image_angle)
        
        page.update()

    page.add(
        ft.Row(
            [ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
             txt_number,
             ft.IconButton(ft.Icons.ADD, on_click=plus_click),
             ft.ElevatedButton(text="Reset", on_click=reset_click, color=ft.Colors.WHITE, bgcolor=ft.Colors.RED_400)
             ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

#Ejecutar el programa
#ft.app(target=main, view=ft.WEB_BROWSER, assets_dir="assets")

# Configuración para Render.com
 if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Puerto dinámico de Render
    ft.app(target=main, port=port, view=ft.WEB_BROWSER, host="0.0.0.0", assets_dir="assets")