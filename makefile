# Переменные
COMPOSE = docker-compose
WEB = web
POETRY = poetry run 

build:
	$(COMPOSE) build

up:
	$(COMPOSE) up

down:
	$(COMPOSE) down

restart:
	$(COMPOSE) down && $(COMPOSE) up --build

logs:
	$(COMPOSE) logs -f

migrate:
	$(COMPOSE) exec $(WEB) $(POETRY) python server/manage.py migrate

makemigrations:
	$(COMPOSE) exec $(WEB) $(POETRY) python server/manage.py makemigrations

createsuperuser:
	$(COMPOSE) exec $(WEB) $(POETRY) python server/manage.py createsuperuser

shell:
	$(COMPOSE) exec $(WEB) $(POETRY) python server/manage.py shell

collectstatic:
	$(COMPOSE) exec $(WEB) $(POETRY) python server/manage.py collectstatic --no-input

ps:
	$(COMPOSE) ps

mongosh:
	$(COMPOSE) mongosh