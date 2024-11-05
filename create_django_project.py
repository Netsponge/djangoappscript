import os
import shutil

# Nom de base du projet et chemins des dossiers
PROJECT_NAME = "MonProjet"
BASE_DIR = os.path.join(os.getcwd(), PROJECT_NAME)
FILES_TO_CREATE = {
    "asgi.py": "/mnt/data/asgi.py",
    "urls.py": "/mnt/data/urls.py",
    "wsgi.py": "/mnt/data/wsgi.py",
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

def setup_project():
    """Crée la structure de base du projet."""
    print(f"Configuration du projet '{PROJECT_NAME}'...")

    # Créer le dossier principal du projet
    create_directory(BASE_DIR)

    # Créer les fichiers principaux du projet à partir des fichiers téléchargés
    for file_name, template_path in FILES_TO_CREATE.items():
        create_file_from_template(file_name, template_path)

    print(f"Projet '{PROJECT_NAME}' configuré avec succès !")

if __name__ == "__main__":
    setup_project()
