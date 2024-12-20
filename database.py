import sqlite3
class Database:
    def __init__(self, path: str):
        self.path = path
    def crate_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS reviews(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NUT NULL,
                    food_rating INTEGER,
                    cleanliness_rating INTEGER, 
                    extra_comments TEXT NUT NULL
                )
            """)
            conn.commit()
    def dialog (self, data:dict):
        with sqlite3.connect('self.path') as conn:
            conn.execute(
                '''
                INSERT INTO reviews (name, food_rating, cleanliness_rating,  extra_comments)
                VALUES (?, ?, ?, ?)
                ''',
                (data["name"], data["food_rating"],
                 data["cleanliness_rating"], data["extra_comments"])
            )