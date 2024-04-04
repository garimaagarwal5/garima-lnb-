import mysql.connector
def register_user():
    print("Registration")
    username=input("Enter Username")
    password=input("Enter password")
    email=input("Enter email id")
    name=input("enter name")
    try:
        mydb=mysql.connector.connect(host="localhost",user='root',
                                passwd='Admin@123',database='garima',auth_plugin='mysql_native_password')

        if mydb.is_connected():
            print("Successfully connected with DATABASE")
            cursor=mydb.cursor()
            '''query1="create table users1(username varchar(50),password varchar(50),name varchar(50),email varchar(50)) ";
            cursor.execute(query1); '''  
            query2="insert into users1 (username,password,name,email) values(%s,%s,%s,%s)"
            cursor.execute(query2,(username,password,name,email))
            mydb.commit()
            print("Registration successfully")
    except mysql.connector.Error as err:
        print(f"Error:{err}")
    finally:
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()
        print("Connection closed")
def login_user():
    print("#####LoGIN#####")
    username=input("enter username")
    password=input("enter password")
    try:
        mydb=mysql.connector.connect(host="localhost",user='root',
            passwd='Admin@123',database='garima',auth_plugin='mysql_native_password');
        cursor=mydb.cursor()
             
        query="select * from users1 where username=%s and password=%s"
        cursor.execute(query,(username,password))
        user=cursor.fetchone()
        if user:
            print("login sucessfully")
        else:
            print("Enter correct username and password")
    except mysql.connector.Error as err:
        print(f"Error:{err}")
        
    finally:
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()
            print("Connection closed")

while True:
    print("User Authentication System ")
    print("press 1 for Registration")
    print("2.Login")
    print("3.Exit")
    choice=int(input("enter choice"))
    if choice==1:
        register_user()
    elif choice==2:
        login_user()
    elif choice==3:
        print("Exiting program .Goodbye")
        break
    else:
        print("Enter correct value")
