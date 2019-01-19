from Database import Database as db
from datetime import datetime

class Task():

    @staticmethod
    def active(user_id):
        query = "UPDATE vehicle_details SET sale_state ='sold', sale_date =now() WHERE user_id =%s"
        cur = db.getCursor()
        if cur.execute(query,[user_id]):
            db.commit()
    @staticmethod
    def getStataccount(user_id):
        query = "SELECT * FROM account_holder_details WHERE user_id = %s"
        cur = db.getCursor()
        cur.execute(query,[user_id])
        return cur.fetchall()
    @staticmethod
    def getStatvehicle(user_id):
        query = "SELECT * FROM vehicle_details WHERE user_id = %s"
        cur = db.getCursor()
        cur.execute(query,[user_id])
        return cur.fetchall()
    @staticmethod
    def getStattransfer(user_id):
        query = "SELECT * FROM transfer_details WHERE user_id = %s"
        cur = db.getCursor()
        cur.execute(query,[user_id])
        return cur.fetchall()
    @staticmethod
    def getStatlicense(user_id):
        query = "SELECT * FROM license_details WHERE user_id = %s"
        cur = db.getCursor()
        cur.execute(query,[user_id])
        return cur.fetchall()
    def getuserid(self):
        query = "SELECT user_id from account_holder_details"
        cur = db.getCursor()
        cur.execute(query)
        result =  cur.fetchall()
        for i in result:
                 print (i)

        

