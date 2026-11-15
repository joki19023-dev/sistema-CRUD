# Blog Project - Sistema CRUD Completo y Gestión de Imágenes (Django)

Aplicación web de Blog construida con **Django** que implementa un sistema **CRUD (Create, Read, Update, Delete)** completo, persistencia en base de datos **SQLite (`db.sqlite3`)** mediante el ORM, administración desde `/admin` y subida de imágenes mediante formularios dinámicos (`ModelForm`).

## Configuración del Manejo de Imágenes (`ImageField` y `Pillow`)

1. **Dependencia `Pillow` (`requirements.txt`)**:
   - Se incluyó `Pillow` en `requirements.txt` para permitir el procesamiento y validación de imágenes en el campo `models.ImageField`.
   - Instalación:
     ```bash
     pip install -r requirements.txt
     ```
2. **Modelo `Post` (`posts/models.py`)**:
   - Se incorporó el campo `imagen = models.ImageField(upload_to='posts/', null=True, blank=True)` y su respectiva migración (`posts/migrations/0002_post_imagen.py`).
3. **Configuración de `MEDIA_URL` y `MEDIA_ROOT` (`blog_project/settings.py` y `blog_project/urls.py`)**:
   - En `settings.py` se definieron:
     ```python
     MEDIA_URL = '/media/'
     MEDIA_ROOT = BASE_DIR / 'media'
     ```
   - En `blog_project/urls.py` se agregó `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` cuando `settings.DEBUG` está activo para servir las imágenes subidas durante el desarrollo.
4. **Formulario `PostForm` (`posts/forms.py`) y Template (`post_form.html`)**:
   - `PostForm` hereda de `forms.ModelForm` e incluye `['titulo', 'contenido', 'autor', 'estado', 'imagen']`.
   - En `post_form.html`, la etiqueta `<form method="post" enctype="multipart/form-data">` asegura el envío binario del archivo, y las vistas `crear_post` y `editar_post` reciben `request.FILES`.
   - En `post_detail.html`, la imagen se renderiza dinámicamente mediante `{{ post.imagen.url }}`.

## Rutas CRUD Disponibles (`posts/urls.py`)
- **Listar (Index):** `/` (`lista_posts`)
- **Detalle (Detail):** `/post/<int:pk>/` (`detalle_post`)
- **Crear (Create):** `/post/nuevo/` (`crear_post`)
- **Editar (Update):** `/post/<int:pk>/editar/` (`editar_post`)
- **Eliminar (Delete):** `/post/<int:pk>/eliminar/` (`eliminar_post`)

## Cómo entrar al Panel de Administración (`/admin`)
1. Ejecuta `python manage.py runserver` y entra a `http://127.0.0.1:8000/admin/`.
2. Credenciales del superusuario precargado en `db.sqlite3`:
   - **Usuario:** `admin`
   - **Contraseña:** `admin1234`
