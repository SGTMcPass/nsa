# Makefile for nasa-simulation-assistants

.PHONY: all list validate export help

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
help:
	@echo "🛠️  Available Makefile targets:"
	@echo "  make list         - List all registered prompts"
	@echo "  make validate     - Check that all registry file paths exist"
	@echo "  make export ID=xxx FILE=output.md - Export prompt content to file"

