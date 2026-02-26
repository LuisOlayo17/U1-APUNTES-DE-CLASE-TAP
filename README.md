# U1 – Interfaz Gráfica de Usuario  
---

# 1.1 Fundamentos del Diseño de Interfaces Gráficas

Una Interfaz Gráfica de Usuario (GUI) es el medio mediante el cual una persona interactúa visualmente con un sistema informático. En lugar de escribir comandos en consola, el usuario utiliza botones, campos de texto, listas desplegables y otros componentes visuales.

En Flet, la interfaz se construye mediante un **árbol jerárquico de controles**, donde cada elemento forma parte de un contenedor superior. Todo comienza con el objeto principal llamado `page`, que representa la ventana de la aplicación.

## El objeto `page`

El objeto `page` funciona como el contenedor raíz. Desde ahí se configuran:

- Título de la ventana
- Tema (claro u oscuro)
- Color de fondo
- Márgenes y espaciados
- Eventos globales

Ejemplo básico de configuración:

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Registro de Estudiantes"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F5F5F5"
    page.padding = 20

ft.app(target=main)
```

---

## Organización de elementos: Column y Row

En cualquier GUI es fundamental organizar visualmente los componentes.

### ft.Column
Organiza los controles verticalmente (uno debajo del otro).

Ejemplo:

```python
ft.Column(
    controls=[
        ft.TextField(label="Nombre"),
        ft.TextField(label="Correo"),
        ft.ElevatedButton("Enviar")
    ],
    spacing=10
)
```

### ft.Row
Organiza los controles horizontalmente (uno al lado del otro).

```python
ft.Row(
    controls=[
        ft.ElevatedButton("1"),
        ft.ElevatedButton("2"),
        ft.ElevatedButton("3")
    ],
    spacing=5
)
```

---

## Propiedades importantes

### expand
Permite que un elemento ocupe todo el espacio disponible dentro del contenedor padre.

```python
ft.TextField(expand=True)
```

### alignment
Define la alineación de los controles.

```python
alignment=ft.alignment.Alignment(0, 0)
```

---

# 1.2 Eventos en una Aplicación

Un evento es cualquier acción que ocurre dentro de la aplicación y que requiere una respuesta del sistema.

Ejemplos de eventos:
- Clic en botón
- Cambio en un campo de texto
- Envío de formulario
- Recepción de mensaje

## Eventos más comunes en Flet

### on_click
Se ejecuta cuando el usuario presiona un botón.

```python
def boton_click(e):
    print("Botón presionado")

ft.ElevatedButton("Aceptar", on_click=boton_click)
```

---

### on_change
Se activa cuando el contenido de un campo cambia.

```python
def texto_cambiado(e):
    print("Nuevo valor:", e.control.value)

ft.TextField(on_change=texto_cambiado)
```

---

### subscribe (Comunicación en tiempo real)

En aplicaciones como chat1.py, se utiliza un sistema de publicación y suscripción (pub/sub).

Ejemplo real:

```python
page.pubsub.subscribe(on_message)
```

Este método permite que la aplicación reaccione cuando otro usuario envía un mensaje.

<img width="1896" height="889" alt="image" src="https://github.com/user-attachments/assets/e45366eb-253d-403f-b659-f390fb351655" />


---

# 1.3 Manejo de Eventos (Event Handlers)

El manejo de eventos consiste en definir qué ocurre cuando el usuario interactúa con la interfaz.

Proceso general:

1. El usuario interactúa.
2. Se ejecuta una función.
3. Se actualiza la interfaz.
4. Se llama a `page.update()`.

Ejemplo en una calculadora:

```python
def numero_click(e):
    display.value += e.control.data
    page.update()
```

<img width="1571" height="876" alt="image" src="https://github.com/user-attachments/assets/956d1a76-45d5-4db5-8838-f294c71cc8a4" />


Flet no actualiza automáticamente la pantalla. Si no se llama a `page.update()`, el usuario no verá los cambios aunque el valor interno haya sido modificado.

---

# 1.4 Componentes Gráficos de Control

Los controles permiten capturar información y mostrar datos.

## Componentes principales usados en clase

| Componente | Uso | Ejemplo práctico |
|------------|------|-----------------|
| ft.TextField | Captura texto libre | Nombre, Email |
| ft.Dropdown | Lista de opciones | Carrera |
| ft.RadioGroup | Selección única visible | Género |
| ft.Container | Personalización visual | Bordes, colores |
| ft.Divider | Separación visual | División de secciones |
| ft.ElevatedButton | Ejecutar acciones | Enviar |

---

## Ejemplo completo de formulario

```python
def main(page: ft.Page):

    def enviar_click(e):
        resultado.value = f"Hola {txt_nombre.value}"
        page.update()

    txt_nombre = ft.TextField(label="Nombre")
    resultado = ft.Text()

    page.add(
        ft.Column([
            txt_nombre,
            ft.ElevatedButton("Enviar", on_click=enviar_click),
            resultado
        ])
    )

ft.app(target=main)
```

---

# 1.5 Flujo de Interacción en una GUI

El ciclo básico en una aplicación gráfica es:

1. Entrada del usuario
2. Procesamiento interno
3. Actualización visual

Este ciclo ocurre constantemente mientras la aplicación está en ejecución.

---

# 1.6 Relación con la Lógica de Programación

El archivo ejercicio1.py, aunque funciona en consola, contiene la base lógica que luego se adapta a la interfaz gráfica.

Ejemplo de estructura condicional:

```python
if int(edad_usuario) > 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
```

En una GUI, esa misma lógica puede ejecutarse dentro de un evento on_click.

---

# Referencias Bibliográficas

- Flet Team. (2024). *Flet: Build Flutter apps in Python*. Disponible en: https://flet.dev/docs/
- Matthes, E. (2023). *Python Crash Course: A Hands-On, Project-Based Introduction to Programming*. No Starch Press.
- Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
