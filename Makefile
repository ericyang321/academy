pyinstall:
	pip install -r python/requirements.txt

pytest:
	python -m pytest

pyrun:
	python python/index.py

pyconsole:
	python -i python/index.py
