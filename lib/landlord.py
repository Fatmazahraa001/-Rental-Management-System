
from lib.config import CONN, CURSOR


class Landlord:    

    @classmethod
    def create_landlord(cls, name, email):
        sql = "INSERT INTO landlords(name, email) VALUES(?, ?)"
        CURSOR.execute(sql, (name, email))
        CONN.commit()

        return CURSOR.lastrowid

    @classmethod
    def get_landlord_by_id(cls, landlord_id):
        sql = "SELECT * FROM landlords WHERE id =?"
        CURSOR.execute(sql, (landlord_id,))
        return CURSOR.fetchone()
    @classmethod
    def update_landlord_by_id(cls, landlord_id, name, email):
        sql = "UPDATE landlords SET name =?, email =? WHERE id =?"
        CURSOR.execute(sql, (name, email, landlord_id))
        CONN.commit()
        return landlord_id
    @classmethod
    def delete_landlord_by_id(cls, landlord_id):
        sql = "DELETE FROM landlords WHERE id =?"
        CURSOR.execute(sql, (landlord_id,))
        CONN.commit()
        return landlord_id
    @classmethod
    def count_all_landlords(cls):
        sql = "SELECT COUNT(*) FROM landlords"
        CURSOR.execute(sql)        
        return CURSOR.fetchone()
    @classmethod
    def fetch_all_landlords(cls):
        sql = "SELECT * FROM landlords"
        CURSOR.execute(sql)
        return CURSOR.fetchall()
