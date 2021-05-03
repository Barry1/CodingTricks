.PHONY: check pretty

check:
	pylama *.py
	pylint *.py
	pyflakes *.py

pretty:
	isort *.py
	black *.py

autogit: check pretty
	git commit -m "Autocommit from Makefile after check and pretty"

autopush: autogit
	git push

