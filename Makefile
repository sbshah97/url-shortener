VENV_NAME := venv
VENV_BIN := $(VENV_NAME)/bin
PYTHON := $(VENV_BIN)/python
PIP := $(VENV_BIN)/pip

DOCKER_COMPOSE := docker-compose

.PHONY: venv install test run clean docker-build docker-run

venv:
	@python -m venv $(VENV_NAME)

install: venv
	@$(PIP) install -r requirements.txt

test: install
	@$(PYTHON) test_app.py

run: install
	@$(PYTHON) app.py

clean:
	@rm -rf $(VENV_NAME)
	@find . -name "*.pyc" -exec rm -f {} \;
	@find . -name "__pycache__" -exec rm -rf {} \;

docker-build:
	@$(DOCKER_COMPOSE) build

docker-run:
	@$(DOCKER_COMPOSE) up
