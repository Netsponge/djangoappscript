import os
import shutil
import subprocess
import sys

# Nom de base du projet et chemins des dossiers
PROJECT_NAME = "my_project"
BASE_DIR = os.path.join(os.getcwd(), PROJECT_NAME)
VENV_DIR = os.path.join(BASE_DIR, 'venv')  # Chemin de l'environnement virtuel
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")  # Dossier des templates
FILES_TO_CREATE = {
    "asgi.py": """import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MonProjet.settings')
application = get_asgi_application()
""",
    "urls.py": """from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
""",
    "wsgi.py": """import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MonProjet.settings')
application = get_wsgi_application()
""",
}

def create_directory(path):
    """Crée un dossier si il n'existe pas."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Dossier créé: {path}")
    else:
        print(f"Dossier déjà existant: {path}")

def create_file_from_template(file_name, template_content):
    """Crée un fichier à partir d'un contenu template si le fichier n'existe pas."""
    destination = os.path.join(BASE_DIR, file_name)
    if not os.path.exists(destination):
        with open(destination, 'w') as f:
            f.write(template_content)
        print(f"Fichier {file_name} créé avec du contenu par défaut.")
    else:
        print(f"Fichier {file_name} déjà existant.")

def create_virtual_environment():
    """Crée un environnement virtuel dans le dossier du projet."""
    if not os.path.exists(VENV_DIR):
        subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])
        print(f"Environnement virtuel créé à: {VENV_DIR}")
    else:
        print(f"Environnement virtuel déjà existant à: {VENV_DIR}")

def setup_project():
    """Crée la structure de base du projet."""
    print(f"Configuration du projet '{PROJECT_NAME}'...")

    # Créer le dossier principal du projet
    create_directory(BASE_DIR)

    # Créer le dossier des templates
    create_directory(TEMPLATES_DIR)

    # Créer l'environnement virtuel
    create_virtual_environment()

    # Créer les fichiers principaux du projet à partir des contenus définis
    for file_name, template_content in FILES_TO_CREATE.items():
        create_file_from_template(file_name, template_content)

    print(f"Projet '{PROJECT_NAME}' configuré avec succès !")

if __name__ == "__main__":
    setup_project()
