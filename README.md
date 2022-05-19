# InventoryTracker

## Prerequisites

Python 3.9

## Running the app on Replit

    click the run button
    sign in with:
      username: admin
      password: password
    success! You can now CRUD items and warehouses.

## Setup db

Run this commands to create tables in the database:

    python manage.py migrate

## Create a super user

You need a user to access the information in the system.

Run this command and follow the short setup

    python manage.py createsuperuser --username admin --email admin@gmail.com --password admin

## Launch the app

To launch the app, run:

    python manage.py runserver

Sign in to the app using the created super user at http://127.0.0.1:8000/

Congratulations! You have access to the inventory items and warehouses.

Have fun!
