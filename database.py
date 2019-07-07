import mysql.connector as mysql

class database:
    def dbConnect(self):
        return mysql.connect(
            host="localhost",
            user="root",
            passwd="",
            database="dbbluetranquility"
        )

    def get_therapists(self):
        try:
            db = self.dbConnect()
            sql = "SELECT CONCAT(first_name, ' ', last_name , '(', nickname, ')' as name FROM therapists;"
            cursor = db.cursor(dictionary=True)
            cursor.execute(sql)
            therapists = cursor.fetchall()
            return therapists
        except mysql.Error as err:
            print("Something went wrong...\n%s" % str(err))
            return []
        except:
            print("Something went wrong. Contact the admin.")
            return []

    def fake_therapists(self):
        return ["Marcuz Corpuz", "Daryl Mora", "Paolo Merina"]

    def isAdmin(self, fingerId):
        return fingerId == 1

    def saveTime(self, fingerId):
        if fingerId == 1:
            return "Daryl Mora", "in"
        else:
            return "Anonymous", "in"


if __name__ == '__main__':
    therapists = get_therapists() 
    print("get_therapists(): [\"%s\",...]" % str(therapists[0]))
