
.PHONY: style test

# run checks on all files and potentially modifies some of them

style:
    black --preview

# run tests for the library

test:
    python -m unittest

# release
