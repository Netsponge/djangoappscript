import os
import subprocess
import sys

import os
import subprocess
import sys

# Project name and directory paths
PROJECT_NAME = "my_project"
BASE_DIR = os.getcwd() + f"/{PROJECT_NAME}"
VENV_DIR = os.path.join(BASE_DIR, '.venv')  # Virtual environment directory
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")  # Templates directory

# Content for the .gitignore file
GITIGNORE_CONTENT = """
my_project
.venv
*.sqlite3
__pycache__
"""

def create_directory(path):
    """Creates a directory if it does not exist."""
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")

def create_virtual_environment():
    """Creates a virtual environment in the project folder."""
    subprocess.run([sys.executable, "-m", "venv", VENV_DIR])
    print(f"Virtual environment created at {VENV_DIR}")

def activate_virtual_environment():
    """Activates the virtual environment in a subprocess."""
    venv_dir = '/Users/jeanbaptistemarrec/workspace/djangoappscript/my_project/.venv'
    activate_script = os.path.join(venv_dir, 'bin', 'activate')

    # Check if the activation script exists
    if not os.path.isfile(activate_script):
        print(f"The activation script was not found at {activate_script}")
        return

    # Execute the activation script in a bash subprocess
    subprocess.run(f"source {activate_script} && echo 'Virtual environment activated'", shell=True, executable='/bin/bash')

    print("The virtual environment has been activated in the subprocess.")

def install_django():
    """Installs Django in the virtual environment."""
    pip_path = os.path.join(VENV_DIR, 'bin', 'pip')
    subprocess.check_call([pip_path, 'install', 'django'])
    print("Django installed in the virtual environment.")

def start_django_project():
    """Initializes the Django project with `django-admin startproject`."""
    django_admin_path = os.path.join(VENV_DIR, 'bin', 'django-admin')
    subprocess.check_call([django_admin_path, 'startproject', "core", BASE_DIR])
    print(f"Django project '{PROJECT_NAME}' initialized with `manage.py`.")


def git_add_commit(commit_message, branch_name):
    try:
        # Run 'git add .' to add all modified files
        subprocess.run(['git', 'add', '.'], check=True)
        print("Files added successfully.")

        # Check if there are changes before attempting a commit
        status = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        if status.stdout.strip():  # If the output is not empty, there are changes
            # Run 'git commit -m "message"'
            subprocess.run(['git', 'commit', '-m', commit_message], check=True)
            print("Commit successful.")
        else:
            print("No changes to commit.")

    except subprocess.CalledProcessError as e:
        print(f"Error while executing the Git command: {e}")

def create_gitignore():
    """Creates a .gitignore file with the specified rules."""
    gitignore_path = os.path.join(BASE_DIR, ".gitignore")
    with open(gitignore_path, "w") as f:
        f.write(GITIGNORE_CONTENT)
    print(f".gitignore file created with the specified rules.")

def setup_project():
    """Creates the basic structure of the project."""
    print(f"Setting up the '{PROJECT_NAME}' project...")
    create_directory(PROJECT_NAME)
    create_virtual_environment()
    activate_virtual_environment()
    install_django()
    start_django_project()
    git_add_commit("success")
    create_directory(TEMPLATES_DIR)
    # create_gitignore()
    # print(f"'{PROJECT_NAME}' project successfully set up!")

if __name__ == "__main__":
    setup_project()
