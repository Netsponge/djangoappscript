import os
import subprocess
import sys

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

def style_css(static_dir, style_css_name, content="{font-family: Arial, sans-serif; background-color: #4b0979; color: whitesmoke;}"):
    # Creates the specified directory if it doesn't exist
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)

    # Constructs the full file path
    file_path = os.path.join(static_dir, style_css_name)

    # Creates the file and writes the content (or leaves it empty by default)
    with open(file_path, 'w') as file:
        file.write(content)
    
    print(f"CSS file created: {file_path}")

def create_home_html(templates_dir, file_name):
    # HTML content for home.html with the specified structure
    content = """<!DOCTYPE html>
    {% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
     <link rel="stylesheet" href="{% static 'css/style.css' %} ">
</head>
<body>
    <h1>Hello-World</h1>
    <p>Check out our <a href="/about">About</a> page.</p>
</body>
</html>"""

    # Creates the specified directory if it doesn't exist
    if not os.path.exists(templates_dir):
        os.makedirs(templates_dir)

    # Constructs the full file path
    file_path = os.path.join(templates_dir, file_name)

    # Creates the file and writes the content
    with open(file_path, 'w') as file:
        file.write(content)
    
    print(f"HTML file created: {file_path}")


def create_about_html(templates_dir, file_name):
    # HTML content for home.html with the specified structure
    content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About</title>
</head>
<body>
    <h1>About</h1>
    <p>Check out our <a href="/">Home</a> page.</p>
</body>
</html>"""

# Creates the specified directory if it doesn't exist
    if not os.path.exists(templates_dir):
        os.makedirs(templates_dir)

    # Constructs the full file path
    file_path = os.path.join(templates_dir, file_name)

    # Creates the file and writes the content
    with open(file_path, 'w') as file:
        file.write(content)

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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('about/', views.about),
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
    settings_file_path = os.path.join(core_dir, file_name)
    
    if not os.path.exists(settings_file_path):
        print(f"Le fichier '{settings_file_path}' n'existe pas.")
        return

    with open(settings_file_path, 'r') as file:
        content = file.read()

    new_content = content.replace(
        "'DIRS': []", 
        "'DIRS': ['templates']" 
        #rajouter ####################
        #STATICFILES_DIRS = [
    #os.path.join(BASE_DIR, 'static')
    #et import os au dessus
    # from pathlib import Path  ###################
    )

    with open(settings_file_path, 'w') as file:
        file.write(new_content)

    
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
    create_home_html(TEMPLATES_DIR, "home.html")
    create_about_html(TEMPLATES_DIR, "about.html")  # Creates the home.html file in the templates directory
    create_directory(STATIC_DIR)
    style_css(STATIC_DIR, "style.css")  # Creates the CSS file in the static directory
    create_views_py(CORE_DIR, "views.py")
    update_urls_py(CORE_DIR, "urls.py")
    update_settings(CORE_DIR, "settings.py")
    create_gitignore()
    print(f"'{PROJECT_NAME}' project successfully set up! 🎉")

if __name__ == "__main__":
    setup_project()
