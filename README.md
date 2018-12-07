Projet Carotte

==============

Permettre aux gens de trouver des produits sans emballage

R�colter des donn�es sur les utilisateurs

Conqu�rir le monde

Install
=======

Install dependencies:

.. code-block:: bash

    pip install -r requirements.txt

Initialize database tables:

.. code-block:: bash

    python manage.py migrate

Create a super-user for the admin:

.. code-block:: bash

    python manage.py createsuperuser

Run
===

.. code-block:: bash

    python manage.py runserver