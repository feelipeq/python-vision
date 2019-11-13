settings=src.settings.base

ifdef SIMPLE_SETTINGS
	settings=$(SIMPLE_SETTINGS)
else
	export SIMPLE_SETTINGS=$(settings)
endif

export PYTHONPATH=$(shell pwd)/src
export GOOGLE_APPLICATION_CREDENTIALS=/home/osboxes/secrets/Quickstart-09f65f8f8289.json



clean: ## Clean local environment
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@rm -f *.log

format:
	black .

install:
	pip3 install -r requirements.txt

run:
	python3 $(PYTHONPATH)/main.py
