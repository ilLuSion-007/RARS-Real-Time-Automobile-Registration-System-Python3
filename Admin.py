from Database import Database as db

class Admin:
    'Class to maintain admin info'

    def __init__(self):
        pass
    
    @staticmethod
    def authenticate(username, password):
        query = "SELECT * FROM admin_details WHERE admin_id = %s AND admin_password = %s"
        cur = db.getCursor()
        cur.execute(query, (username, password))
        return cur.fetchone() != None


