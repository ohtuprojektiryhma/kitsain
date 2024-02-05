from sqlalchemy.sql import text


class PantryRepository:
    def __init__(self, db):
        self.db = db

    def insert_ingredient(self, ingredient_name, amount, serial_number):
        query1 = text(
            """INSERT INTO pantry (ingredient_name, amount, serial_number) 
            VALUES (:ingredient_name, :amount, :serial_number)"""
        )
        self.db.session.execute(
            query1,
            {
                "ingredient_name": ingredient_name,
                "amount": amount,
                "serial_number": serial_number,
            },
        )
        self.db.session.commit()

    def delete_ingredient(self, ingredient_name):
        query = text("DELETE FROM pantry WHERE ingredient_name = :ingredient_name")

        self.db.session.execute(query, {"ingredient_name": ingredient_name})
        self.db.session.commit()

    def insert_recipe(self, recipe):
        query = text("INSERT INTO recipes (recipe_json) VALUES (:recipe)")
        self.db.session.execute(query, {"recipe": recipe})
        self.db.session.commit()

    def get_all_pantry_ingredients(self):
        query = text("SELECT ingredient_name, amount, serial_number FROM pantry")
        ingredients = self.db.session.execute(query).fetchall()

        return ingredients

    def test_database_connection(self):
        connection = False
        try:
            query = text("SELECT 1")
            self.db.session.execute(query)
            connection = True
            print("connection to database found")
            print("using database for saving")
        except:  # pylint: disable=W0702
            print("connection to database not found")
            print("using text files for saving")
        return connection
