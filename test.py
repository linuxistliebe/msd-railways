import time
import mysql.connector as msd
con=msd.connect(host='localhost', user='root', password='seven', database='msd_db')
if con.is_connected():
    print("Connection has been established!")
else:
    print("Oops, some error has occured...")

curs=con.cursor()

def typ(a):
    for i in a:
        print(i,end="")
        time.sleep(0.03)
def typfast(a):
    for i in a:
        print(i,end="")
        time.sleep(0.003)



while True:
    typfast('''

----------------------------      
WELCOME TO MSD-RAILWAYS HOME
----------------------------

''')

    print()
    typfast('''
[1] Login
[2] Register 
[3] Help
[4] Credits
[5] Quit                  
''')




    def logindash():
        typ("(*)Logged in successfully")
        print()
        while True:
                typfast('''

--------------------      
WELCOME TO DASHBOARD
--------------------
''')

                typfast('''
[1] Reservation
[2] View current_ticket_status
[3] Cancellation
[4] Return to home                  
''')
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

                    elif tkt_choice==7:
                        print("Ticket No.",tkt_choice,"booked successfully!")
                        time.sleep(0.8)

                    elif tkt_choice==6:
                        print("Ticket No.",tkt_choice,"booked successfully!")
                        time.sleep(0.8)

                    elif tkt_choice==5:
                        print("Ticket No.",tkt_choice,"booked successfully!")
                        time.sleep(0.8)

                    elif tkt_choice==4:
                        print("Ticket No.",tkt_choice,"booked successfully!")
                        time.sleep(0.8)

                    elif tkt_choice==3:
                        print("Ticket No.",tkt_choice,"booked successfully!")
                        time.sleep(0.8)

                    elif tkt_choice==2:
                        print("Ticket No.",tkt_choice,"booked successfully!")
                        time.sleep(0.8)

                    elif tkt_choice==1:
                        print("Ticket No.",tkt_choice,"booked successfully!")
                        time.sleep(0.8)

                    else:
                        typ("(*)Invalid Choice Entered!")
                        time.sleep(1.2)

                choice_dash=int(input("Enter your choice -> "))
                if choice_dash==4:
                    break
                elif choice_dash==3:
                    typ("|CANCELLATION|")
                    print()
                elif choice_dash==2:
                    typ("|current_ticket_status|")
                    print()

                elif choice_dash==1:
                    typ("|Reservation|")
                    reservation()

                else:
                    typ("(*)Invalid Choice Entered!")
                    time.sleep(1.8)


    choice=int(input("Enter your choice -> "))
    if choice==5:
        typ("Quitting MSD-RAILWAYS Home...")
        exit()
    elif choice==4:
        typ(" GITHUB- https://github.com/linuxistliebe ")
        time.sleep(5)

    elif choice==3:
        typ("This is MSD-Railways Home. Here, you can open the Tickets Dashboard, login to your account (if exists), register an account, open the credits panel.")
        time.sleep(3)
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
            logindash()
            

        time.sleep(2)
        
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
            print("Account Created","(*)USERNAME -",username_create)
        else:
            print("USERNAME -",username_create,"is not available!")
            time.sleep(1.3)
    else:
        typ("(*)Invalid Choice Entered!")
        time.sleep(1.8)
        
