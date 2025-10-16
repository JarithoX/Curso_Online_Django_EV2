# Curso Online - Proyecto EV2

Repositorio base para el proyecto "Plataforma de Cursos Online" (evaluación EV2).

Este proyecto contiene la base de un backend en Django. La versión final de la API se implementará en Node.js + Firebase, pero este repositorio sirve como base Django para administración, pruebas y documentación.

## Estructura del repo
- `cursoOnline/` - configuración del proyecto Django (settings, urls, wsgi, asgi).
- `cursos/`, `estudiantes/`, `profesores/`, `matriculas/`, `evaluaciones/`, `certificados/`, `home/` - aplicaciones Django.
- `requirements.txt` - dependencias del proyecto.
- `.env.example` - ejemplo de variables de entorno.

## Requisitos
- Python 3.10+ (o la versión que tu equipo use)
- git

## Setup (Windows - PowerShell)
1. Clonar el repo:

```powershell
git clone https://github.com/JarithoX/Curso_Online_Django_EV2.git
cd Curso_Online_Django_EV2
```

2. Crear y activar un entorno virtual:

```powershell
python -m venv entorno
.\entorno\Scripts\Activate.ps1
```

3. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

4. Copiar `.env.example` a `.env` y ajustar valores (poner una `SECRET_KEY` real en desarrollo):

```powershell
copy .env.example .env
# editar .env con tu editor preferido
```

5. Migraciones y superuser:

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

6. Levantar el servidor:

```powershell
python manage.py runserver
```

Abre `http://127.0.0.1:8000/admin/` para entrar al admin de Django.

## Notas sobre `.gitignore` y archivos no versionados
- El repositorio evita versionar entornos virtuales (`entorno/`), archivos temporales y la base de datos local (`db.sqlite3`). Esto significa que cualquiera al clonar deberá crear su propio virtualenv e instalar dependencias al clonar.
- Si por alguna razón necesitas compartir una base de datos de ejemplo, crea un script o dump (no subas `db.sqlite3` directamente si contiene datos sensibles).
