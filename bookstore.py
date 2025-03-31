import mysql.connector
mydb=mysql.connector.connect (host="localhost", user="root", password="12345")
#CREATING DATABASE AND TABLE
mycursor=mydb.cursor()
mycursor.execute("create database if not exists book_store")
mycursor.execute("use book_store")
mycursor.execute("create table if not exists signup(username varchar(20),password varchar(20))")
while True:
    def LOGIN():
        print("""1:Signup
2:Login""")
        ch=int(input("SIGNUP/LOGIN(1,2):"))
    #SIGNUP
        if ch==1:
            username=input("USERNAME:")
            pw=input("PASSWORD:")

            mycursor.execute("insert into signup values('"+username+"','"+pw+"')")
            mydb.commit()

    #LOGIN
        elif ch==2:

            username=input("USERNAME:")

            mycursor.execute("select username from signup where username='"+username+"'")
            pot=mycursor.fetchone()

            if pot is not None:
                print("VALID USERNAME!!!!!!")

                pw=input("PASSWORD:")

                mycursor.execute("select password from signup where password='"+pw+"'")
                a=mycursor.fetchone()

                if a is not None:
                    print("""+++++++++++++++++++++++
+++LOGIN SUCCESSFULL+++
+++++++++++++++++++++++""")
    LOGIN()
    print("""======================================================================
++++++++++++++++++++++++++    MY BOOK BOOK_STORE     +++++++++++++++++++++++++
==========================================================================""")

    mycursor.execute("create table if not exists Books(BookName varchar(30) primary key,Genre varchar(20),Quantity int(3),Author varchar(20),Publication varchar(30),Price int(4),Total int(8))")
    mydb.commit()
    mycursor.execute("create table if not exists sell(CustomerName varchar(20),PhoneNumber char(12) primary key, BookName varchar(30),Quantity int(100),Price int(4),total_price int(8),foreign key (BookName) references Books(BookName))")
    mydb.commit()
    mycursor.execute("create table if not exists Staff_details(Name varchar(30), Gender varchar(10),Age int(3), PhoneNumber char(12) unique key , Address varchar(40))") 
    mydb.commit()
    while True:
            print("""1:Add Books
2:Sell Books
3:Search Books(for Availability)
4:Staff Details
5:Sell Record
6:Available Books
7:Total Income after the Latest Reset 
8:Exit""")
            a=int(input("Enter your choice:"))
            if a==1:
                def ADDBOOKS():
                    print("All information prompted are mandatory to be filled")
                    book=str(input("Enter Book Name:"))
                    genre=str(input("Genre:"))
                    quantity=int(input("Enter quantity:"))        
                    author=str(input("Enter author name:"))
                    publication=str(input("Enter publication house:"))
                    price=int(input("Enter the price:"))
                    total=quantity*price
                    mycursor.execute("select * from Books where bookname='"+book+"'")
                    row=mycursor.fetchone()
                    if row is not None:
                        mycursor.execute("update Books set quantity=quantity+'"+quantity+"' where bookname='"+book+"'")
                        mydb.commit()
                        print("""++++++++++++++++++++++
++SUCCESSFULLY ADDED++
++++++++++++++++++++++""")
                    else:
                        mycursor.execute("insert into Books(bookname,genre,quantity,author,publication,price,total) values('"+book+"','"+genre+"','"+str(quantity)+"','"+author+"','"+publication+"','"+str(price)+"', '"+str(total)+"')")
                        mydb.commit()
                        print("""++++++++++++++++++++++
++SUCCESSFULLY ADDED++
++++++++++++++++++++++""")
                ADDBOOKS()
            if a==2:
                def DELETE():
                    print("AVAILABLE BOOKS...")
                    mycursor.execute("select * from Books ")
                    for x in mycursor:
                        print(x)
                    cusname=str(input("Enter customer name:"))
                    phno=input("Enter phone number:")
                    book=str(input("Enter Book Name:"))
                    price=int(input("Enter the price per book:"))
                    n=int(input("Enter quantity :"))
                    f=price*n
                    mycursor.execute("select quantity from Books where bookname='"+book+"'")
                    lk=mycursor.fetchone()
                    if max(lk)<n:
                        print(n,"Books are not available!!!!")
                    else:
                        mycursor.execute("select bookname from Books where bookname='"+book+"'")
                        log=mycursor.fetchone()
                        if log is not None:
                            mycursor.execute("insert into sell values('"+cusname+"','"+phno+"','"+book+"','"+str(n)+"','"+str(price)+"','"+str(f)+"')")
                            mydb.commit()
                            mycursor.execute("update Books set quantity=quantity-'"+str(n)+"', total=total-'"+str(f)+"' where BookName='"+book+"'")
                            mydb.commit()
                            print("""++++++++++++++++++++++
++BOOK HAS BEEN SOLD++
++++++++++++++++++++++""")
                        else:
                            print("BOOK IS NOT AVAILABLE!!!!!!!")
                DELETE()
            if a==3:
                def SEARCH_BOOKS():
                    print("""1:Search by name
2:Search by genre
3:Search by author""")
                    l=int(input("Search by?:"))
#BY BOOKNAME
                    if l==1:
                        o=input("Enter Book to search:")
                        mycursor.execute("select bookname from Books where bookname='"+o+"'")
                        tree=mycursor.fetchone()
                        if tree!=None:
                            print("""++++++++++++++++++++
++BOOK IS IN STOCK++
++++++++++++++++++++""")
                        else:
                            print("BOOK IS NOT IN STOCK!!!!!!!")
#BY GENRE
                    if l==2:
                            g=input("Enter genre to search:")
                            mycursor.execute("select genre from Books where genre='"+g+"'")
                            poll=mycursor.fetchall()
                            if poll is not None:
                                print("""++++++++++++++++++++
++BOOK IS IN STOCK++
++++++++++++++++++++""")
                                mycursor.execute("select * from Books where genre='"+g+"'")
                                for y in mycursor:
                                    print(y)
                            else:
                                print("BOOKS OF SUCH GENRE ARE NOT AVAILABLE!!!!!!!!!")
#BY AUTHOR NAME
                    if l==3:
                            au=input("Enter author to search:")
                            mycursor.execute("select author from Books where author='"+au+"'")
                            home=mycursor.fetchall()
                            if home is not None:
                                print("""++++++++++++++++++++
++BOOK IS IN STOCK++
++++++++++++++++++++""")

                                mycursor.execute("select * from Books where author='"+au+"'")
                                for z in mycursor:
                                    print(z)
                            else:
                                print("BOOKS OF THIS AUTHOR ARE NOT AVAILABLE!!!!!!!")
                                    
                SEARCH_BOOKS()
                #STAFF DETAILS
            if a==4:
                def STAFF_DETAILS():
                    print("1:New staff entry")
                    print("2:Remove staff")
                    print("3:Existing staff details")
                    ch=int(input("Enter your choice:"))
#NEW STAFF ENTRY
                    if ch==1:
                        fname=str(input("Enter Fullname:"))
                        gender=str(input("Gender(M/F/O):"))
                        age=int(input("Age:"))
                        phoneno=input("Staff phone no.:")
                        add=str(input("Address:"))
                        mycursor.execute("insert into Staff_details(name,gender,age,phonenumber,address) values('"+fname+"','"+gender+"','"+str(age)+"','"+phoneno+"','"+add+"')")
                        mydb.commit()
                        print("""+++++++++++++++++++++++++++++
+STAFF IS SUCCESSFULLY ADDED+
+++++++++++++++++++++++++++++""")
                        
#REMOVE STAFF
                    elif ch==2:
                        nm=str(input("Enter staff name to remove:"))
                        mycursor.execute("select name from staff_details where name='"+nm+"'")
                        toy=mycursor.fetchone()
                        if toy is not None:
                            mycursor.execute("delete from staff_details where name='"+nm+"'")
                            print("""+++++++++++++++++++++++++++++++++
++STAFF IS SUCCESSFULLY REMOVED++
+++++++++++++++++++++++++++++++++""")
                            mydb.commit()
                        else:
                            print("STAFF DOESNOT EXIST!!!!!!")
#EXISTING STAFF DETAILS
                    elif ch==3:
                        mycursor.execute("select * from Staff_details")
                        run=mycursor.fetchall()
                        if run is not None:
                                print("EXISTING STAFF DETAILS...")
                                for t in run:
                                    print(t)
                                                    
                        else:
                            print("NO STAFF EXISTS!!!!!!!")
                        mydb.commit()
                STAFF_DETAILS()       
#SELL HISTORY                                
            if a==5:
                def SELL_HISTORY():
                    print("1:Sell history details")
                    print("2:Reset Sell history")
                    ty=int(input("Enter your choice:"))
                    if ty==1:
                        mycursor.execute("select * from sell")
                        for u in mycursor:
                            print(u)
                    if ty==2:
                        bb=input("Are you sure(Y/N):")
                        if bb=="Y":
                            mycursor.execute("delete from sell")
                            mydb.commit()
                        elif bb=="N":
                            pass
                SELL_HISTORY()
#AVAILABLE BOOKS
            if a==6:
                def AVAILABLE():
                    mycursor.execute("select * from Books order by bookname")
                    for v in mycursor:
                        print(v)
                AVAILABLE()
#TOTAL INCOME AFTER LATEST UPDATE
            if a==7:
                def TOTAL():
                    mycursor.execute("select sum(total_price) from sell")
                    for x in mycursor:
                        print(x)
                TOTAL()
#EXIT                    
            elif a==8:
                break
    break

