install:
	pip install -e .[dev]

test:
	pytest

lint:
	ruff check .

format:
	ruff format .

build:
	poetry build --format sdist

build-wheel:
	poetry build --format wheel

build-sdist:
	poetry build --format sdist

py-build:
	python setup.py sdist bdist_wheel