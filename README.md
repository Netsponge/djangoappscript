# djangoappscript is a more advanced script for a django project

### Create a new folder "myapp"

```python
os.makedirs("myapp", exist_ok=True)
```

### Create a virtual environment for python

```python
subprocess.run([sys.executable, "-m", "venv", ".venv"])
```
 ### Install django in virtual environment
 
 ```python
subprocess.run([os.path.join(".venv", "bin", "pip"), "install", "django"] if os.name != 'nt' else [os.path.join(".venv", "Scripts", "pip"), "install", "django"])
```

### Create django project
```python
subprocess.run(["django-admin", "startproject", project_name])
```