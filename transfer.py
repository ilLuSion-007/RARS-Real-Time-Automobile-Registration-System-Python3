from Database import Database as db

class transfer:
    'Class to maintain user info'
    user_id = ""
    vyear = ""
    vnumber = ""
    vnowner = ""
    vprice = ""
    vpowner = ""
    vtype = ""
    def __init__(self, user_id, vyear, vnumber, vnowner, vprice, vpowner, vtype):
        self.user_id = user_id
        self.vyear = vyear
        self.vnumber = vnumber
        self.vnowner = vnowner
        self.vprice = vprice
        self.vpowner = vpowner
        self.vtype = vtype

    def save(self):
        #The Transfer details of new owner
        query = "INSERT INTO transfer_details (user_id, vyear, vnumber, vnowner, vprice, vpowner, vtype) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        cur = db.getCursor()
        if cur.execute(query, (self.user_id, self.vyear, self.vnumber, self.vnowner, self.vprice, self.vpowner, self.vtype)):
           db.commit()
           return 1
        else:
            return 0
       
    #def active(user_id):
        #query = "UPDATE vehicle_details SET sale_state = sold, sale_date =now() WHERE user_id =%s"
        #cur = db.getCursor()
        #if cur.execute(query,(user_id)):
            #db.commit()
            #return 1
        #else:
            #return 0
       

