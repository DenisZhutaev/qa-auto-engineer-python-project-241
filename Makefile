.PHONY: install lint test check test-coverage

install:
	uv pip install -e .
	uv pip install pytest ruff pytest-cov

lint:
	uv run ruff check .

test:
	uv run pytest tests/

test-coverage:
	uv run pytest tests/ --cov=gendiff --cov-report=xml --cov-report=term

check:
	uv run ruff check .
	uv run pytest tests/
