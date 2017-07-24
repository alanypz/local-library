local-library
=============

A Django web application for a local library. Implements user sessions, custom models, views, forms, templates, and automated tests.

Made with the amazing resources at [MDN](https://developer.mozilla.org/en-US/docs/Learn/Server-side). I highly recommended check it out!


Requirements
------------
* Python 3.4+
* Django 1.11+

Running Locally
---------------

Aquire the project repo.

```
git clone https://github.com/alanypz/local-library.git
```

(Optional) Create and activate a virtual environment.

```
virtualenv -p /usr/local/bin/python3 venv
source venv/bin/activate
```

Install project dependencies.

```
pip install -r requirements.txt
```

(Optional) Create an admin user to access the admin portal.

```
python manage.py createsuperuser
```

Run server.

```
python manage.py runserver
```

The server will load on `http://localhost:8000/`. You can access the admin portal via `http://localhost:8000/admin/`

To exit the virtual environment:

```
deactivate
```


Testing
-------

```
python manage.py test
```

To run tests on the command line:

```
python manage.py shell
```
