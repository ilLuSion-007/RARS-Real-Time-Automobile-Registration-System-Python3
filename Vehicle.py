from Database import Database as db

class Vehicle:
    'Class to maintain user info'
    user_id = ""
    vehicle_no = ""
    vehicle_type = ""
    vehicle_name = ""
    vehicle_model = ""
    vehicle_color = ""
    vehicle_owner = ""
    vehicle_year = ""
    sale_state = ""
    sale_date = ""
    def __init__(self, user_id, vehicle_no, vehicle_type, vehicle_name, vehicle_model, vehicle_color, vehicle_owner, vehicle_year):
        self.user_id = user_id
        self.vehicle_no = vehicle_no
        self.vehicle_type = vehicle_type
        self.vehicle_name = vehicle_name
        self.vehicle_model = vehicle_model
        self.vehicle_color = vehicle_color
        self.vehicle_owner = vehicle_owner
        self.vehicle_year = vehicle_year

    def save(self):
        query = "INSERT INTO vehicle_details (user_id, vehicle_no, vehicle_type, vehicle_name, vehicle_model, vehicle_color, vehicle_owner, vehicle_year, sale_state, sale_date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, 'not sold', now())"
        cur = db.getCursor()
        if cur.execute(query, (self.user_id, self.vehicle_no, self.vehicle_type, self.vehicle_name, self.vehicle_model, self.vehicle_color, self.vehicle_owner, self.vehicle_year)):
           db.commit()
           return 1
        else:
            return 0
    @staticmethod
    def authenticate(user_id):
        query = "SELECT * FROM vehicle_details WHERE user_id = %s"
        cur = db.getCursor()
        cur.execute(query, (user_id))
        return cur.fetchone() != None

