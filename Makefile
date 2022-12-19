build:
	docker compose -f local.yml build

up:
	docker compose -f local.yml up
	pre-commit install

makemigrations:
	docker compose -f local.yml run --rm django python manage.py makemigrations

migrate:
	docker compose -f local.yml run --rm django python manage.py migrate

createsuperuser:
	docker compose -f local.yml run --rm django python manage.py createsuperuser

test:
	docker compose -f local.yml run --rm django pytest

init_data:
	docker compose -f local.yml run --rm django python manage.py loaddata initial_data/models.json

enter_db:
	docker exec -it sgz_local_postgres psql -U nxzKlUiKpsgjcLAMOxtutZVVjYDuUKEi -W sgz
