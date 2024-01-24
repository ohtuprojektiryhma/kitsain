FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY poetry.lock pyproject.toml /usr/src/app/

RUN pip3 install poetry

RUN poetry install

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "python", "src/manage.py", "runserver", "0.0.0.0:8000"]