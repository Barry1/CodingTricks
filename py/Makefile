.PHONY: check pretty

LINELENGTH = 85

#pyflakes is not used, flake 8 wraps it and understands noqa.
#prospector *.py seems to be defect at the moment

check:
	pylint *.py
#	pep8 *.py
	pylama *.py
	flake8 --ignore=E501 *.py
	mypy --python-version 3.7 --show-error-codes *.py

pretty:
	isort --overwrite-in-place --line-length $(LINELENGTH) --py 37 *.py
	black --color --target-version py37 --line-length $(LINELENGTH) *.py

autogit: check pretty
	git commit -m "Autocommit from Makefile after check and pretty"

autopush: autogit
	git push

