# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import text
# from app import app

# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://"
# db = SQLAlchemy(app)


# def insert_ingredient(ingredient_name):
#     query = text(
#         "INSERT INTO pantry (ingredient_name) VALUES (:ingredient_name)")
#     db.session.execute(query, {"ingredient_name": ingredient_name})
#     db.session.commit()


# def delete_ingredient(ingredient_name):
#     query = text("DELETE FROM pantry WHERE ingredient_name = :ingredient_name")
#     db.session.execute(query, {"ingredient_name": ingredient_name})
#     db.session.commit()


# def insert_recipe(name):
#     query = text(
#         "INSERT INTO recipes (name) VALUES (:name)")
#     db.session.execute(query, {"name": name})
#     db.session.commit()
