
from lib.config import CONN, CURSOR

class Apartment:
    @classmethod
    def create_apartment(cls,apartment_name , location, landlord_id):
        sql = "INSERT INTO apartments(apartment_name, location, landlord_id) VALUES(?, ?, ?)"
        CURSOR.execute(sql, (apartment_name, location, landlord_id))
        CONN.commit()

        return CURSOR.lastrowid
    @classmethod
    def get_apartments_by_id(cls, apartment_id):
        sql = "SELECT * FROM apartments WHERE id =?"
        CURSOR.execute(sql, (apartment_id,))
        return CURSOR.fetchone()
    @classmethod
    def update_apartment_by_id(cls, apartment_id, apartment_name, location, landlord_id):
        sql = "UPDATE apartments SET apartment_name =?, location =?, landlord_id = ? WHERE id =?"
        CURSOR.execute(sql, (apartment_name, location, landlord_id, apartment_id))
        CONN.commit()
        return apartment_id
    @classmethod
    def fetch_all_apartments(cls):
        sql = "SELECT * FROM apartments"
        CURSOR.execute(sql)
        return CURSOR.fetchall()
    @classmethod
    def delete_apartment_by_id(cls, apartment_id):
        sql = "DELETE FROM apartments WHERE id =?"
        CURSOR.execute(sql, (apartment_id,))
        CONN.commit()
        return apartment_id
    @classmethod
    def get_apartment_by_landlord_id(cls, landlord_id):
        sql = "SELECT * FROM apartments WHERE landlord_id =?"
        CURSOR.execute(sql, (landlord_id,))
        return CURSOR.fetchall()
    @classmethod
    def count_all_apartments(cls):
        sql = "SELECT COUNT(*) FROM apartments"
        CURSOR.execute(sql)        
        return CURSOR.fetchone()
    @classmethod
    def get_apartments_by_location(cls, location):
        sql = "SELECT * FROM apartments WHERE location =?"
        CURSOR.execute(sql, (location,))
        return CURSOR.fetchall()
    
