import mysql.connector
from Module import *

try:
    conn = mysql.connector.connect( host="localhost",
                                    database="votingsystem",
                                    user="root",
                                    password="Mukesh@2001")
    if conn:
        print("connection established")
        # cursor.execute("create database VotingSystesm")
        # image = 
        # print(str(image)[2:-1])
        # value = (399388, image, '840003', 300001)
        # print(cursor)
        # cursor.execute('insert into voter(voterid, photo, pin, aid) values(30002, %s, "840003", 300001)',(image, ))
        # conn.commit()
        # ls = cursor.fetchall()
        # cursor.execute("select photo from voter")
        # ls = cursor.fetchall()
        # for l in ls:
        #     with open("images/temp.png", "wb") as f:
        #         # print(l[0].encode)
        #         f.write(l[0])
        #         print("Done")
        Cursor = conn.cursor()
        PIN = []
        Cursor.execute("select pin from postaladdress")
        ls = Cursor.fetchall()
        for l in ls:
            PIN.append(l[0])
        
        AID = {}
        Cursor.execute("select aid,name from assembly")
        ls = Cursor.fetchall()
        for l in ls:
            aid_, name_ = l
            AID[name_] = aid_

        ANAME = []
        for key, val in AID.items():
            ANAME.append(key)
        # print(self.ANAME)
        
        VID = []
        Cursor.execute('select voterid from voter')
        ls = Cursor.fetchall()
        for l in ls:
            VID.append(l[0])
        
        Cursor.close()
    else:
        print("Unable to establish connection")
        sys.exit(1)
except mysql.connector.Error as e:
    print("Got mysql error {}".format(e))
    sys.exit(1)
# print(PIN)
# print(AID)
# print(ANAME)
# print(VID)