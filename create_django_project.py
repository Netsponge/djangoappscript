import os
import shutil
import subprocess
import sys

# Nom de base du projet et chemins des dossiers
PROJECT_NAME = "MonProjet"
BASE_DIR = os.path.join(os.getcwd(), PROJECT_NAME)
VENV_DIR = os.path.join(BASE_DIR, 'venv')  # Chemin de l'environnement virtuel
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")  # Dossier des templates
FILES_TO_CREATE = {
    "asgi.py": os.path.join(TEMPLATES_DIR, "asgi.py"),
    "urls.py": os.path.join(TEMPLATES_DIR, "urls.py"),
    "wsgi.py": os.path.join(TEMPLATES_DIR, "wsgi.py"),
}

def create_directory(path):
    """Crée un dossier si il n'existe pas."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Dossier créé: {path}")
    else:
        print(f"Dossier déjà existant: {path}")

def create_file_from_template(file_name, template_path):
    """Crée un fichier à partir d'un template si le fichier n'existe pas."""
    destination = os.path.join(BASE_DIR, file_name)
    if not os.path.exists(destination):
        shutil.copy(template_path, destination)
        print(f"Fichier {file_name} créé à partir de {template_path}.")
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

    # Créer les fichiers principaux du projet à partir des fichiers téléchargés
    for file_name, template_path in FILES_TO_CREATE.items():
        create_file_from_template(file_name, template_path)

    print(f"Projet '{PROJECT_NAME}' configuré avec succès !")

if __name__ == "__main__":
    setup_project()
