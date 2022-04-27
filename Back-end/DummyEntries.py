def insertpostaladdress(cursor):
    """here inserting some of dummy entries for simple execution of program"""
    dummy = [
        "INSERT INTO POSTALADDRESS VALUES('840003', 'JALE', 'DARBHANGA','BIHAR', 'INDIA')",
        "INSERT INTO POSTALADDRESS VALUES('842303', 'BANDHAULI', 'DARBHANGA','BIHAR', 'INDIA')",
        "INSERT INTO POSTALADDRESS VALUES('847301', 'KOTA', 'KOTA','RAJSTHAN', 'INDIA')",
        "INSERT INTO POSTALADDRESS VALUES('847303', 'MOHALI', 'MOHALI','PUNJAB', 'INDIA')",
        "INSERT INTO POSTALADDRESS VALUES('848703', 'BHATINDA', 'LUCKNOW','UTTAR PRADESH', 'INDIA')",
        "INSERT INTO POSTALADDRESS VALUES('849876', 'KUCHH', 'JAIPUR','RAJSTHAN', 'INDIA')"
    ]

    try:
        for value in dummy:
            cursor.execute(value)
        print("dummy for postaladdress is inserted")
    except Exception as e:
        print(e.with_traceback())
    
def insertassembly(cursor):
    """here inserting some of dummy entries for simple execution of program"""
    dummy = [
        "INSERT INTO ASSEMBLY VALUES(300000, 'JALE-478', 'JALE')",
        "INSERT INTO ASSEMBLY VALUES(300001, 'MOHALI-343', 'MOHALI')",
        "INSERT INTO ASSEMBLY VALUES(300002, 'KOTA-45', 'JAIPUR')",
        "INSERT INTO ASSEMBLY VALUES(300003, 'DUBAI-762', 'HABIBI')",
        "INSERT INTO ASSEMBLY VALUES(300004, 'TURKMENISTAN-43', 'LAMOA')"
    ]
    try:
        for value in dummy:
            cursor.execute(value)
        print("dummy assembly is inserted")
    except Exception as e:
        print(e.with_traceback())
