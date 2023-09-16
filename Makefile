package=pip
run:
	. venv/bin/activate; \
	python main.py;
setup:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip install -r requirements.txt;
install:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip install $(package);
extract:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip freeze > requirements.txt;
