COLOUR_GREEN=\033[0;32m
COLOUR_RED=\033[0;31m
COLOUR_BLUE=\033[0;34m
COLOUR_END=\033[0m

run-app:
	@echo "${COLOUR_BLUE}Running app...${COLOUR_END}"
	@aerich upgrade
	@python run.py

run-app-local:
	@echo "${COLOUR_BLUE}Running app in debug mode...${COLOUR_END}"
	@aerich upgrade
	@uvicorn app.main:app --reload

formatter:
	@black .
	@isort .
	@flake8
	@autoflake --remove-all-unused-imports --remove-unused-variables --recursive --in-place --ignore-init-module-imports .

testing:
	@pytest

create_resource:
	@read -p "Enter Resource Name: " RESOURCE \
	&& mkdir ./tests/$${RESOURCE} \
	&& mkdir ./app/main/routes/$${RESOURCE} \
	&& echo '' > ./app/main/routes/$${RESOURCE}/__init__.py \
	&& echo '' > ./app/main/routes/$${RESOURCE}/router.py \
	&& mkdir ./app/infra/database/repositories/$${RESOURCE} \
	&& echo '' > ./app/infra/database/repositories/$${RESOURCE}/__init__.py \
	&& echo '' > ./app/infra/database/repositories/$${RESOURCE}/repository.py \
	&& mkdir ./app/domain/models/$${RESOURCE} \
	&& echo '' > ./app/domain/models/$${RESOURCE}/__init__.py \
	&& echo '' > ./app/domain/models/$${RESOURCE}/model.py \
	&& mkdir ./app/application/schemas/$${RESOURCE} \
	&& echo '' > ./app/application/schemas/$${RESOURCE}/__init__.py \
	&& echo '' > ./app/application/schemas/$${RESOURCE}/schema.py \
	&& mkdir ./app/application/usecases/$${RESOURCE} \
	&& echo '' > ./app/application/usecases/$${RESOURCE}/__init__.py \
	&& echo '' > ./app/application/usecases/$${RESOURCE}/usecase.py \
	&& echo '' > ./tests/$${RESOURCE}/__init__.py \
	&& echo '' > ./tests/$${RESOURCE}/conftest.py \
	&& echo '' > ./tests/$${RESOURCE}/test_model.py \
	&& echo '' > ./tests/$${RESOURCE}/test_router.py \
	&& echo '' > ./tests/$${RESOURCE}/test_schema.py \
	&& echo "$(COLOUR_GREEN)#### RESOURCE $(RESOURCE) HAS BEEN CREATED ####$(COLOUR_END)" \
	&& echo "$(COLOUR_RED)#### DONT FORGET THAT ADD THIS RESOURCES IN app/infra/settings/settings.py ####$(COLOUR_END)"

makemigrations:
	@read -p "set your name migration: " MIGRATION \
	&& aerich migrate --name $${MIGRATION}

migrate:
	@aerich upgrade

init_db:
	@aerich init-db
