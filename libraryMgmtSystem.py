import mysql.connector as a
con = a.connect(host="localhost",user="root",password="12345",database="library")

def addBook():
    bookName = input("Enter Book Name :")
    bookCode = input("Enter Book Code :")
    bookTotal = input("Total Books :")
    subject = input("Enter Subject :")
    data = (bookName,bookCode,bookTotal,subject)
    sql = 'insert into books values(%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">----------------------------------------------------------------------------------------------<")
    print("Data Entered Successfully")
    main()

def issueBook():
    name = input("Enter Your Name :")
    registration = input("Enter Rwgistraton No. :")
    bookCode = input("Enter Book Code :")
    date = input("Enter Date :")
    data = (name,registration,bookCode,date)
    sql = 'insert into issue values(%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">----------------------------------------------------------------------------------------------<")
    print("Book issued to :",name)
    bookup(bookCode,-1)

def submitBook():
    name = input("Enter Your Name :")
    registration = input("Enter Rwgistraton No. :")
    bookCode = input("Enter Book Code :")
    date = input("Enter Date :")
    data = (name,registration,bookCode,date)
    sql = 'insert into submit values(%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">----------------------------------------------------------------------------------------------<")
    print("Book submitted to :",name)
    bookup(bookCode,1)

def bookup(co,u):
    bookCode = input("Enter BookCode:")
    a = 'select totalbooks from books where bookcode = %s'
    data = (bookCode,)
    c = con.cursor()
    c.execute(a,data)
    myResult = c.fetchone()
    t = myResult[0] + u
    sql = 'update books set totalBooks = %s where bookcode = %s'
    data1 = (t,bookCode)
    c.execute(sql,data1)
    con.commit()
    main()

def delBook():
    bookCode = input("Enter Book code :")
    sql = 'delete from books where bookcode = %s'
    data = (bookCode,)
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    main()

def displayBook():
    sql = 'select * from books'
    c = con.cursor()
    c.execute(sql)
    myResult = c.fetchall()
    for i in myResult:
        print("Book Name :",i[0])
        print("Book Code :",i[1])
        print("Total :",i[2])
        print(">----------------------------------------------------------------------------------------<")
    main()

def main():
    print("""
                                            LIBRARY MANAGEMENT SYSTEM
    1.ADD BOOK
    2.ISSUE BOOK
    3.SUBMIT BOOK
    4.DELETE BOOK
    5.DISPLAY BOOK
    """)

    choice = input("Enter Task No :")
    print(">-----------------------------------------------------------------------------------------<")
    if(choice == '1'):
        addBook()
    elif(choice == '2'):
        issueBook()
    elif(choice == '3'):
        submitBook()
    elif(choice == '4'):
        delBook()
    elif(choice == '5'):
        displayBook()
    else:
        print("Wrong Choice......")
        main()

def pswd():
    ps = input("Enter Password :")
    if ps == "himanshu":
        main()
    else:
        print("Wrong Password")
        pswd()

pswd()

    





