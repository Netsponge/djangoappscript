import os
import subprocess
import sys

# Nom du projet et chemins des dossiers
PROJECT_NAME = "my_project"
BASE_DIR = os.getcwd()
VENV_DIR = os.path.join(BASE_DIR, '.venv')  # Chemin de l'environnement virtuel
TEMPLATES_DIR = os.path.join(BASE_DIR, PROJECT_NAME, "templates")  # Dossier des templates

# Contenu du fichier .gitignore
GITIGNORE_CONTENT = """
.venv
*.sqlite3
__pycache__
"""

def create_directory(path):
    """Crée un dossier s'il n'existe pas."""
    os.makedirs(path, exist_ok=True)
    print(f"Dossier créé: {path}")

def create_virtual_environment(path):
    """Crée un environnement virtuel dans le dossier du projet."""
    # Create a virtual environment in "myapp/.venv"
    subprocess.run([sys.executable, "-m", "venv", f"{path}/.venv"])
    # Activate the virtual environment
    activation_cmd = f"source {path}/.venv/bin/activate"
    subprocess.run(activation_cmd, shell=True)

def install_django():
    """Installe Django dans l'environnement virtuel."""
    pip_path = os.path.join(VENV_DIR, 'bin', 'pip')
    subprocess.check_call([pip_path, 'install', 'django'])
    print("Django installé dans l'environnement virtuel.")

def start_django_project():
    """Initialise le projet Django avec `django-admin startproject`."""
    # Vérifier si manage.py existe déjà avant de tenter de créer le projet
    if not os.path.exists(os.path.join(BASE_DIR, 'manage.py')):
        django_admin_path = os.path.join(VENV_DIR, 'bin', 'django-admin')
        subprocess.check_call([django_admin_path, 'startproject', PROJECT_NAME, BASE_DIR])
        print(f"Projet Django '{PROJECT_NAME}' initialisé avec `manage.py`.")
    else:
        print("Le fichier 'manage.py' existe déjà. Le projet Django a déjà été initialisé.")

def create_gitignore():
    """Crée un fichier .gitignore avec les règles spécifiées."""
    gitignore_path = os.path.join(BASE_DIR, ".gitignore")
    with open(gitignore_path, "w") as f:
        f.write(GITIGNORE_CONTENT)
    print(f"Fichier .gitignore créé avec les règles spécifiées.")

def setup_project():
    """Crée la structure de base du projet."""
    print(f"Configuration du projet '{PROJECT_NAME}'...")
    create_virtual_environment(PROJECT_NAME)
    # install_django()
    # start_django_project()
    # create_directory(TEMPLATES_DIR)
    # create_gitignore()
    # print(f"Projet '{PROJECT_NAME}' configuré avec succès !")

if __name__ == "__main__":
    setup_project()
