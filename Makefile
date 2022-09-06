init:
	virtualenv .venv
	git init 
	touch run.py
	mkdir app 
	touch ./app/__init__.py ./app/settings.py ./app/routes.py 
	mkdir ./app/resources 
	touch ./app/resources/__init__.py ./app/resources/resource.py

install:
	pip install --upgrade pip
	pip install -r requirements.txt

test: 
	#make test

format:
	#format code 

bulid:
	#build app 
deploy:
	#deploy app
