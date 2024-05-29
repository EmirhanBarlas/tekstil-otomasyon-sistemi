import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            barcode TEXT NOT NULL UNIQUE
        )
        """)
        self.connection.commit()

    def add_product(self, name, barcode):
        self.cursor.execute("INSERT INTO products (name, barcode) VALUES (?, ?)", (name, barcode))
        self.connection.commit()

    def get_product(self, barcode):
        self.cursor.execute("SELECT * FROM products WHERE barcode = ?", (barcode,))
        return self.cursor.fetchone()

    def close(self):
        self.connection.close()
