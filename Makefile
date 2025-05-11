# Makefile for nasa-simulation-assistants

.PHONY: all list validate export convert-profile validate-profile help

YAML_FILE=profiles/prompt/nasa_simulation_prompt_assistant.yaml
CONVERT_SCRIPT=tools/convert_prompt_profile.py
JSON_FILE=profiles/prompt/nasa_simulation_prompt_assistant.json
MD_FILE=profiles/prompt/nasa_simulation_prompt_assistant.md
MAX_RETRIES=3


all: list

list:
	@echo "📋 Listing all prompts..."
	@python3 tools/load_prompt.py --list

validate:
	@echo "🔍 Validating prompt registry..."
	@python3 tools/load_prompt.py --validate

export:
	@echo "📤 Exporting prompt by ID (set ID= and FILE=)..."
	@test -n "$(ID)" && test -n "$(FILE)" || (echo "❌ You must set ID and FILE"; exit 1)
	@python3 tools/load_prompt.py --id $(ID) --export $(FILE)

convert:
	@echo "🔄 Converting JSON assistant profile to YAML and Markdown..."
	@python3 tools/convert_prompt_profile.py profiles/prompt/nasa_simulation_prompt_assistant.json

lint:
	echo "🔎 Linting JSON MD and YAML prompt files..."
	@python3 tools/lint_prompts.py

validate-prompts:
	@echo "🔎 Validating prompt structure and metadata..."
	@python3 tools/validate_prompt_files.py

convert-profile:
	@echo "🚀 Converting YAML to JSON and Markdown..."
	python3 $(CONVERT_SCRIPT) $(YAML_FILE)
	@echo "🔎 Running pre-commit validation on generated files..."
	# Retry loop for pre-commit
	@retries=0; \
	while ! pre-commit run --all-files; do \
		retries=$$((retries + 1)); \
		if [ $$retries -ge $(MAX_RETRIES) ]; then \
			echo "❌ Pre-commit failed after $(MAX_RETRIES) attempts."; \
			exit 1; \
		fi; \
		echo "🔄 Pre-commit failed. Retrying ($$retries/$(MAX_RETRIES))..."; \
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
