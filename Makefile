.DEFAULT_GOAL := help

ifdef TOXENV
TOX := tox -- #to isolate each tox environment if TOXENV is defined
endif

# Generates a help message. Borrowed from https://github.com/pydanny/cookiecutter-djangopackage.
help: ## Display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@perl -nle'print $& if m{^[\.a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

install-dev-dependencies:
	pip install tox

clean: ## Remove generated byte code, coverage reports, and build artifacts
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

python-test-requirements: ## Install test extra requires
	$(TOX) pip install ".[test]"

python-unit-tests: clean python-test-requirements ## Run unit tests
	$(TOX) pytest ./tests

python-acceptance-test: clean python-test-requirements ## Run acceptance tests
	$(TOX) behave

python-quality-test:
	$(TOX) pylint --output-format=colorized tutor_data_manager tests features --rcfile=./setup.cfg

run-tests: python-unit-tests python-acceptance-test python-quality-test
