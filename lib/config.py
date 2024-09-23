
import sqlite3
CONN = sqlite3.connect('houses.db')
CURSOR = CONN.cursor()

class Database:
    def create_tables(self):
        sql1 = """
              CREATE TABLE IF NOT EXISTS tenants(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name varchar(40),
              email varchar(40),
              age INTEGER,
              phone_number TEXT NOT NULL,              
              rent INTEGER,
              landlord_id INTEGER,
              apartment_id INTEGER,  
              FOREIGN KEY(landlord_id) REFERENCES landlords(id),
              FOREIGN KEY(apartment_id) REFERENCES apartments(id)
              )       
       """
        CURSOR.execute(sql1)
        sql2 = """
              CREATE TABLE IF NOT EXISTS landlords(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name varchar(40),
              email varchar(40))              
        """
        CURSOR.execute(sql2)
        sql3 = """
               CREATE TABLE IF NOT EXISTS apartments(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               apartment_name TEXT,
               location varchar(40),                             
               landlord_id INTEGER,                       
               FOREIGN KEY(landlord_id) REFERENCES landlords(id))
        """
        CURSOR.execute(sql3)

        CONN.commit()
    def drop_tables(self):
        sql1 = "DROP TABLE IF EXISTS tenants"
        CURSOR.execute(sql1)
        sql2 = "DROP TABLE IF EXISTS landlords"
        CURSOR.execute(sql2)
        sql3 = "DROP TABLE IF EXISTS apartments"
        CURSOR.execute(sql3)
        CONN.commit()

db = Database()
# print("\n *****Loading...*****")
# db.drop_tables()
# print('\n*****Dropped Tables*****')
# print('\n ======3 Tables created======')
# db.create_tables()
