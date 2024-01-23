

touch .env

python3 -m venv venv

venv/bin/activate

python3 src/manage.py migrate

python3 src/manage.py runserver

poetry shell

python3 src/main.py