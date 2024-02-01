import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from dotenv import load_dotenv
from app import app

DEFAULT_ENV_URL = "postgresql+psycopg2://"
dirname = os.path.dirname(__file__)
found = True

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    found = False

if found:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = DEFAULT_ENV_URL

db = SQLAlchemy(app)


def insert_ingredient(ingredient_name):
    query = text("INSERT INTO pantry (ingredient_name) VALUES (:ingredient_name)")

    db.session.execute(query, {"ingredient_name": ingredient_name})
    db.session.commit()


def delete_ingredient(ingredient_name):
    query = text("DELETE FROM pantry WHERE ingredient_name = :ingredient_name")

    db.session.execute(query, {"ingredient_name": ingredient_name})
    db.session.commit()


def insert_recipe(recipe):
    query = text("INSERT INTO recipes (recipe_json) VALUES (:recipe)")
    db.session.execute(query, {"recipe": recipe})
    db.session.commit()
