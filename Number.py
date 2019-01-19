from Database import Database as db

class Number:
    'Class to maintain user info'
    user_id = ""
    vname = ""
    vtype = ""
    vmodel = ""
    vprice = ""
    vowner = ""
    def __init__(self, user_id, vname,  vtype, vmodel, vprice, vowner):
        self.user_id = user_id
        self.vname = vname
        self.vtype = vtype
        self.vmodel = vmodel
        self.vprice = vprice
        self.vowner = vowner
        

    def save(self):
        query = "INSERT INTO temp_details (user_id, vname, vtype, vmodel, vprice, vowner) VALUES(%s, %s, %s, %s, %s, %s)"
        cur = db.getCursor()
        if cur.execute(query, (self.user_id, self.vname, self.vtype, self.vmodel, self.vprice, self.vowner)):
           db.commit()
           return 1
        else:
            return 0


