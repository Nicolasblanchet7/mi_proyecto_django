# CUSTOM SHOES 👟

## Descripción del Proyecto
Este es un proyecto de comercio electrónico básico desarrollado con Django que permite a los usuarios visualizar un catálogo de zapatillas, seleccionar un modelo y sus características (talla y color) para agregarlo a un carrito de compras. La aplicación calcula el precio total de los productos en el carrito.

## Tecnologías Utilizadas
- **Backend:** Python 3.11, Django 5.0.
- **Frontend:** HTML5, CSS3.
- **Base de Datos:** SQLite3 (base de datos por defecto de Django).

## Funcionalidades de la Aplicación
- Catálogo de productos con información detallada e imágenes.
- Sistema de carrito de compras funcional.
- Cálculo automático del precio total del carrito.
- Gestión de productos, imágenes y precios a través del panel de administración de Django.

## Instalación y Uso
Para ejecutar este proyecto en tu máquina local, sigue estos pasos:

1.  Clona el repositorio:
    `git clone https://github.com/tu_usuario/tu_repositorio.git`

2.  Navega al directorio del proyecto:
    `cd tu_repositorio`

3.  Crea y activa un entorno virtual (recomendado):
    `python -m venv venv`
    `source venv/bin/activate`  (En Windows usa `venv\Scripts\activate`)

4.  Instala las dependencias:
    `pip install -r requirements.txt`  (Asegúrate de tener un archivo `requirements.txt`)

5.  Aplica las migraciones de la base de datos:
    `python manage.py migrate`

6.  Crea un superusuario para acceder al panel de administración:
    `python manage.py createsuperuser`

7.  Inicia el servidor de desarrollo:
    `python manage.py runserver`

8.  Abre tu navegador y ve a `http://127.0.0.1:8000/`.

## Observaciones y Futuras Mejoras
- **Persistencia del Carrito de Compras por Usuario:** Actualmente, la lógica del carrito utiliza un ID fijo, lo que implica que todos los usuarios comparten el mismo carrito. Para una implementación real, sería necesario vincular cada carrito a un usuario o a una sesión de usuario para garantizar una experiencia de compra individualizada.
- **Sistema de Autenticación:** Se podría agregar un sistema de registro e inicio de sesión para que los usuarios puedan tener perfiles personales y gestionar sus propios carritos y pedidos.
