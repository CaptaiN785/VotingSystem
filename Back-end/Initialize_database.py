import mysql.connector
import DummyEntries

def initialize_database(host, user, password, database):
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
                PHONE int,
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

        # Closing the connection.
        if conn:
            conn.close()
            print("Connection is closed")

    except Exception as e:
        print(e.with_traceback())

