import os
import subprocess
import sys
from colorama import Fore, init

# Initialisation de colorama pour afficher des couleurs dans la console
init(autoreset=True)

# Nom du projet et chemins de répertoire
PROJECT_NAME = "my_project"
BASE_DIR = os.path.join(os.getcwd(), PROJECT_NAME)
CORE_DIR = os.path.join(BASE_DIR, "core")  # Dossier du projet Django principal
VENV_DIR = os.path.join(CORE_DIR, '.venv')  # Dossier de l'environnement virtuel
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")  # Dossier de templates

# Contenu du fichier .gitignore
GITIGNORE_CONTENT = """
my_project
.venv
*.sqlite3
__pycache__
"""

def create_directory(path):
    os.makedirs(path, exist_ok=True)
    print(Fore.YELLOW + f"Dossier créé : {path}")

def create_virtual_environment():
    subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True)
    print(Fore.GREEN + f"Environnement virtuel créé dans {VENV_DIR}")

def activate_virtual_environment():
    # Active l'environnement virtuel dans un sous-processus
    activate_script = os.path.join(VENV_DIR, 'bin', 'activate')

    if not os.path.isfile(activate_script):
        print(Fore.RED + f"Le script d'activation est introuvable : {activate_script}")
        return

    subprocess.run(f"source {activate_script} && echo 'Environnement virtuel activé'", shell=True, executable='/bin/bash')
    print(Fore.GREEN + "L'environnement virtuel a été activé.")

def install_django():
    pip_path = os.path.join(VENV_DIR, 'bin', 'pip')
    subprocess.check_call([pip_path, 'install', 'django'])
    print(Fore.GREEN + "Django installé dans l'environnement virtuel.")

def start_django_project():
    django_admin_path = os.path.join(VENV_DIR, 'bin', 'django-admin')
    subprocess.check_call([django_admin_path, 'startproject', "core", BASE_DIR])
    print(Fore.GREEN + f"Projet Django '{PROJECT_NAME}' initialisé avec `manage.py`.")

def create_gitignore():
    gitignore_path = os.path.join(BASE_DIR, ".gitignore")
    with open(gitignore_path, "w") as f:
        f.write(GITIGNORE_CONTENT)
    print(Fore.GREEN + ".gitignore créé avec les règles spécifiées.")

def setup_project():
    print(Fore.YELLOW + f"Configuration du projet '{PROJECT_NAME}'...")
    create_directory(PROJECT_NAME)
    create_directory(CORE_DIR)
    create_virtual_environment()
    activate_virtual_environment()
    install_django()
    start_django_project()
    create_directory(TEMPLATES_DIR)
    create_gitignore()
    print(Fore.GREEN + f"Projet '{PROJECT_NAME}' configuré avec succès ! 🎉")

def run_server():
    print(Fore.YELLOW + "Démarrage du serveur de développement Django...")
    
    if not os.path.isdir(VENV_DIR):
        print(Fore.RED + "Erreur : L'environnement virtuel n'est pas configuré.")
        return
    
    os.chdir(BASE_DIR)
    python_command = "python3" if sys.platform != "win32" else "py"
    
    try:
        subprocess.run([os.path.join(VENV_DIR, 'bin', python_command), "manage.py", "runserver"], check=True)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Erreur lors du démarrage du serveur : {e}")

if __name__ == "__main__":
    setup_project()
    run_server()
