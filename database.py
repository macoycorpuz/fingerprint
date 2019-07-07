import mysql.connector as mysql


def dbConnect():
    return mysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database="dbbluetranquility"
    )

def get_therapists():
    try:
        db = dbConnect()
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

def fake_therapists():
    return ["Marcuz Corpuz", "Daryl Mora", "Paolo Merina"]


if __name__ == '__main__':
    therapists = get_therapists() 
    print("get_therapists(): [\"%s\",...]" % str(therapists[0]))
