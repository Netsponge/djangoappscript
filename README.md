# Djangostart

## Prerequisites

- Ensure that `py` command points to python3 with `py -V` (python 3 or above)
- Ensure that `git` command is working

## Clone this repository

In your terminal

```shell
git clone https://github.com/Netsponge/djangoappscript
cd djangoappscript
```
## Check if the GIT identity is configured
 make sure to have your GitHub PAT (private access token) to push to your project !

 if it's not activate, the script help you to configure your git identity.


## Launch script

In the terminal, launch

```shell
py create_django_project.py
```

## Restart from scratch

```shell
rm -rf my_project && py create_django_project.py
```

## Git commit
 
````shell
git add 
git commit -m "first commit"
````

## Run server 
ensure you are in the good directory to run the command

~/workspace/djangoappscript/my_project$ py manage.py runserver

```shell
py manage.py runserver
```
go to localhost 