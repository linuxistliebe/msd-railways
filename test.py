import mysql.connector as msd
con=msd.connect(host='localhost', user='root', password='seven', database='msd_db')
if con.is_connected():
    print("Connection has been established!")
else:
    print("Oops, some error has occured...")

while True:
    print('''
----------------------------      
WELCOME TO MSD-RAILWAYS HOME
----------------------------

''')

    print()
    print('''
[1] 
[2] 
[3] Login
[4] Register 
[5] Help
[6] Credits
[7] Quit                  
''')
    choice=int(input("Enter your choice -> "))
    if choice==7:
        print("Quitting MSD-RAILWAYS Home...")
        exit()
    elif choice==6:
        print(" GITHUB- https://github.com/linuxistliebe ")

    elif choice==5:
        print("This is MSD-Railways Home. Here, you can register your account, purchase tickets, view details, etc. If you have an already exisiting account, then use it to login!")

