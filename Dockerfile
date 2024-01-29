FROM python:3.10
ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

WORKDIR /kitsain/

RUN chgrp root /kitsain/ && chmod 660 /kitsain/

COPY poetry.lock pyproject.toml /kitsain/

RUN pip3 install poetry

RUN poetry install

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "python", "src/app.py", "runserver", "0.0.0.0:8000"]