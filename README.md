# U1 – Interfaz Gráfica de Usuario  

---

# 1.1 Fundamentos del Diseño de Interfaces Gráficas

Una Interfaz Gráfica de Usuario (GUI, Graphical User Interface) es el entorno visual que permite la interacción entre una persona y un sistema computacional mediante elementos gráficos. Este tipo de interfaz sustituye el uso exclusivo de comandos en texto por componentes visuales que facilitan la usabilidad, accesibilidad y eficiencia del sistema.

Las GUI se basan en principios de diseño como:

- Claridad visual
- Organización jerárquica
- Consistencia
- Retroalimentación inmediata
- Simplicidad en la interacción

En el framework Flet, la interfaz se construye mediante una estructura jerárquica de controles organizada en forma de árbol. Cada elemento forma parte de un contenedor superior. El nodo raíz de esta estructura es el objeto `page`, que representa la ventana principal de la aplicación.

---

## El objeto `page`

El objeto `page` actúa como el contenedor principal de la aplicación. Desde este objeto se controlan aspectos visuales, estructurales y funcionales.

Entre sus principales responsabilidades se encuentran:

- Configuración del título de la ventana.
- Definición del modo de tema (claro u oscuro).
- Control del color de fondo.
- Administración de márgenes internos.
- Gestión de eventos globales.
- Renderización de los controles añadidos.

Ejemplo de configuración inicial:

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Registro de Estudiantes"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F5F5F5"
    page.padding = 20

ft.app(target=main)
```

Esta configuración establece la identidad visual básica de la aplicación y prepara el entorno para agregar los controles gráficos.

---

## Organización de Elementos: Column y Row

Una correcta organización visual es esencial para garantizar la comprensión y facilidad de uso.

### ft.Column

Permite organizar los controles verticalmente. Es especialmente útil en formularios donde los campos deben mostrarse uno debajo del otro.

Características:
- Distribución lineal vertical.
- Control del espaciado.
- Posibilidad de expansión adaptable.
- Soporte de alineación.

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

---

### ft.Row

Permite organizar los controles horizontalmente. Es útil cuando se requiere agrupar botones o elementos relacionados.

Características:
- Distribución lineal horizontal.
- Ajuste dinámico del espacio.
- Compatibilidad con `expand`.

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

## Propiedades Relevantes

### expand

Permite que un control ocupe todo el espacio disponible dentro del contenedor padre. Esto favorece la creación de interfaces adaptables y responsivas.

```python
ft.TextField(expand=True)
```

### alignment

Controla la posición de los elementos dentro del contenedor, permitiendo centrado, alineación lateral o distribución personalizada.

```python
alignment=ft.alignment.Alignment(0, 0)
```

Estas propiedades influyen directamente en la experiencia del usuario y en la percepción visual del sistema.

---

# 1.2 Tipos de Eventos

Los eventos son mecanismos que permiten que una aplicación responda a acciones del usuario o del sistema. Constituyen la base del comportamiento dinámico de una GUI.

Un evento se compone de:

- Una acción detonante.
- Un manejador (función).
- Una respuesta visual o lógica.

Ejemplos de eventos:
- Clic en botón.
- Cambio de texto.
- Selección de opción.
- Recepción de información externa.

---

## Eventos más utilizados en Flet

### on_click

Se ejecuta cuando el usuario presiona un botón. Es uno de los eventos más utilizados.

```python
def boton_click(e):
    print("Botón presionado")

ft.ElevatedButton("Aceptar", on_click=boton_click)
```

---

### on_change

Se activa cuando cambia el contenido de un campo de entrada.

```python
def texto_cambiado(e):
    print("Nuevo valor:", e.control.value)

ft.TextField(on_change=texto_cambiado)
```

Este evento es útil para validaciones en tiempo real.

---

### subscribe (Modelo Publicación/Suscripción)

En aplicaciones como `chat1.py`, se emplea el modelo pub/sub, el cual permite que múltiples instancias compartan información en tiempo real.

```python
page.pubsub.subscribe(on_message)
```

Este mecanismo permite que la aplicación escuche mensajes emitidos por otros usuarios y ejecute automáticamente una función de respuesta.

<img width="1896" height="889" alt="image" src="https://github.com/user-attachments/assets/e45366eb-253d-403f-b659-f390fb351655" />

Este modelo es fundamental en sistemas de comunicación, notificaciones y aplicaciones colaborativas.

---

# 1.3 Manejo de Eventos (Event Handlers)

El manejo de eventos consiste en asociar funciones específicas a acciones del usuario.

Un manejador de eventos debe:

1. Capturar la acción.
2. Procesar la información.
3. Modificar el estado interno.
4. Actualizar la interfaz.

Ejemplo aplicado en una calculadora:

```python
def numero_click(e):
    display.value += e.control.data
    page.update()
```

<img width="1571" height="876" alt="image" src="https://github.com/user-attachments/assets/956d1a76-45d5-4db5-8838-f294c71cc8a4" />

### Importancia de `page.update()`

Flet trabaja bajo un modelo de actualización manual. Esto significa que los cambios en los valores internos no se reflejan visualmente hasta que se ejecuta `page.update()`.

Si se omite esta instrucción:
- La interfaz no se refresca.
- El usuario no percibe los cambios.
- Se genera inconsistencia visual.

---

# 1.4 Componentes Gráficos de Control

Los componentes gráficos son elementos visuales interactivos que permiten capturar datos y mostrar información.

Cada componente cumple una función específica dentro de la arquitectura de la interfaz.

## Componentes utilizados

| Componente | Función | Aplicación |
|------------|----------|------------|
| ft.TextField | Entrada de texto libre | Formularios y chat |
| ft.Dropdown | Selección de opciones predeterminadas | Formularios |
| ft.RadioGroup | Selección exclusiva entre alternativas | Formularios |
| ft.Container | Personalización visual | Calculadora |
| ft.Divider | Separación estructural | Organización |
| ft.ElevatedButton | Disparo de acciones | Envío de información |

### Importancia del uso correcto de componentes

Seleccionar el componente adecuado mejora:

- La claridad de la interfaz.
- La experiencia del usuario.
- La eficiencia del sistema.
- La reducción de errores de entrada.

Un diseño adecuado de componentes garantiza coherencia visual y funcional dentro de la aplicación.

---

# Referencias Bibliográficas

- Flet Team. (2024). *Flet: Build Flutter apps in Python*. Disponible en: https://flet.dev/docs/
- Matthes, E. (2023). *Python Crash Course: A Hands-On, Project-Based Introduction to Programming*. No Starch Press.
- Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
