import os
import subprocess
import sys
from colorama import Fore, init

# Initialize colorama for color output in the console
init(autoreset=True)

# Project name and directory paths
PROJECT_NAME = "my_project"
BASE_DIR = os.path.join(os.getcwd(), PROJECT_NAME)
CORE_DIR = os.path.join(BASE_DIR, "core")  # Main Django project folder
VENV_DIR = os.path.join(CORE_DIR, '.venv')  # Virtual environment directory in "core"
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")  # Templates directory

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

def create_gitignore():
    # Creates a .gitignore file with the specified rules.
    gitignore_path = os.path.join(BASE_DIR, ".gitignore")
    with open(gitignore_path, "w") as f:
        f.write(GITIGNORE_CONTENT)
    print(".gitignore file created with the specified rules.")

def setup_project():
    # Creates the basic structure of the project.
    print(f"Setting up the '{PROJECT_NAME}' project...")
    create_directory(PROJECT_NAME)
    create_directory(CORE_DIR)
    create_virtual_environment()
    activate_virtual_environment()
    install_django()
    start_django_project()
    create_directory(TEMPLATES_DIR)
    create_gitignore()
    print(Fore.GREEN + f"'{PROJECT_NAME}' project successfully set up! 🎉")

def run_server():
    # Starts the Django development server.
    print("Starting Django development server...")
    
    # Check if virtual environment is set up correctly by verifying if the folder exists
    if not os.path.isdir(VENV_DIR):
        print("Error: The virtual environment is not set up correctly.")
        return

    # Change directory to 'my_project' to execute manage.py
    os.chdir(BASE_DIR)

    # Detect whether the system is Windows or Linux/Mac
    python_command = "python3" if sys.platform != "win32" else "py"
    
    # Execute `python manage.py runserver` to start the server
    try:
        subprocess.run([os.path.join(VENV_DIR, 'bin', python_command), "manage.py", "runserver"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        print("Failed to start the server.")

if __name__ == "__main__":
    setup_project()
    run_server()
