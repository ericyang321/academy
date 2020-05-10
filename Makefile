pyinstall:
	pip install -r python/requirements.txt

pytest:
	python -m pytest

pyrun:
	python python/index.py

pyconsole:
	python -i python/index.py

cbuild:
	clang -Wall -o ./bin/index ./c/index.c -lm

crun:
	make cbuild && ./bin/index
