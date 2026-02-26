from dataclasses import dataclass

import flet as ft


# =========================
# MODELO DE MENSAJE
# =========================
@dataclass
class Message:  # noqa: B903
    # Nombre del usuario que envía el mensaje
    user_name: str
    # Contenido del mensaje
    text: str
    # Tipo de mensaje (chat o mensaje de inicio de sesión)
    message_type: str


# =========================
# COMPONENTE VISUAL DEL MENSAJE
# =========================
@ft.control
class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()

        # Guardamos el mensaje recibido
        self.message = message

        # Alineación vertical de los elementos
        self.vertical_alignment = ft.CrossAxisAlignment.START

        # Controles que forman el mensaje (avatar + texto)
        self.controls = [
            # Avatar circular con la inicial del usuario
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(self.message.user_name)),
                color=ft.Colors.WHITE,
                bgcolor=self.get_avatar_color(self.message.user_name),
            ),
            # Columna con nombre del usuario y mensaje
            ft.Column(
                tight=True,
                spacing=5,
                controls=[
                    # Nombre del usuario en negritas
                    ft.Text(self.message.user_name, weight=ft.FontWeight.BOLD),
                    # Texto del mensaje (seleccionable)
                    ft.Text(self.message.text, selectable=True),
                ],
            ),
        ]

    # Obtiene la inicial del nombre del usuario
    def get_initials(self, user_name: str):
        if user_name:
            return user_name[:1].capitalize()
        else:
            return "Unknown"

    # Asigna un color al avatar según el nombre del usuario
    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.Colors.AMBER,
            ft.Colors.BLUE,
            ft.Colors.BROWN,
            ft.Colors.CYAN,
            ft.Colors.GREEN,
            ft.Colors.INDIGO,
            ft.Colors.LIME,
            ft.Colors.ORANGE,
            ft.Colors.PINK,
            ft.Colors.PURPLE,
            ft.Colors.RED,
            ft.Colors.TEAL,
            ft.Colors.YELLOW,
        ]
        # Se usa el hash del nombre para que el color sea siempre el mismo
        return colors_lookup[hash(user_name) % len(colors_lookup)]


# =========================
# FUNCIÓN PRINCIPAL
# =========================
def main(page: ft.Page):
    # Configuración básica de la página
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.title = "Flet Chat"

    # -------------------------
    # FUNCIÓN PARA UNIRSE AL CHAT
    # -------------------------
    def join_chat_click(e):
        # Validar que el nombre no esté vacío
        if not join_user_name.value:
            join_user_name.error_text = "Name cannot be blank!"
            join_user_name.update()
        else:
            # Guardar el nombre del usuario en la sesión
            page.session.store.set("user_name", join_user_name.value)

            # Cerrar el diálogo de bienvenida
            welcome_dlg.open = False

            # Mostrar el nombre como prefijo al escribir mensajes
            new_message.prefix = ft.Text(f"{join_user_name.value}: ")

            # Enviar mensaje de bienvenida al chat
            page.pubsub.send_all(
                Message(
                    user_name=join_user_name.value,
                    text=f"{join_user_name.value} Se a unido al chat.",
                    message_type="login_message",
                )
            )

    # -------------------------
    # FUNCIÓN PARA ENVIAR MENSAJES
    # -------------------------
    async def send_message_click(e):
        if new_message.value != "":
            # Enviar el mensaje a todos los usuarios conectados
            page.pubsub.send_all(
                Message(
                    page.session.store.get("user_name"),
                    new_message.value,
                    message_type="chat_message",
                )
            )
            # Limpiar el campo de texto
            new_message.value = ""
            await new_message.focus()

    # -------------------------
    # FUNCIÓN PARA RECIBIR MENSAJES
    # -------------------------
    def on_message(message: Message):
        # Mensaje normal de chat
        if message.message_type == "chat_message":
            m = ChatMessage(message)
        # Mensaje de inicio de sesión
        elif message.message_type == "login_message":
            m = ft.Text(
                message.text,
                italic=True,
                color=ft.Colors.BLACK_45,
                size=12,
            )

        # Agregar el mensaje al listado
        chat.controls.append(m)
        page.update()

    # Suscribirse al sistema de mensajes
    page.pubsub.subscribe(on_message)

    # =========================
    # DIÁLOGO DE BIENVENIDA
    # =========================
    join_user_name = ft.TextField(
        label="Ingresa tu usuario",
        autofocus=True,
        on_submit=join_chat_click,
    )

    welcome_dlg = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Bienvenido!"),
        content=ft.Column([join_user_name], width=300, height=70, tight=True),
        actions=[ft.Button(content="Entrar", on_click=join_chat_click)],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.overlay.append(welcome_dlg)

    # =========================
    # LISTA DE MENSAJES DEL CHAT
    # =========================
    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    # =========================
    # CAMPO PARA NUEVOS MENSAJES
    # =========================
    new_message = ft.TextField(
        hint_text="Escribe un mensaje...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        on_submit=send_message_click,
    )

    # =========================
    # ESTRUCTURA FINAL DE LA PÁGINA
    # =========================
    page.add(
        # Contenedor del chat
        ft.Container(
            content=chat,
            border=ft.Border.all(1, ft.Colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True,
        ),
        # Barra inferior para escribir mensajes
        ft.Row(
            controls=[
                new_message,
                ft.IconButton(
                    icon=ft.Icons.SEND_ROUNDED,
                    tooltip="Enviar mensaje",
                    on_click=send_message_click,
                ),
            ]
        ),
    )


# Ejecutar la aplicación
ft.run(main)