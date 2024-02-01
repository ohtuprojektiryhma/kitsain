from os import getenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from app import app

DEFAULT_ENV_URL = "postgresql+psycopg2://"

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
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
