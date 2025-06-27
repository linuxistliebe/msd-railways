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


while True:
    print('''
----------------------------      
WELCOME TO MSD-RAILWAYS HOME
----------------------------

''')

    print()
    print('''
[1] Tickets 
[2] Login
[3] Register 
[4] Help
[5] Credits
[6] Quit                  
''')
    choice=int(input("Enter your choice -> "))
    if choice==6:
        typ("Quitting MSD-RAILWAYS Home...")
        exit()
    elif choice==5:
        typ(" GITHUB- https://github.com/linuxistliebe ")
        time.sleep(5)

    elif choice==4:
        typ("This is MSD-Railways Home. Here, you can open the Tickets Dashboard, login to your account (if exists), register an account, open the credits panel.")
        time.sleep(3)
    elif choice==2:
        print()
        username_query=input("Enter your USERNAME -> ")
        password_query=input("Enter your PASSWORD -> ")
        
        curs.execute("select * from account where username='{}' and pass='{}'".format(username_query, password_query))
        result=curs.fetchall()
        if len(result)==0:
            typ("(*) Wrong Password or Username!")

        else:
            time.sleep(0.8)
            for i in result:
                print(i)
        
    elif choice==1:
        print()
        username_create=input("Create a Username -> ")
        password_create=input("Create a Password -> ")
        city_create=input("Enter the name of your city -> ")
        age_create=int(input("Enter your age -> "))
        
        

    else:
        typ("Invalid Choice Entered!")
        time.sleep(2)
        
