# InventoryTracker

## Prerequisites

Python 3.9

## Running the app on Replit

### Creating a new repl

    select `python3` as the langauge
    replace `run` in `.repl` with:

    run = """
    python manage.py migrate --no-input;
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py 
    shell;
    python manage.py runserver 0.0.0.0:3000;
    """

### loading the app

    click the run button
    go to /dashboard to access Django's default UI
    sign in with:
      username: admin
      password: password
    success! You can now CRUD items and warehouses.

## Running the app outside Replit

### Setup db

Run this commands to create tables in the database:

    python manage.py migrate

### Create a super user

You need a user to access the information in the system.

Run this command and follow the short setup

    python manage.py createsuperuser --username admin --email admin@gmail.com --password admin

### Launch the app

To launch the app, run:

    python manage.py runserver

Sign in to the app using the created super user at http://127.0.0.1:8000/dashboard

Congratulations! You have access to the inventory items and warehouses.

Have fun!

## Endpoints

To interact with the app use the following endpoints:

    [ GET ] /dashboard => admin UI

    [ GET ] /api/warehouses => list warehouses
    [ GET ] /api/warehouses/:id => retrieve warehouse
    [ GET ] /api/warehouses/:id/items => list warehouse items
    [ POST ] /api/warehouses/ => create a new warehouse
    [ PATCH ] /api/warehouses/:id/ => update a warehouse
    [ DELETE ] /api/warhouses/:id/ => delete a warehouse

    [ GET ] /api/items => list items
    [ GET ] /api/items/:id => retrieve item
    [ POST ] /api/items/ => create an item
    [ PATCH ] /api/items/:id/ => patch an item
    [ DELETE ] /api/items/:id/ => delete an item
