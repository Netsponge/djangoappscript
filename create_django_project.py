import os
import json
import subprocess
import sys
# from colorama import Fore, init
# init()

# Project name and directory paths
PROJECT_NAME = "my_project"
BASE_DIR = os.path.join(os.getcwd(), PROJECT_NAME)
CORE_DIR = os.path.join(BASE_DIR, "core")  # Main Django project folder
VENV_DIR = os.path.join(BASE_DIR, '.venv')  # Virtual environment directory in "core"
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")  # Templates directory
STATIC_DIR = os.path.join(BASE_DIR, "static")  # Static files directory

# Content for the .gitignore file
GITIGNORE_CONTENT = """
my_project
core/.venv
*.sqlite3
__pycache__
"""

def create_directory(path):
    # Creates a directory if it does not exist.
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")

def create_virtual_environment():
    # Creates a virtual environment in the project folder.
    subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True)
    print(f"Virtual environment created at {VENV_DIR}")

def activate_virtual_environment():
    # Activates the virtual environment in a subprocess.
    activate_script = os.path.join(VENV_DIR, 'bin', 'activate')

    # Check if the activation script exists.
    if not os.path.isfile(activate_script):
        print(f"The activation script was not found at {activate_script}")
        return

    # Activate the virtual environment using `source`
    subprocess.run(f"source {activate_script} && echo 'Virtual environment activated'", shell=True, executable='/bin/bash')
    print("The virtual environment has been activated.")

def install_django():
    # Installs Django in the virtual environment.
    pip_path = os.path.join(VENV_DIR, 'bin', 'pip')
    subprocess.check_call([pip_path, 'install', 'django'])
    print("Django installed in the virtual environment.")

def start_django_project():
    """Initializes the Django project with `django-admin startproject`."""
    django_admin_path = os.path.join(VENV_DIR, 'bin', 'django-admin')
    subprocess.check_call([django_admin_path, 'startproject', "core", BASE_DIR])
    print(f"Django project '{PROJECT_NAME}' initialized with `manage.py`.")

def update_allowed_hosts(settings_file):
    # Adds "127.0.0.1" to the ALLOWED_HOSTS in settings.py
    if not os.path.exists(settings_file):
        print(f"ERROR: The file '{settings_file}' does not exist.")
        return

    with open(settings_file, 'r') as file:
        content = file.readlines()

    # Modify the ALLOWED_HOSTS line
    for i, line in enumerate(content):
        if line.strip().startswith("ALLOWED_HOSTS"):
            content[i] = "ALLOWED_HOSTS = ['127.0.0.1']\n"
            break

    # Write the updated content back to settings.py
    with open(settings_file, 'w') as file:
        file.writelines(content)
    
    print("Updated ALLOWED_HOSTS to include '127.0.0.1' in settings.py")

class CSSManager:
    def __init__(self, project_name='my_project', static_dir='static'):
        """
        Initialise le gestionnaire de styles CSS
        """
        self.base_dir = os.getcwd()
        self.project_dir = os.path.join(self.base_dir, project_name)
        self.static_dir = os.path.join(self.project_dir, static_dir)
        self.css_dir = os.path.join(self.static_dir, 'css')
        
        # Crée les dossiers nécessaires
        os.makedirs(self.css_dir, exist_ok=True)

    def load_styles_from_json(self, json_file='styles_config.json'):
        """
        Charge et crée les fichiers CSS depuis un fichier JSON
        """
        filepath = os.path.join(self.base_dir, json_file)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                styles = json.load(file)
            
            for filename, content in styles.items():
                self.create_style(filename, content)
            
            print("Tous les fichiers CSS ont été créés avec succès.")
        
        except FileNotFoundError:
            print(f"Fichier de configuration {json_file} non trouvé.")
        except json.JSONDecodeError:
            print("Erreur de décodage du fichier JSON.")

    def create_style(self, filename, content):
        """
        Crée un fichier CSS dans le dossier static/css
        """
        filepath = os.path.join(self.css_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"Fichier CSS créé : {filename}")


class HTMLTemplateManager:
    def __init__(self, project_name='my_project', templates_dir='templates'):
        """
        Initialise le gestionnaire de templates
        """
        self.base_dir = os.getcwd()
        self.project_dir = os.path.join(self.base_dir, project_name)
        self.templates_dir = os.path.join(self.project_dir, templates_dir)
        
        # Crée le dossier projet et templates s'ils n'existent pas
        os.makedirs(self.templates_dir, exist_ok=True)

    def load_templates_from_json(self, json_file='templates_config.json'):
        """
        Charge et crée les templates depuis un fichier JSON
        """
        filepath = os.path.join(self.base_dir, json_file)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                templates = json.load(file)
            
            for filename, content in templates.items():
                self.create_template(filename, content)
            
            print("Tous les templates ont été créés avec succès.")
        
        except FileNotFoundError:
            print(f"Fichier de configuration {json_file} non trouvé.")
        except json.JSONDecodeError:
            print("Erreur de décodage du fichier JSON.")

    def create_template(self, filename, content):
        """
        Crée un fichier HTML dans le dossier templates du projet
        """
        filepath = os.path.join(self.templates_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"Template créé : {filename}")


def create_gitignore():
    # Creates a .gitignore file with the specified rules.
    gitignore_path = os.path.join(BASE_DIR, ".gitignore")
    with open(gitignore_path, "w") as f:
        f.write(GITIGNORE_CONTENT)
    print(".gitignore file created with the specified rules.")



import os

def create_views_py(core_dir, file_name):
    if not os.path.exists(core_dir):
        os.makedirs(core_dir)
    file_path = os.path.join(core_dir, file_name)

    default_content = """# views.py
# This is the views file for the core directory

#from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    #return HttpResponse("Home.")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("About page.")
    return render(request, 'about.html')

"""
    with open(file_path, 'w') as file:
        file.write(default_content)



import os

def update_urls_py(core_dir, file_name):
    # content
    new_content = """from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('about/', views.about),
    path('posts/', include('posts.urls'))
] 
"""
    file_path = os.path.join(core_dir, file_name)

    if os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write(new_content)
        print(f"Le fichier '{file_name}' dans le dossier '{core_dir}' a été mis à jour avec les nouveaux liens.")
    else:
        print(f"Le fichier '{file_path}' n'existe pas.")


def update_settings(core_dir, file_name):
    # Construit le chemin complet du fichier settings.py
    settings_file_path = os.path.join(core_dir, file_name)
    
    if not os.path.exists(settings_file_path):
        print(f"Le fichier '{settings_file_path}' n'existe pas.")
        return

   
    with open(settings_file_path, 'r') as file:
        content = file.readlines()

    
    import_os_present = False
    new_lines = []

  
    for line in content:
        if line.strip() == "import os":
            import_os_present = True
        
      
        if not import_os_present and line.startswith("import"):
            new_lines.append("import os\n")  
            import_os_present = True
        
        new_lines.append(line)

    if not import_os_present:
        new_lines.insert(0, "import os\n")

   
    for i, line in enumerate(new_lines):
        if "'DIRS': []" in line:
            new_lines[i] = "            'DIRS': ['templates'],\n"
        elif "'DIRS':" in line and "templates" not in line:
            new_lines[i] = "            'DIRS': ['templates'],\n"
    
    staticfiles_found = False
    for i, line in enumerate(new_lines):
        if "STATICFILES_DIRS" in line:
            staticfiles_found = True
            break

    if not staticfiles_found:
        staticfiles_config = "\nSTATICFILES_DIRS = [\n    os.path.join(BASE_DIR, 'static')\n]\n"
        new_lines.append(staticfiles_config)
    
    with open(settings_file_path, 'w') as file:
        file.writelines(new_lines)


    
def setup_project():
    # Creates the basic structure of the project.
    print(f"Setting up the '{PROJECT_NAME}' project...")
    create_directory(PROJECT_NAME)
    create_directory(CORE_DIR)
    create_virtual_environment()
    activate_virtual_environment()
    install_django()
    start_django_project()
    settings_file = os.path.join(CORE_DIR, "settings.py")
    update_allowed_hosts(settings_file) 
    create_directory(TEMPLATES_DIR)
    template_manager = HTMLTemplateManager()
    template_manager.load_templates_from_json()
    css_manager = CSSManager()
    css_manager.load_styles_from_json()
    create_views_py(CORE_DIR, "views.py")
    update_urls_py(CORE_DIR, "urls.py")
    update_settings(CORE_DIR, "settings.py")
    create_gitignore()
    print(f"'{PROJECT_NAME}' project successfully set up! 🎉")
    print(f"'{PROJECT_NAME}' now type, cd my_project 📂")
    print(f"'{PROJECT_NAME}' and run the server with py manage.py runserver 🔍")

if __name__ == "__main__":
    setup_project()
