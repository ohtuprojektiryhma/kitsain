FROM python:3.10
ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

WORKDIR /kitsain

COPY . .

RUN chgrp root /kitsain && chmod 660 /kitsain

RUN pip3 install poetry

###RUN poetry install --no-root

EXPOSE 8000

###CMD ["poetry", "run", "flask", "--app", "src/app.py", "runserver", "0.0.0.0:8000"]
CMD ["poetry", "--version"]