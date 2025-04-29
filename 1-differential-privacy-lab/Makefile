.PHONY: install launch test lint help

install:
	pip install -r requirements.txt

launch:
	jupyter lab

test:
	pytest lib/

lint:
	black . && markdownlint "**/*.md" && yamllint .

help:
	@echo "Available commands:"
	@echo "  make launch   # Launch Jupyter Lab server"
	@echo "  make lint     # Format Python + lint Markdown and YAML files"
	@echo "  make test     # Runs any tests that exist"
  @echo "  make help     # Show this help message"