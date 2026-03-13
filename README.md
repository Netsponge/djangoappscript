
# 🔍 djangoappscript

> Script Python de scraping automatisé des coordonnées d'artisans pour intégration dans un CRM de prospection commerciale.

## 📌 À quoi ça sert ?

Ce script automatise la collecte de coordonnées professionnelles d'artisans (nom, adresse, email, coordonnées géographiques) et les intègre directement dans un CRM pour faciliter la prospection commerciale B2B.

**Problème résolu :** la recherche et la saisie manuelle de contacts prennent des heures. Ce script le fait en quelques minutes.

## ⚙️ Fonctionnalités

- 🕷️ **Scraping automatisé** des coordonnées d'artisans (nom, adresse, téléphone, email)
- 📍 **Enrichissement géographique** : extraction et normalisation des coordonnées géolocalisées
- 🗄️ **Intégration CRM** : import direct des données dans une base Django (modèles prospects)
- 🔄 **Pipeline de données** : extraction → nettoyage → enrichissement → import

## 🛠️ Stack technique

- Python 3
- Django (modèles & ORM)
- Scraping (requests / BeautifulSoup)
- Géolocalisation
- PostgreSQL / SQLite

## 🚦 Utilisation

```bash
git clone https://github.com/Netsponge/djangoappscript
cd djangoappscript
pip install -r requirements.txt
python script.py
```

## 💡 Contexte

Projet développé dans le cadre d'un besoin métier concret : alimenter un CRM B2B avec des leads qualifiés dans le secteur de l'artisanat, sans saisie manuelle. Le script inclut la gestion des données géolocalisées pour permettre un ciblage géographique de la prospection.

---

Made with 🐍 by [Jean-Baptiste Marrec](https://github.com/Netsponge)

## Prerequisites

- Ensure that `py` command points to python3 with `py -V` (python 3 or above)
- Ensure that `git` command is working

## Clone this repository

In your terminal

```shell
git clone https://github.com/Netsponge/djangoappscript
cd djangoappscript
```

## Launch script

In the terminal, launch

```shell
py create_django_project.py
```

## Restart from scratch

```shell
rm -rf my_project && py create_django_project.py
```

## The server is listeneing to port:

 http://127.0.0.1:8000/

The install worked successfully! Congratulations!

## Git commit
 
````shell
git add .
git commit -m "first commit"
````
## py manage 
