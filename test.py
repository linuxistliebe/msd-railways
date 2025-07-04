#importing modules and establishing connection
import time
import mysql.connector as msd
con=msd.connect(host='localhost', user='root', password='seven', database='msd_db')
if con.is_connected():
    print("Connection has been established!")
else:
    print("Oops, some error has occured...")

curs=con.cursor()

#a function to get that "typewriter effect"
def typ(a):
    for i in a:
        print(i,end="")
        time.sleep(0.03)
def typfast(a):
    for i in a:
        print(i,end="")
        time.sleep(0.003)


# a while loop for the main menu of "MSD-RAILWAYS"
while True:
    typfast('''

-----------------------------     
WELCOME TO MSD-RAILWAYS HOME|
-----------------------------

''')

    print()
    typfast('''
[1] Login
[2] Register 
[3] Help
[4] Credits
[5] Quit
[6] Admin               
''')



    # logindash is a function for the dashboard displayed after logging in
    def logindash(loggedin_id):
        typ("(*)Logged in successfully as ")
        print(loggedin_id)
        while True:
                typfast('''

---------------------     
WELCOME TO DASHBOARD|
---------------------
''')

                typfast('''
[1] Reservation
[2] View current_ticket_status
[3] Cancellation
[4] Return to home                  
''')
                # this function is for viewing booked tickets by the user
                def current_ticket_status():
                    print()
                    curs.execute("select * from {} order by num".format(loggedin_id))
                    result_current_ticket_status=curs.fetchall()
                    if len(result_current_ticket_status)==0:
                        print("(*) No Tickets have been booked with this account!")
                        time.sleep(1.2)

                    else:
                        for i in result_current_ticket_status:
                            print(i)



                # this function is for cancellation of tickets booked by the user
                def cancellation():        
                    print()
                    tick_no=int(input("Enter the Ticket NO. to remove -> "))
                    curs.execute("delete from {} where num={}".format(loggedin_id,tick_no))
                    con.commit()
                    print("(*) Ticket NO.",tick_no,end="")
                    typ(" has been deleted!")
                    time.sleep(1.4)
                # this is a function for booking tickets from available options
                def reservation():
                    print()
                    
                    print('''
-----------------
AVAILABLE ROUTES|
-----------------
                        ''')
                    typfast('''
[1] Gotham to Empire Bay      7:00 AM
[2] Gotham to Metropolis      7:00 AM 
[3] Gotham to Vice City       7:00 AM  
[4] Empire Bay to Gotham      7:00 AM  
[5] Metropolis to Gotham      7:00 AM  
[6] Vice City to Gotham       7:00 AM  
[7] Empire Bay to Metropolis  7:00 AM  
[8] Metropolis to Vice City   7:00 AM
[9] <--Return    
''')
                    time.sleep(0.4)
                    tkt_choice=int(input("Select a TICKET to book -> "))
                    if tkt_choice==9:
                        pass
                    elif tkt_choice==8:
                        print("Ticket No.",tkt_choice,"booked successfully!")
                        time.sleep(0.8)
                        curs.execute("insert into {} values (8,100,'Metropolis','Vice City','7 AM','Flashpoint')".format(loggedin_id))
                        con.commit()

                    elif tkt_choice==7:
                        print("Ticket No.",tkt_choice,"booked successfully!")
                        time.sleep(0.8)
                        curs.execute("insert into {} values (7,100,'Empire Bay','Metropolis','7 AM','Flashpoint')".format(loggedin_id))
                        con.commit()

                    elif tkt_choice==6:
                        print("Ticket No.",tkt_choice,"booked successfully!")
                        time.sleep(0.8)
                        curs.execute("insert into {} values (6,100,'Vice City','Gotham','7 AM','Flashpoint')".format(loggedin_id))
                        con.commit()

                    elif tkt_choice==5:
                        print("Ticket No.",tkt_choice,"booked successfully!")
                        time.sleep(0.8)
                        curs.execute("insert into {} values (5,100,'Metropolis','Gotham','7 AM','Flashpoint')".format(loggedin_id))
                        con.commit()

                    elif tkt_choice==4:
                        print("Ticket No.",tkt_choice,"booked successfully!")
                        time.sleep(0.8)
                        curs.execute("insert into {} values (4,100,'Empire Bay','Gotham','7 AM','Flashpoint')".format(loggedin_id))
                        con.commit()

                    elif tkt_choice==3:
                        print("Ticket No.",tkt_choice,"booked successfully!")
                        time.sleep(0.8)
                        curs.execute("insert into {} values (3,50,'Gotham','Vice City','7 AM','LinuxEXP')".format(loggedin_id))
                        con.commit()

                    elif tkt_choice==2:
                        print("Ticket No.",tkt_choice,"booked successfully!")
                        time.sleep(0.8)
                        curs.execute("insert into {} values (2,50,'Gotham','Metropolis','7 AM','LinuxEXP')".format(loggedin_id))
                        con.commit()

                    elif tkt_choice==1:
                        print("Ticket No.",tkt_choice,"booked successfully!")
                        time.sleep(0.8)
                        curs.execute("insert into {} values (1,50,'Gotham','Empire Bay','7 AM','LinuxEXP')".format(loggedin_id))
                        con.commit()

                    else:
                        typ("(*)Invalid Choice Entered!")
                        time.sleep(1.2)

                choice_dash=int(input("Enter your choice -> "))
                
                #this one signs you out
                if choice_dash==4:
                    break

                # function for cancelling the previously books tickets by a user
                elif choice_dash==3:
                    typ("|CANCELLATION|")
                    print()
                    cancellation()

                #displays currently booked tickets by a user
                elif choice_dash==2:
                    typ("|current_ticket_status|")
                    print()
                    current_ticket_status()

                # takes you to the reservation function where you book tickets from available option
                elif choice_dash==1:
                    typ("|Reservation|")
                    reservation()

                else:
                    typ("(*)Invalid Choice Entered!")
                    time.sleep(1.8)

    # if-elif-else statements for the MSD-RAILWAYS menu options
    choice=int(input("Enter your choice -> "))
    if choice==5:
        typ("Quitting MSD-RAILWAYS Home...")
        con.close()
        exit()
    elif choice==4:
        typ(" GITHUB- https://github.com/linuxistliebe ")
        time.sleep(5)

    elif choice==3:
        typ("This is MSD-Railways Home. Here, you can open the Tickets Dashboard, login to your account (if exists), register an account, open the credits panel.")
        time.sleep(3)

    # this one is for loggin in, checks username and password and drops you to the dashboard mentioned previously
    elif choice==1:
        print()
        username_query=input("Enter your USERNAME -> ")
        password_query=input("Enter your PASSWORD -> ")
        
        curs.execute("select * from account where username='{}' and pass='{}'".format(username_query, password_query))
        result=curs.fetchall()
        if len(result)==0:
            typ("(*) Wrong Password or Username!")

        else:
            time.sleep(0.8)
            logindash(username_query)
            

        time.sleep(2)

    #this one is for creating an account    
    elif choice==2:
        print()
        username_create=input("Create a Username -> ")
        password_create=input("Create a Password -> ")
        city_create=input("Enter the name of your city -> ")
        age_create=int(input("Enter your age -> "))
        name_create=input("Enter your name -> ")
        curs.execute("SELECT username from account where username='{}'".format(username_create))
        result_crt=curs.fetchall()
        if len(result_crt)==0:
            curs.execute("insert into account values('{}','{}','{}','{}','{}')".format(name_create,username_create,age_create,city_create,password_create))     
            con.commit()
            time.sleep(1.7)
            curs.execute("create table {}(num int, price int, from_city varchar(30), to_city varchar(30), time varchar(10), train_name varchar(10))".format(username_create))
            print("Account Created","(*)USERNAME -",username_create)
        else:
            print("USERNAME -",username_create,"is not available!")
            time.sleep(1.3)


    #ADMIN MENU- for admins
    elif choice==6:
        print()
        typfast("(*)Verify Yourself before heading to the ADMIN MENU!")
        print()
        # PASSWORD FOR ADMIN is the secretCode
        secretCode=input("Enter the secretCode -> ")
        curs.execute("select scode from admin")
        scode=curs.fetchone()[0]
        if secretCode==scode:
            while True:
                print()
                typfast("Welcome ADMIN")
                print()
                typ("~~~ With great power comes great resposibility!")
                typfast('''
---------------------------------                
[1] Display all available tickets
[2] Display ACCOUNTS 
[3] Display PASSWORDS
[4] Change the secretCode
[5] eXit root-admin-mode
---------------------------------
''')
                opt=int(input("Enter your choice -> "))
                if opt==5:
                    typfast("[!]:eXiting root-admin-mode")
                    break

                #changing secretCode
                elif opt==4:
                    print()
                    new_scode=input("Enter the new secretCode (make sure it's strong!) -> ")
                    curs.execute("update admin set scode='{}'".format(new_scode))
                    con.commit()

                #2-step verification implemented
                elif opt==3:
                    print()
                    ans=int(input("What is 1+1? "))
                    if ans==2:
                        print()
                        typfast("Fetching Passwords...")
                        print()
                        curs.execute("select username, pass from account;")
                        result=curs.fetchall()
                        for i in result:
                            print(i)
                        time.sleep(3)

                    #if secondary test fails
                    else:
                        typ("Nice Try. Now get out!")
                        con.close()
                        exit()

                #2-step verification implemented
                elif opt==2:
                    print()
                    ans=int(input("What is 1+1 in Boolean Algebra? "))
                    if ans==1:
                        print()
                        typfast("Fetching Accounts...")
                        print()
                        curs.execute("select * from account;")
                        result=curs.fetchall()
                        for i in result:
                            print(i)

                    #if secondary test fails
                    else:
                        typ("Nice Try. Now get out!")
                        con.close()
                        exit()

                #this one just fetches the available tickets!
                elif opt==1:
                    print()
                    curs.execute("select * from tickets")
                    result=curs.fetchall()
                    for i in result:
                        print(i)
                        time.sleep(3)

    # invalid input given by user in MSD-RAILWAYS menu
    else:
        typ("(*)Invalid Choice Entered!")
        time.sleep(1.8)
 #end of the project, finally!
 #Check out my github profile -> https://github.com/linuxistliebe      
 #Check out the repository    ->https://github.com/linuxistliebe/msd-railways 
