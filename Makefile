.PHONY: style test docs

check_dirs := lekin examples tests

# run checks on all files and potentially modifies some of them

style:
	black $(check_dirs)
	isort $(check_dirs)
	flake8 $(check_dirs)
	pre-commit run --files $(check_dirs)

# run tests for the library

test:
	python -m unittest

# run tests for the docs

docs:
	make -C docs clean M=$(shell pwd)
	make -C docs html M=$(shell pwd)
