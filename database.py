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
                CREATE TABLE IF NOT EXISTS  dishes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT  NUT NULL,
                    price FLOAT,
                    cover TEXT NUT NULL,
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


    def save_dishes(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                    INSERT INTO dishes (name, price, cover, description, categories)
                    VALUES (?, ?, ?, ?, ?)
                """,
                (data["name"], data["price"], data ["cover"], data["description"], data["categories"] )
            )

    def get_all_dishes(self):
        with sqlite3.connect(self.path) as conn:
            result = conn.execute("SELECT * from dishes")
            result.row_factory = sqlite3.Row
            data = result.fetchall()
            return [dict(row) for row in data]

