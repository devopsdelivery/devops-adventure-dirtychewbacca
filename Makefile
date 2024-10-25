help: ## Show help
	# From https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


install:
	poetry install
	poetry add ruff
	poetry add black

#cria ambiente virtual
shell:
	poetry shell


init:
	poetry init -C app

add:
	poetry add fastapi uvicorn asyncpg python-decouple -C app



alembic_init-migrations: ## Init alembic
	poetry run alembic init migrations

alembic_migrate: ## Migrate
	poetry run alembic revision --autogenerate -m "Add table"

alembic_upgrade: ## Upgrade
	poetry run alembic upgrade head



#makemigrations:
#	poetry run python databse.py makemigrations

migrate:
	poetry run python databse.py migrate

collectstatic:
	poetry run python databse.py collectstatic -c --noinput

run_server: makemigrations migrate collectstatic
	poetry run python manage.py runserver

#cria amb virtual que existe apenas durante a execução do script python
run_app_main:
	poetry run python app/main.py

run_uvicorn: ## Run the FastAPI server
	poetry run uvicorn app.main:app --reload




build-postgresql:
	docker build -t postgres ./postgres

build-app:
	docker build -t app ./app

build-all:
	docker build -t app ./app
	docker build -t postgres ./postgres

run-postgres:
	docker run -d --rm --name postgres --network app-network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -p 5432:5432 postgres

run-app: build-all run-postgres
	docker run -it --rm --name app --network app-network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_HOST=postgres -e POSTGRES_DB=postgres -v ${PWD}/app:/app -p 8000:8000 app poetry run uvicorn src.app:app --host 0.0.0.0 --port 8000


stop-all:
	docker stop app postgres



# Variables
APP_NAME = app_api
POSTGRES_NAME = postgres
DOCKER_COMPOSE = docker-compose
COMPOSE_FILE = docker-compose.yml

# Targets
.PHONY: all build run push clean

# Default target
all: build

# Build the images
build_compose:
	@$(DOCKER_COMPOSE) build

# Run the services
run_compose:
	@$(DOCKER_COMPOSE) up

# Push the images to Docker Hub
push_compose:
	@$(DOCKER_COMPOSE) push

# Clean up Docker containers and images
clean_compose:
	@$(DOCKER_COMPOSE) down
	@docker rmi $(APP_NAME) $(POSTGRES_NAME) || true

# Extract inspection data from the services to a file
inspect:
	@docker inspect $(APP_NAME) > $(APP_NAME)_inspect.json || true
	@docker inspect $(POSTGRES_NAME) > $(POSTGRES_NAME)_inspect.json || true