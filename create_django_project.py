# -*- coding: utf-8 -*-
import os
import subprocess
import sys

# Create a new folder "myapp"
os.makedirs("myapp", exist_ok=True)

# Create a virtual environment for python
subprocess.run([sys.executable, "-m", "venv", ".venv"])

# Install django in virtual environment
subprocess.run([os.path.join(".venv", "bin", "pip"), "install", "django"] if os.name != 'nt' else [os.path.join(".venv", "Scripts", "pip"), "install", "django"])

# Create django project
subprocess.run(["django-admin", "startproject", project_name])

# Naviguer dans le dossier du projet
os.chdir(project_name)

# Ajouter ALLOWED_HOSTS dans settings.py
settings_path = os.path.join(project_name, "settings.py")
with open(settings_path, "r") as f:
    settings_content = f.read()

# Insérer ALLOWED_HOSTS
settings_content = settings_content.replace(
    "ALLOWED_HOSTS = []",
    "ALLOWED_HOSTS = ['localhost', '127.0.0.1']"
)

with open(settings_path, "w") as f:
    f.write(settings_content)

# Créer l'application
subprocess.run([os.path.join("..", ".venv", "bin", "python"), "manage.py", "startapp", app_name])

# Créer le fichier .env
with open(".env", "w") as f:
    f.write("SECRET_KEY='votre_cle_secrète'\n")
    f.write("DEBUG=True\n")
    f.write("ALLOWED_HOSTS='localhost, 127.0.0.1'\n")

# Créer le fichier .gitignore
with open(".gitignore", "w") as f:
    f.write(".env\n")
    f.write("__pycache__/\n")
    f.write("*.pyc\n")
    f.write("*.pyo\n")
    f.write("*.pyd\n")
    f.write("db.sqlite3\n")
    f.write(".venv/\n")

# Créer le fichier README.md
with open("README.md", "w") as f:
    f.write(f"# {project_name}\n")
    f.write("Ce projet est un projet Django.\n\n")
    f.write("## Installation\n")
    f.write("```bash\n")
    f.write("pip install -r requirements.txt\n")
    f.write("```\n")

# Créer les dossiers templates et static
os.makedirs(os.path.join(app_name, "templates", app_name), exist_ok=True)
os.makedirs(os.path.join(app_name, "static"), exist_ok=True)

# Créer le fichier base.html
with open(os.path.join(app_name, "templates", app_name, "base.html"), "w") as f:
    f.write("<!DOCTYPE html>\n<html lang=\"fr\">\n<head>\n")
    f.write("    <meta charset=\"UTF-8\">\n")
    f.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
    f.write(f"    <title>{project_name}</title>\n")
    f.write("</head>\n<body>\n")
    f.write("    <h1>Bienvenue dans le projet Django</h1>\n")
    f.write("</body>\n</html>")

# Créer le fichier layout.html
with open(os.path.join(app_name, "templates", app_name, "layout.html"), "w") as f:
    f.write("<!DOCTYPE html>\n<html lang=\"fr\">\n<head>\n")
    f.write("    <meta charset=\"UTF-8\">\n")
    f.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
    f.write(f"    <title>{project_name}</title>\n")
    f.write("</head>\n<body>\n")
    f.write("    <header>\n        <h1>Mon Projet Django</h1>\n    </header>\n")
    f.write("    <main>\n        {% block content %}{% endblock %}\n    </main>\n")
    f.write("    <footer>\n        <p>&copy; 2024 Mon Projet</p>\n    </footer>\n")
    f.write("</body>\n</html>")

print(f"Projet {project_name} créé avec succès !")
print("N'oubliez pas d'activer l'environnement virtuel avec 'source .venv/bin/activate' sur Mac/Linux ou '.venv\\Scripts\\activate' sur Windows.")
