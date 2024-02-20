.PHONY: clean data lint requirements sync_data_to_s3 sync_data_from_s3

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
# BUCKET = {{ cookiecutter.s3_bucket }}
# PROFILE = {{ cookiecutter.aws_profile }}
PROJECT_NAME = {{ cookiecutter.repo_name }}

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Make Dataset
data: requirements
	python src/data/make_dataset.py data/raw data/processed

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete


## Set up python interpreter environment
environment:
	conda env create -f environment.yaml

#################################################################################
# Documentation                                                                 #
#################################################################################

docs_md:
	pdoc --pdf src > docs/docs.md

docs_html:
	pdoc --html --output-dir docs src