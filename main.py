import flet as ft

def main(page: ft.Page):

    page.title = "Calculadora IAP"
    page.window_width = 250
    page.window_height = 400
    page.padding = 20

    # Display
    display_text = ft.Text("0", size=30)

    display = ft.Container(
        content=display_text,
        bgcolor=ft.Colors.BLACK12,
        border_radius=8,
        alignment=ft.alignment.Alignment(1, 0),
        padding=10,
        width=210,
        height=70,
    )

    # Funciones
    def add_number(e, number):
        if display_text.value == "0":
            display_text.value = number
        else:
            display_text.value += number
        page.update()

    def clear_display(e):
        display_text.value = "0"
        page.update()

    # Grid de botones
    grid = ft.GridView(
        runs_count=2,
        spacing=10,
        run_spacing=10,
        width=210,
        height=200,
        expand=False
    )

    # Botones
    grid.controls.append(
        ft.Container(
            content=ft.Text("1", size=20),
            alignment=ft.alignment.Alignment(0, 0),
            bgcolor=ft.Colors.PRIMARY,
            border_radius=8,
            on_click=lambda e: add_number(e, "1")
        )
    )

    grid.controls.append(
        ft.Container(
            content=ft.Text("2", size=20),
            alignment=ft.alignment.Alignment(0, 0),
            bgcolor=ft.Colors.SECONDARY,
            border_radius=8,
            on_click=lambda e: add_number(e, "2")
        )
    )

    grid.controls.append(
        ft.Container(
            content=ft.Text("3", size=20),
            alignment=ft.alignment.Alignment(0, 0),
            bgcolor=ft.Colors.TERTIARY,
            border_radius=8,
            on_click=lambda e: add_number(e, "3")
        )
    )

    grid.controls.append(
        ft.Container(
            content=ft.Text("C", size=20, color=ft.Colors.WHITE),
            alignment=ft.alignment.Alignment(0, 0),
            bgcolor=ft.Colors.ERROR,
            border_radius=8,
            on_click=clear_display
        )
    )

    # Layout principal
    page.add(
        ft.Column(
            controls=[display, grid],
            tight=True
        )
    )

ft.app(target=main)