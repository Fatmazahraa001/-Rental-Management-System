from lib.config import CONN, CURSOR


class Tenant:
    @classmethod
    def create_tenant(cls, name, email, age, phone_number, rent, landlord_id, apartment_id):
        sql = "INSERT INTO tenants(name, email, age, phone_number, rent, landlord_id, apartment_id) VALUES(?, ?, ?, ?, ?, ?, ?)"
        CURSOR.execute(sql, (name, email, age, phone_number, rent, landlord_id, apartment_id))
        CONN.commit()

        return CURSOR.lastrowid
    @classmethod
    def get_tenants_by_id(cls, tenant_id):
        sql = "SELECT * FROM tenants WHERE id =?"
        CURSOR.execute(sql, (tenant_id,))
        return CURSOR.fetchone()
    @classmethod
    def delete_tenant(cls, tenant_id):
        sql = "DELETE FROM tenants WHERE id =?"
        CURSOR.execute(sql, (tenant_id,))
        CONN.commit()
        return tenant_id
    @classmethod
    def get_total_rents(cls, landlord_id):
        sql = "SELECT SUM(rent) FROM tenants WHERE landlord_id =?"
        CURSOR.execute(sql, (landlord_id,))        
        return CURSOR.fetchone()
    @classmethod
    def get_tenants_by_landlord_id(cls, landlord_id):
        sql = "SELECT * FROM tenants WHERE landlord_id =?"
        CURSOR.execute(sql, (landlord_id,))
        return CURSOR.fetchall()
    @classmethod
    def get_average_rent(cls, landlord_id):
        sql = "SELECT AVG(rent) FROM tenants WHERE landlord_id =?"
        CURSOR.execute(sql, (landlord_id,))        
        return CURSOR.fetchone()
    @classmethod
    def count_all_tenants(cls):
        sql = "SELECT COUNT(*) FROM tenants"
        CURSOR.execute(sql)        
        return CURSOR.fetchone()
    @classmethod
    def update_tenant(cls, tenant_id, name, email, age, phone_number, rent, landlord_id, apartment_id):
        sql = "UPDATE tenants SET name =?, email =?, age =?, phone_number =?, rent =?, landlord_id = ?, apartment_id= ? WHERE id = ?"
        CURSOR.execute(sql, (name, email, age, phone_number, rent, landlord_id, apartment_id ,tenant_id))
        CONN.commit()
        return tenant_id
    @classmethod
    def fetch_all_tenants(cls):
        sql = "SELECT * FROM tenants"
        CURSOR.execute(sql)
        return CURSOR.fetchall()