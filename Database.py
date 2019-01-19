import MySQLdb as mysql

class Database:
    'Class for database connection to mysql'
    db = None

    @staticmethod
    def getCursor(server = 'localhost', port=3306, user ='rtovehicle', password ='rto@12345', database = 'rtovehicle'):
        if Database.db is None:
            Database.db = mysql.connect("localhost", "rtovehicle", "rto@12345", "rtovehicle")
        return Database.db.cursor()

    @staticmethod
    def commit():
        Database.db.commit()

    
