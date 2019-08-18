PYTHON := ${PWD}/venv/bin/python3
PIP := ${PWD}/venv/bin/pip3

venv:
	virtualenv venv -p python3.7

install: venv
	${PIP} install -r requirements.txt

clean: 
	sudo rm -rf venv