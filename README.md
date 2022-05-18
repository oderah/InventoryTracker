# InventoryTracker

## Prerequisites

Docker

Python 3.9

## Setup python environment

Run the following commands:

    pipenv shell
    pipenv install

## Setup postgres

Run the following commands:

    docker run --name inventory -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
    docker exec -it inventory psql -U postgres -c "create database inventory"
    docker exec -it inventory psql -U postgres inventory -c "GRANT ALL PRIVILEGES ON DATABASE inventory TO postgres"

Change the database connection settings in tracker/settings.py

    change NAME, USER, and PASSWORD to match your database info

Run this command to create tables in the database:

    python manage.py migrate

## Create a super user

You need a user to access the information in the system.

Run this command and follow the short setup

    python manage.py createsuperuser

## Launch the app

To launch the app, run:

    python manage.py runserver

Sign in to the app using the created super user at http://127.0.0.1:8000/admin/

Congratulations! You have access to the inventory items and warehouses.

Have fun!
