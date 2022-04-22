import mysql.connector
import random

host = "localhost"
user = "root"
password = "Mukesh@2001"
database = "votingsystem"

digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def get_connection():
    conn = mysql.connector.connect(host=host,
                                    database=database,
                                    user=user,
                                    password=password)
    return conn

def get_voterid_list():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT VOTERID FROM VOTER")
        
        voter_list = cursor.fetchall()
        voter_list = [item[0] for item in voter_list]
        cursor.close()
        conn.close()
        return voter_list
    except Exception as e:
        print("Server erorr.")
        return list()

def get_generated_voterid():
    VID = get_voterid_list()
    vid = random.randint(10000000, 99999999)
    while vid in VID:
        vid = random.randint(10000000, 99999999)
    return vid

def validate_voter(name, phone, email, dob, assembly, pin, image):
    if len(name) < 3 and any(d in name for d in digit):
        print("Name error.")
        return False
    
    if len(phone) != 10 or not str(phone).isdigit():
        print("Phone error.")
        return False

    if not '@' in email or  not '.' in email:
        print("email error.")
        return False    

    year = int(dob[-4:])
    if 2022 - year < 18:
        print("DOB error.")
        return False

    if assembly == "Select your assembly":
        print("Assembly error.")
        return False

    if pin == "Select your pin":
        print("Pin error.")
        return False

    if image is None:
        print("image error.")
        return False

    return True


def add_voter(name, phone, email, dob, assembly, pin, image):
    if not validate_voter(name, phone, email, dob, assembly, pin, image):
        return False
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT AID FROM ASSEMBLY WHERE NAME = %s",(assembly, ))
        aid = cursor.fetchone()[0]
        voterid = get_generated_voterid()
        sql = "INSERT INTO VOTER VALUES ({},'{}','{}','{}', STR_TO_DATE('{}','%d-%m-%Y'), now(), '{}', {})".format(
            voterid, name,phone, email, dob, pin , aid
        )
        cursor.execute(sql) # added information of voter to voter table
        print("info processed.")
        # now add image of voter

        sql = """INSERT INTO PHOTO(voterid, image) VALUES (%s, %s)"""
        tup = (voterid, image)
        cursor.execute(sql, tup)
        print("image processed")
        conn.commit()
        print("Voter added.")
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error while adding voter.", e.with_traceback())
        return False

    return True

def get_voter_info(voterid):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM VOTER WHERE VOTERID = {}".format(voterid)
        cursor.execute(sql)
        ls = cursor.fetchone()
        dic = {}
        dic["voterid"], dic["name"], dic["phone"],dic["email"], dic["dob"],dic["reg"], dic["pin"], dic["assemblyid"] = ls
    except Exception as e:
        print("Server error while fetching information of voter.")
        return -1

    return dic

if __name__ == '__main__':
    get_voter_info(76736087)