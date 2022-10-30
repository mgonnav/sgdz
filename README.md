# Sistema Gestor de Zapatillas

Sistema gestor de zapatillas para el curso de Sistemas de Informacion CCOMP10-1 2022-2

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

### Requirements
- Docker v20.10.12 (including docker compose)
- Install the dependencies requirements:

```bash
$ pip install -r requirements/local.txt
$ pre-commit install
```

## Local setup
First, you need to build the docker images for the project. You can do it using the following command:
```bash
$ make build
```
It may take some minutes if you run it for the first time.

After that, you can run the containers with:
```bash
$ make up
```

### Migrations and User creation
To run commands that involve calling the `manage.py` file, you can use a temporal django
container where you can execute these commands. Run the following commands to create migrations,
apply them and create a superuser:
```bash
$ make makemigrations
$ make migrate
$ make createsuperuser
```
After that, you will be prompted for the credentials for the new user, as you normally would.
Then, you can login into the admin at [http://0.0.0.0:8000/admin](http://0.0.0.0:8000/admin)
or [http://localhost:8000/admin](http://localhost:8000/admin).

## Basic Commands

### Type checks

Running type checks with mypy:

    $ mypy sgz

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest
