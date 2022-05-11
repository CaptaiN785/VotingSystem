import mysql.connector
import random
import DummyEntries

host = "localhost"
user = "root"
password = "Mukesh@2001"
database = "votingsystem"

digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

POSTS = ["MLA", "Chief Minister", "Prime minister"]


def initialize_database():
    try:
        # connecting with server without having any database
        conn = mysql.connector.connect( host=host,
                                        user=user,
                                        password=password)

        if not conn.is_connected():
            print("Got an error.")
            raise Exception
        
        # creating a cursor to create a database if not exists
        mycursor = conn.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS VOTINGSYSTEM")
        # After creating database close connection with server
        # Reconnect with database specified 
        if mycursor :
            mycursor.close()
        if conn:
            conn.close()
        
        # Connecting with server with specified database
        conn = mysql.connector.connect(
            host=host,
            user = user,
            password=password,
            database = database
        )
        print("Database is connnected")

        # Created cursor to execute initial query
        mycursor = conn.cursor()

        # Creating a table name "assembly" which will contain assemly name and information if not exists
        createAssemblyTable = """CREATE TABLE IF NOT EXISTS ASSEMBLY(
            AID int primary key auto_increment, 
            NAME varchar(20),
            BLOCK varchar(20)
            )
        """
        mycursor.execute(createAssemblyTable)
        # mycursor.execute("alter assembly set auto_increment = 300000")

        # checking whether assembly table has some entries or not 
        # if not then I will insert some dummy entries.
        mycursor.execute("SELECT * FROM ASSEMBLY")
        ls = mycursor.fetchall()
        if len(ls) == 0:
            DummyEntries.insertassembly(mycursor)
        print("Assmebly table is created")

        # Creating a postaladdress to store the address ot voter not make extra usage of memory
        createPostalAddress = """
            CREATE TABLE IF NOT EXISTS POSTALADDRESS(
                PIN varchar(6) primary key,
                POST varchar(30),
                DISTRICT varchar(20),
                STATE varchar(20),
                COUNTRY varchar(20)
            )
        """
        mycursor.execute(createPostalAddress)

        # Checking for whether it has any entries or not.
        # if not then insert some dummy entries.
        mycursor.execute("SELECT * FROM POSTALADDRESS")
        LS = mycursor.fetchall()
        if len(LS) == 0:
            DummyEntries.insertpostaladdress(mycursor)
        print("Postaladdress is created")

        # Creating a voter table which will store all information about voters
        createVoter = """
            CREATE TABLE IF NOT EXISTS VOTER(
                VOTERID int primary key,
                NAME varchar(30),
                PHONE varchar(10),
                EMAIL varchar(30),
                DOB date,
                REGDATE date, 
                PIN varchar(6),
                AID int
            )
        """
        mycursor.execute(createVoter)
        print("Voter is created")

        # creating a photo table, it will store images of voters seperatley just to remove heavy load on single table.
        createPhoto = """
            CREATE TABLE IF NOT EXISTS PHOTO(
                VOTERID INT PRIMARY KEY,
                IMAGE LONGBLOB
            )
        """
        mycursor.execute(createPhoto)
        print("Photo is created")

        # Creating election table for inserting election date post and all.
        createElection = """
            CREATE TABLE IF NOT EXISTS ELECTION(
                EID INT PRIMARY KEY AUTO_INCREMENT,
                NAME VARCHAR(30),
                POST VARCHAR(20),
                DATE DATE,
                AID INT
            )
        """
        mycursor.execute(createElection)
        print("Election table is created.")

        createCandidate = """
            CREATE TABLE IF NOT EXISTS CANDIDATE(
                CID INT PRIMARY KEY AUTO_INCREMENT,
                VID INT UNIQUE,
                EID INT,
                SYMBOL VARCHAR(100)
            )
        """
        mycursor.execute(createCandidate)
        print("Candidate table is created.")

        # Closing the connection.
        if conn:
            conn.close()
            print("Connection is closed")

    except Exception as e:
        print(e.with_traceback())
initialize_database()

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
        return False,{}
    
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
        return False, {}

    return True, get_voter_info(voterid)

def get_voter_info(voterid):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM VOTER WHERE VOTERID = {}".format(voterid)
        cursor.execute(sql)
        ls = cursor.fetchone()
        cursor.close()
        conn.close()
        dic = {}
        dic["voterid"], dic["name"], dic["phone"],dic["email"], dic["dob"],dic["reg"], dic["pin"], dic["assemblyid"] = ls
    except Exception as e:
        print("Server error while fetching information of voter.")
        return -1

    return dic

def get_assembly_list():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "SELECT AID, NAME FROM ASSEMBLY"
        cursor.execute(sql)

        ls = cursor.fetchall()
        cursor.close()
        conn.close()
        dic = {}
        lst = []
        for aid, name in ls:
            dic[name] = aid
            lst.append(name)

        return (lst, dic)

    except Exception as e:
        print("Error while fetching assembly list.")

def get_voter_photo(voterid):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "SELECT IMAGE FROM PHOTO WHERE VOTERID = {}".format(voterid)
        cursor.execute(sql)
        image = cursor.fetchone()[0]
        # print(image)
        with open('voter.png', 'wb') as file:
            file.write(image)
        
        return "voter.png"

    except Exception as e:
        print("Error while fetching image of voter.")

def add_election_detail(name, date, post, aid):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """INSERT INTO ELECTION(NAME, DATE, POST, AID) 
                VALUES ('{}', STR_TO_DATE('{}', '%d-%m-%Y'), '{}',{})""".format(name, date, post, aid)
        cursor.execute(sql)
        print("election info is added.")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS {}(
                VID int primary key,
                CID int
            )
        """.format(name))
        print("Election table is created.")

        conn.commit()
        cursor.close()
        conn.close()
        print("Election added successfully.")
        return True
    except Exception as e:
        print("Error while adding election details.")
        return False

def get_upcoming_election_list():
    """It will return name of elections and dic mapping with name and EID(election id)"""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = "SELECT EID, NAME FROM ELECTION WHERE DATE >= CURDATE()"
        cursor.execute(sql)
        lst = cursor.fetchall()
        cursor.close()
        conn.close()
        names = []
        dic = {}
        for eid, name in lst:
            names.append(name)
            dic[name] = eid

        return names, dic

    except Exception as e:
        print("Error while fetching election list")

def get_past_election_list():
    """It will return name of elections and dic mapping with name and EID(election id)"""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = "SELECT EID, NAME FROM ELECTION WHERE DATE <= CURDATE()"
        cursor.execute(sql)
        lst = cursor.fetchall()
        cursor.close()
        conn.close()
        names = []
        dic = {}
        for eid, name in lst:
            names.append(name)
            dic[name] = eid

        return names, dic

    except Exception as e:
        print("Error while fetching election list")

def get_next_symbol(eid):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "SELECT COUNT(*) FROM CANDIDATE WHERE EID = {}".format(eid)
        cursor.execute(sql)

        ls = cursor.fetchone()[0]
        
        symbol_path = "../symbol/{}.png".format(int(ls)+1)

        return symbol_path
    except Exception as e:
        print("Error while fetchign net symbol.")

def add_candidate(cid, eid, symbol):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = """INSERT INTO CANDIDATE(VID, EID, SYMBOL) VALUES(
            {}, {}, '{}'
        )""".format(cid, eid, symbol)

        cursor.execute(sql)
        conn.commit()
        print("candidate added succesfully.")
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print("Error while adding candidate.")
        return False

def get_pin_list():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT PIN FROM POSTALADDRESS")
        
        lst = cursor.fetchall()
        pins = []
        for pin in lst:
            pins.append(pin[0])
        return pins

    except Exception as e:
        print("Error while fetching pin list.")



if __name__ == '__main__':
    # get_voter_info(76736087)
    # get_voter_photo(76736087)
    # get_assembly_list()
    # name, eid = get_past_election_list()
    # print(name, eid)
    # print(get_next_symbol(2))
    print(get_upcoming_election_list())