SHELL := /bin/bash
.SHELLFLAGS = -ec
.ONESHELL:
.SILENT:

.EXPORT_ALL_VARIABLES:
REPO_DIRECTORY:=$(shell pwd)
PYTHONPATH:=${PYTHONPATH}:${REPO_DIRECTORY}

.PHONY: help
help:
	echo "❓ Use \`make <target>'"
	grep -E '^\.PHONY: [a-zA-Z0-9_-]+ .*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = "(: |##)"}; {printf "\033[36m%-30s\033[0m %s\n", $$2, $$3}'

.PHONY: conda_env  ## 🐍 Create a Python conda environment
conda_env:
	conda create --name tp-streamlit-sid python=3.9 -y

.PHONY: dependencies  ## ⏬ Install development dependencies
dependencies:
	pip install -e .[dev]

.PHONY: streamlit  ## 📈 Run streamlit file used_car_deals.py
streamlit:
	streamlit run dashboard.py
