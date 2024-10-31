# -*- coding: utf-8 -*-
import os
import subprocess
import sys
import os
import sys
import subprocess

# Définir le nom du projet Django
yourproject = "my_django_project"  # Remplacez par le nom souhaité pour votre projet

# Créer un nouveau dossier "myapp"
os.makedirs("myapp", exist_ok=True)

# Créer un environnement virtuel pour Python
subprocess.run([sys.executable, "-m", "venv", ".venv"])

# Installer Django dans l'environnement virtuel
subprocess.run(
    [os.path.join(".venv", "bin", "pip"), "install", "django"] 
    if os.name != 'nt' else [os.path.join(".venv", "Scripts", "pip"), "install", "django"]
)

# Créer le projet Django
subprocess.run(["django-admin", "startproject", yourproject])
