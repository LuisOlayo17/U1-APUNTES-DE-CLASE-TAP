import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Estática - TAP"
    page.window_width = 280
    page.window_height = 450
    page.window_resizable = False
    page.padding = 15

    display = ft.Text("", size=26)
    numero_actual = ""
    operador = ""
    resultado = 0

    def actualizar():
        display.value = numero_actual
        page.update()

    def presionar_numero(e):
        nonlocal numero_actual
        numero_actual += e.control.content.value
        actualizar()

    def presionar_operador(e):
        nonlocal operador, resultado, numero_actual
        if numero_actual != "":
            resultado = float(numero_actual)
            operador = e.control.content.value
            numero_actual = ""
            actualizar()

    def calcular(e):
        nonlocal resultado, numero_actual, operador
        if numero_actual != "":
            if operador == "+":
                resultado += float(numero_actual)
            elif operador == "-":
                resultado -= float(numero_actual)
            elif operador == "×":
                resultado *= float(numero_actual)

            numero_actual = str(resultado)
            actualizar()

    def borrar(e):
        nonlocal numero_actual, operador, resultado
        numero_actual = ""
        operador = ""
        resultado = 0
        actualizar()

    # DISPLAY
    seccion_display = ft.Container(
        content=display,
        height=70,
        padding=10,
        alignment=ft.alignment.Alignment(1, 0),
        bgcolor=ft.Colors.BLACK12,
        border=ft.border.all(1, ft.Colors.RED)
    )

    # BOTONES
    def boton_num(n):
        return ft.Container(
            content=ft.Text(str(n), size=20, color="white"),
            expand=1,
            height=50,
            bgcolor="blue",
            alignment=ft.alignment.Alignment(0, 0),
            border=ft.border.all(1, "white"),
            on_click=presionar_numero
        )

    def boton_op(op):
        return ft.Container(
            content=ft.Text(op, size=20, color="white"),
            expand=1,
            height=60,
            bgcolor="green",
            alignment=ft.alignment.Alignment(0, 0),
            border=ft.border.all(1, "white"),
            on_click=presionar_operador
        )

    boton_borrar = ft.Container(
        content=ft.Text("C", size=20, color="white"),
        expand=1,
        height=50,
        bgcolor="red",
        alignment=ft.alignment.Alignment(0, 0),
        border=ft.border.all(1, "white"),
        on_click=borrar
    )

    boton_igual = ft.Container(
        content=ft.Text("=", size=20, color="white"),
        expand=1,
        height=50,
        bgcolor="orange",
        alignment=ft.alignment.Alignment(0, 0),
        border=ft.border.all(1, "white"),
        on_click=calcular
    )

    seccion_numeros = ft.Column(
        controls=[
            ft.Row([boton_num(1), boton_num(2), boton_num(3)]),
            ft.Row([boton_num(4), boton_num(5), boton_num(6)]),
            ft.Row([boton_num(7), boton_num(8), boton_num(9)]),
            ft.Row([boton_borrar, boton_num(0), boton_igual]),
        ],
        spacing=10
    )

    seccion_operaciones = ft.Row(
        controls=[
            boton_op("+"),
            boton_op("-"),
            boton_op("×"),
        ],
        spacing=10
    )

    page.add(
        ft.Column(
            controls=[
                seccion_display,
                ft.Text("Números:", size=12),
                seccion_numeros,
                ft.Divider(),
                ft.Text("Operaciones:", size=12),
                seccion_operaciones
            ],
            spacing=15
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
