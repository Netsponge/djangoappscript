import os
import subprocess
import sys

# Nom du projet et chemins des dossiers
PROJECT_NAME = "my_project"
BASE_DIR = os.getcwd() + f"/{PROJECT_NAME}"
VENV_DIR = os.path.join(BASE_DIR, '.venv')  # Chemin de l'environnement virtuel
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")  # Dossier des templates

# Contenu du fichier .gitignore
GITIGNORE_CONTENT = """
my_project
.venv
*.sqlite3
__pycache__
"""

def create_directory(path):
    """Crée un dossier s'il n'existe pas."""
    os.makedirs(path, exist_ok=True)
    print(f"Dossier créé: {path}")

def create_virtual_environment():
    """Crée un environnement virtuel dans le dossier du projet."""
    subprocess.run([sys.executable, "-m", "venv", VENV_DIR])
    print(f"Environnement virtuel créé dans {VENV_DIR}")

def activate_virtual_environment():
    """Utilise Python de l'environnement virtuel directement."""
    python_executable = os.path.join(VENV_DIR, "bin", "python")

    # Vérifie si l'exécutable Python existe dans l'environnement virtuel
    if not os.path.isfile(python_executable):
        print("L'exécutable Python n'est pas trouvé dans l'environnement virtuel.")
        return
    
    print(f"Utilisation de Python depuis l'environnement virtuel : {python_executable}")


def install_django():
    """Installe Django dans l'environnement virtuel."""
    pip_path = os.path.join(VENV_DIR, 'bin', 'pip')
    subprocess.check_call([pip_path, 'install', 'django'])
    print("Django installé dans l'environnement virtuel.")

def start_django_project():
    """Initialise le projet Django avec `django-admin startproject`."""
    django_admin_path = os.path.join(VENV_DIR, 'bin', 'django-admin')
    subprocess.check_call([django_admin_path, 'startproject', "core", BASE_DIR])
    print(f"Projet Django '{PROJECT_NAME}' initialisé avec `manage.py`.")

def create_gitignore():
    """Crée un fichier .gitignore avec les règles spécifiées."""
    gitignore_path = os.path.join(BASE_DIR, ".gitignore")
    with open(gitignore_path, "w") as f:
        f.write(GITIGNORE_CONTENT)
    print(f"Fichier .gitignore créé avec les règles spécifiées.")


def setup_project():
    """Crée la structure de base du projet."""
    print(f"Configuration du projet '{PROJECT_NAME}'...")
    create_directory(PROJECT_NAME)
    create_virtual_environment()
    activate_virtual_environment()
    install_django()
    start_django_project()
    # add and commit new files
    # create_directory(TEMPLATES_DIR)
    # create_gitignore()
    # print(f"Projet '{PROJECT_NAME}' configuré avec succès !")

if __name__ == "__main__":
    setup_project()