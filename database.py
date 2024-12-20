import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path

    def crate_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS review (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    phone_or_instagram  TEXT NUT NULL,
                    food_rating  INTEGER,
                    cleanliness_rating  INTEGER,
                    extra_comments TEXT NUT NULL
                    
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS restaurant_new_food (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT  NUT NULL,
                    price FLOAT,
                    description TEXT  NUT NULL,
                    categories TEXT  NUT NULL
                )

            """)
            conn.commit()

    def save_survey(self, data: dict):
         with sqlite3.connect(self.path) as conn:
            conn.execute(
            """
                INSERT INTO review (name, phone_or_instagram,  food_rating,
                cleanliness_rating,  extra_comments )
                VALUES (?, ?, ?, ?, ?)
            """,
            (data["name"], data["phone_or_instagram"], data["food_rating"],
             data["cleanliness_rating"], data["extra_comments"])
            )


    def save_restaurant_food(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                    INSERT INTO restaurant_new_food (name, price, description, categories)
                    VALUES (?, ?, ?, ?)
                """,
                (data["name"], data["price"], data["description"], data["categories"] )
            )


