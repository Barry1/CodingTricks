.PHONY: check pretty

LINELENGTH = 85

#pyflakes is not used, flake 8 wraps it and understands noqa.
#prospector *.py seems to be defect at the moment

check:
	pylama
	-pytest

pretty:
	isort --profile=black --overwrite-in-place --line-length $(LINELENGTH) --py 310 *.py
	black --color --target-version py310 --line-length $(LINELENGTH) *.py

autogit: check pretty
	git commit -m "Autocommit from Makefile after check and pretty"

autopush: autogit
	git push

