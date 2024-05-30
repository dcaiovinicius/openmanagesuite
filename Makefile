VENV_DIR = venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip
FLASK = $(VENV_DIR)/bin/flask

.PHONY: all init run test clean

init:
	python3 -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install python-dotenv

run:
	$(FLASK) --app main run --debug

test:
	$(PYTHON) -m pytest

seeds:
	$(PYTHON) seeds.py

clean:
	rm -rf $(VENV_DIR)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -exec rm -f {} +

all: init
