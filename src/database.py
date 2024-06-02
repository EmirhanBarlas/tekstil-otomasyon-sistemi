# Sqlite veritabanına yapılan işlemleri kayıt edicek olan database.py dosyası.

import sqlite3
import pandas as pd

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    # sqlite veritabanında tablo yoksa eğer tabloyu oluşturucak olan create_tables fonksiyonu.
    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            barcode TEXT NOT NULL UNIQUE
        )
        """)
        
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            contact TEXT,
            address TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS fabrics (
            id INTEGER PRIMARY KEY,
            supplier_id INTEGER,
            type TEXT NOT NULL,
            quantity REAL NOT NULL,
            arrival_date TEXT NOT NULL,
            source TEXT,
            FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
        )
        """)
        
        self.connection.commit()

    def add_product(self, name, barcode):
        self.cursor.execute("INSERT INTO products (name, barcode) VALUES (?, ?)", (name, barcode))
        self.connection.commit()

    def get_product(self, barcode):
        self.cursor.execute("SELECT * FROM products WHERE barcode = ?", (barcode,))
        return self.cursor.fetchone()

    def add_supplier(self, name, contact, address):
        self.cursor.execute("INSERT INTO suppliers (name, contact, address) VALUES (?, ?, ?)", (name, contact, address))
        self.connection.commit()

    def add_fabric(self, supplier_id, fabric_type, quantity, arrival_date, source):
        self.cursor.execute("""
        INSERT INTO fabrics (supplier_id, type, quantity, arrival_date, source)
        VALUES (?, ?, ?, ?, ?)""", (supplier_id, fabric_type, quantity, arrival_date, source))
        self.connection.commit()

    def get_fabric(self, fabric_id):
        self.cursor.execute("SELECT * FROM fabrics WHERE id = ?", (fabric_id,))
        return self.cursor.fetchone()

    def get_all_fabrics(self):
        self.cursor.execute("SELECT * FROM fabrics")
        return self.cursor.fetchall()
    

    def export_to_excel(self):
        fabrics = self.get_all_fabrics()
        df = pd.DataFrame(fabrics, columns=["ID", "Supplier ID", "Type", "Quantity", "Arrival Date", "Source"])
        df.to_excel("excels/fabrics.xlsx", index=False)

    def export_to_yaml(self):
        fabrics = self.get_all_fabrics()
        fabrics_list = [
            {
                "ID": fabric[0],
                "Supplier ID": fabric[1],
                "Type": fabric[2],
                "Quantity": fabric[3],
                "Arrival Date": fabric[4],
                "Source": fabric[5],
            }
            for fabric in fabrics
        ]

    def close(self):
        self.connection.close()
