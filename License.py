from Database import Database as db

class License:
    'Class to maintain user info'
    user_id = ""
    license_no = ""
    driver_name = ""
    issue_year = ""
    expire_year = ""
    issue_authority = ""
    vehicle_type = ""
    def __init__(self, user_id, license_no, driver_name, issue_year, expire_year, issue_authority, vehicle_type):
        self.user_id = user_id
        self.license_no = license_no
        self.driver_name = driver_name
        self.issue_year = issue_year
        self.expire_year = expire_year
        self.issue_authority = issue_authority
        self.vehicle_type = vehicle_type

    def save(self):
        query = "INSERT INTO license_details (user_id, license_no, driver_name, issue_year, expire_year, issue_authority, vehicle_type) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        cur = db.getCursor()
        if cur.execute(query, (self.user_id, self.license_no, self.driver_name, self.issue_year, self.expire_year, self.issue_authority, self.vehicle_type)):
           db.commit()
           return 1
        else:
            return 0


