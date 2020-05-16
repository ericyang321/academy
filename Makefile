pyinstall:
	pip install -r python/requirements.txt

pytest:
	python -m pytest

pyrun:
	python python/index.py

pyconsole:
	python -i python/index.py

cbuild:
	clang -Wall ./c/index.c -o ./bin/indexc -lm

crun:
	make cbuild && ./bin/indexc

cppbuild:
	g++ ./cpp/index.cpp -o ./bin/indexcpp -lm -std=c++17

cpprun:
	make cppbuild && ./bin/indexcpp
