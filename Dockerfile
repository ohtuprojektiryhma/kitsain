FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /kitsain/src

COPY poetry.lock pyproject.toml /kitsain/src

RUN pip3 install poetry

RUN poetry config virtualenvs.create false

RUN poetry install

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "python", "src/manage.py", "runserver", "0.0.0.0:8000"]