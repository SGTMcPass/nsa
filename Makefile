# Makefile for NASA Simulation Agents
# =================================

# Configuration
# ------------
YAML_FILE=profiles/prompt/nasa_simulation_prompt_assistant.yaml
CONVERT_SCRIPT=tools/convert_prompt_profile.py
JSON_FILE=profiles/prompt/nasa_simulation_prompt_assistant.json
MD_FILE=profiles/prompt/nasa_simulation_prompt_assistant.md
MAX_RETRIES=3
PYTHON=python3
PIP=pip
PYTEST=pytest
PRECOMMIT=pre-commit

# Colors
RED=\033[0;31m
GREEN=\033[0;32m
YELLOW=\033[0;33m
NC=\033[0m # No Color

# Phony targets
.PHONY: all help setup install dev-install format lint type test test-cov pre-commit \
	clean clean-pyc clean-build clean-test clean-all \
	list validate export convert convert-profile validate-prompts

# Help
# ----
help:
	@echo "\n${YELLOW}NASA Simulation Agents - Development Tools${NC}\n"
	@echo "Available targets:"
	@echo "  ${GREEN}setup${NC}           - Set up development environment"
	@echo "  ${GREEN}install${NC}         - Install package in development mode"
	@echo "  ${GREEN}dev-install${NC}     - Install development dependencies"
	@echo "  ${GREEN}format${NC}          - Format code with Black and isort"
	@echo "  ${GREEN}lint${NC}            - Run linters (ruff, flake8, black, isort)"
	@echo "  ${GREEN}type${NC}            - Run type checking with mypy"
	@echo "  ${GREEN}test${NC}            - Run tests"
	@echo "  ${GREEN}test-cov${NC}        - Run tests with coverage report"
	@echo "  ${GREEN}pre-commit${NC}      - Run pre-commit on all files"
	@echo "  ${GREEN}clean${NC}           - Remove all build, test, and Python artifacts"
	@echo "  ${GREEN}clean-pyc${NC}       - Remove Python file artifacts"
	@echo "  ${GREEN}clean-build${NC}     - Remove build artifacts"
	@echo "  ${GREEN}clean-test${NC}      - Remove test artifacts"
	@echo "  ${GREEN}clean-all${NC}       - Remove all generated files"

# Development Setup
# ----------------
setup:
	@echo "${YELLOW}🚀 Setting up development environment...${NC}"
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e .[dev]
	$(PRECOMMIT) install

install:
	@echo "${YELLOW}📦 Installing package in development mode...${NC}"
	$(PIP) install -e .

dev-install:
	@echo "${YELLOW}🔧 Installing development dependencies...${NC}"
	$(PIP) install -e ".[dev]"

# Code Quality
# -----------
format:
	@echo "${YELLOW}🎨 Formatting code...${NC}"
	black .
	isort .

lint:
	@echo "${YELLOW}🔍 Running linters...${NC}"
	echo "${YELLOW}Running ruff...${NC}"
	ruff check . --fix
	echo "${YELLOW}Running black...${NC}"
	black --check .
	echo "${YELLOW}Running isort...${NC}"
	isort --check-only .
	echo "${YELLOW}Running flake8...${NC}"
	flake8 .

lint-fix:
	@echo "${YELLOW}🔧 Fixing linting issues...${NC}"
	ruff check . --fix
	black .
	isort .

type:
	@echo "${YELLOW}🔍 Running type checking...${NC}"
	mypy .

# Testing
# -------
test:
	@echo "${YELLOW}🧪 Running tests...${NC}"
	$(PYTEST) -v tests/

test-cov:
	@echo "${YELLOW}📊 Running tests with coverage...${NC}"
	$(PYTEST) --cov=./ --cov-report=term-missing --cov-report=xml tests/

# Pre-commit
# ----------
pre-commit:
	@echo "${YELLOW}✅ Running pre-commit on all files...${NC}"
	$(PRECOMMIT) run --all-files

# Cleanup
# -------
clean: clean-pyc clean-build clean-test

clean-pyc:
	@echo "${YELLOW}🧹 Removing Python file artifacts...${NC}"
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type f -name '*.py[co]' -exec rm -f {} +
	find . -type f -name '*~' -exec rm -f {} +

clean-build:
	@echo "${YELLOW}🧹 Removing build artifacts...${NC}"
	rm -rf build/ dist/ *.egg-info/ .eggs/ .pytest_cache/ .mypy_cache/ .ruff_cache/

clean-test:
	@echo "${YELLOW}🧹 Removing test artifacts...${NC}"
	rm -rf .coverage htmlcov/ .pytest_cache/ test-results/

clean-all: clean
	@echo "${YELLOW}🧹 Removing all generated files...${NC}"
	rm -rf .tox/ .venv/ venv/ env/ .mypy_cache/ .pytest_cache/ .ruff_cache/

# Existing Prompt Management Commands
# ----------------------------------
list:
	@echo "${YELLOW}📋 Listing all prompts...${NC}"
	@$(PYTHON) tools/load_prompt.py --list

validate:
	@echo "${YELLOW}🔍 Validating prompt registry...${NC}"
	@$(PYTHON) tools/load_prompt.py --validate

export:
	@echo "${YELLOW}📤 Exporting prompt by ID (set ID= and FILE=)...${NC}"
	@test -n "$(ID)" && test -n "$(FILE)" || (echo "${RED}❌ You must set ID and FILE${NC}"; exit 1)
	@$(PYTHON) tools/load_prompt.py --id $(ID) --export $(FILE)

convert:
	@echo "${YELLOW}🔄 Converting JSON assistant profile to YAML and Markdown...${NC}"
	@$(PYTHON) tools/convert_prompt_profile.py profiles/prompt/nasa_simulation_prompt_assistant.json

validate-prompts:
	@echo "${YELLOW}🔎 Validating prompt structure and metadata...${NC}"
	@$(PYTHON) tools/validate_prompt_files.py

convert-profile:
	@echo "${YELLOW}🚀 Converting YAML to JSON and Markdown...${NC}"
	@$(PYTHON) $(CONVERT_SCRIPT) $(YAML_FILE)
	@echo "${YELLOW}🔎 Running pre-commit validation on generated files...${NC}"
	@retries=0; \
	while ! $(PRECOMMIT) run --all-files; do \
		retries=$$((retries + 1)); \
		if [ $$retries -ge $(MAX_RETRIES) ]; then \
			echo "${RED}❌ Pre-commit failed after $(MAX_RETRIES) attempts.${NC}"; \
			exit 1; \
		fi; \
		echo "${YELLOW}🔄 Pre-commit failed. Retrying ($$retries/$(MAX_RETRIES))...${NC}"; \
	done
	@echo "✅ Conversion and validation complete."

clean-profile:
	@echo "🧹 Cleaning generated files..."
	rm -f $(JSON_FILE) $(MD_FILE)
	@echo "✅ Cleanup complete."

help:
	@echo "🛠️  Available Makefile targets:"
	@echo "  make list         - List all registered prompts"
	@echo "  make validate     - Check that all registry file paths exist"
	@echo "  make export ID=xxx FILE=output.md - Export prompt content to file"
