import os
import subprocess
import sys

# root project and name project
PROJECT_NAME = "my_project"
BASE_DIR = os.getcwd() + f"/{PROJECT_NAME}"
VENV_DIR = os.path.join(BASE_DIR, '.venv')  # root of virtual environmpent
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")  # templates folder

GITIGNORE_CONTENT = """
my_project
.venv
*.sqlite3
__pycache__
"""

def create_directory(path):
    """create directory"""
    os.makedirs(path, exist_ok=True)
    print(f"Dossier créé: {path}")

def create_virtual_environment():
    """create virtual environment"""
    subprocess.run([sys.executable, "-m", "venv", VENV_DIR])
    print(f"Environnement virtuel créé dans {VENV_DIR}")

def activate_virtual_environment():
    """Activate virtual environment"""
    activate_script = os.path.join(VENV_DIR, "bin", "activate")
    # TODO: check under Windowss
    if sys.platform.startswith("win"):
        subprocess.run(["cmd", "/c", activate_script], check=True)
    else:
        subprocess.run([".", activate_script, "&&", "echo", "virtual environment activate!"], shell=True, check=True)

def install_django():
    """install django in virtual environment"""
    pip_path = os.path.join(VENV_DIR, 'bin', 'pip')
    subprocess.check_call([pip_path, 'install', 'django'])
    print("Django installé dans l'environnement virtuel.")

def start_django_project():
    """Initialise django project with`django-admin startproject`."""
    django_admin_path = os.path.join(VENV_DIR, 'bin', 'django-admin')
    subprocess.check_call([django_admin_path, 'startproject', "core", BASE_DIR])
    print(f"Projet Django '{PROJECT_NAME}' initialisé avec `manage.py`.")


def git_add_commit_push(commit_message, branch_name):
    try:
        # Exécuter 'git add .'
        subprocess.run(['git', 'add', '.'], check=True)
        print("Fichiers ajoutés avec succès.")

        # Exécuter 'git commit -m "message"'
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        print("Commit effectué avec succès.")

        # Exécuter 'git push origin <branche>'
        subprocess.run(['git', 'push', 'origin', branch_name], check=True)
        print(f"Modifications poussées vers la branche {branch_name} avec succès.")

    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande Git: {e}")


def setup_project():
    # Configuration du projet (exemple)
    print("Configuration du projet 'my_project'...")
    
    # Code de création de votre projet (dossier, fichiers, etc.)
    project_name = "my_project"
    print(f"Dossier créé: {project_name}")



def create_gitignore():
    """create gitignore file"""
    gitignore_path = os.path.join(BASE_DIR, ".gitignore")
    with open(gitignore_path, "w") as f:
        f.write(GITIGNORE_CONTENT)
    print(f"Fichier .gitignore créé avec les règles spécifiées.")


def setup_project():
    """setup project"""
    print(f"Configuration du projet '{PROJECT_NAME}'...")
    create_directory(PROJECT_NAME)
    #create_virtual_environment()
    #activate_virtual_environment()
    #install_django()
    #start_django_project()
    git_add_commit_push("Initial commit", "main")
    # create_directory(TEMPLATES_DIR)
    # create_gitignore()
    # print(f"Projet '{PROJECT_NAME}' configuré avec succès !")

if __name__ == "__main__":
    setup_project()
