# Projet Carotte

Permettre aux gens de trouver des produits sans emballage

Récolter des données sur les utilisateurs

Conquérir le monde

## Install

Install dependencies:

```bash
    pip install -r requirements.txt
```

Initialize database tables:

```bash
$ python manage.py migrate
```

Create a super-user for the admin:

```bash
$ python manage.py createsuperuser
```

## Run the development server

```bash
$ python manage.py runserver
```

> Default port is 8000, if it is already taken, you can start the development server on another port by appending the port number to above command.  For example, to run on port 9000 : `python manage.py runserver 9000`

## Use

Use the webapp by visiting the site at the URL printed by `runserver` (defaults to `http://localhost:8000`).

## Administer the site

Visit `/admin`, using the user credentials you've created for the _super-user_ above, in order to adminster the site : add species, products and sellers.