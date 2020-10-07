.ONESHELL:

.PHONY: clean install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:
	pip3 install -r requirements.txt;

tests:
	python3 manage.py test

run:
	python3 manage.py run

all: clean install tests run
