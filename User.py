from Database import Database as db

class User:
    'Class to maintain user info'
    first_name = ""
    last_name = ""
    user_id = ""
    password = ""
    address = ""
    city = ""
    state = ""
    pincode = ""
    phone = ""
    def __init__(self, first_name, last_name,user_id, password, address, city, state, pincode, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.password = password
        self.address = address
        self.city = city
        self.state = state
        self.pincode = pincode
        self.phone = phone
    def save(self):
        query = "INSERT INTO account_holder_details (first_name, last_name,user_id, password, address, city, state, pincode, phone) VALUES(%s, %s,%s, %s, %s, %s, %s, %s, %s)"
        cur = db.getCursor()
        if cur.execute(query, (self.first_name, self.last_name,self.user_id, self.password, self.address, self.city, self.state, self.pincode, self.phone)):
           db.commit()
           return 1
        else:
            return 0
    @staticmethod
    def authenticate(user_id, password):
        query = "SELECT * FROM account_holder_details WHERE user_id = %s AND password = %s"
        cur = db.getCursor()
        cur.execute(query, (user_id, password))
        return cur.fetchone() != None
    @staticmethod
    def authenuser_id(user_id):
        query = "SELECT * FROM account_holder_details WHERE user_id = %s"
        cur = db.getCursor()
        cur.execute(query, [user_id])
        return cur.fetchone() != None

