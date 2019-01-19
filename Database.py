import MySQLdb as mysql

class Database:
    'Class for database connection to mysql'
    db = None

    @staticmethod
    def getCursor(server = '185.22.154.187', port=3306, user ='rtovehicle', password ='rto@12345', database = 'rtovehicle'):
        if Database.db is None:
            Database.db = mysql.connect("185.22.154.187", "rtovehicle", "rto@12345", "rtovehicle")
        return Database.db.cursor()

    @staticmethod
    def commit():
        Database.db.commit()

    