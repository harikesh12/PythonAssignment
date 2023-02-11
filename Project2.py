# This means we have to create a menu-driven console application, where multiple users
# can create their account,
# We have to create an authentication system :
# 1. Registration
# 2. Login (If user is already registered)
# After successful authentication, user should have right to
# 1. Add contacts
# 2. Read all contacts
# 3. Read any specific contact
# 4. Update any specific contact
# 5. Delete any specific contact
# 6. Delete all contacts



# 1. Add contacts
def phonebook_addcontacts(name):
    phone_name=input("Enter the Name of person : ")
    phone_number=input("Enter the Number of Person : ")
    phone_password=input("Enter the Password : ")
    insert_phonebook = 'INSERT INTO phonebook(name,phone_name,phone_number,password) VALUES(%s,%s,%s,%s)'
    insert_phonevalue = (name,phone_name,phone_number,phone_password)
    cursor.execute(insert_phonebook,insert_phonevalue)
    print("Phone book created Successfully !!")

# 2. Read all contacts
def phonebook_read(name):
    spec_query='SELECT * fROM phonebook WHERE name = %s'
    spec_value=(name,)
    cursor.execute(spec_query,spec_value)
    spec_rec=[]
    for rcd in cursor.fetchall():
        spec_rec.append(rcd[0])
    if name in spec_rec:
        read_query="""SELECT * FROM phonebook WHERE name = %s"""
        query_value=(name,)
        cursor.execute(read_query,query_value)
        for rec in cursor.fetchall():
          print(rec)
    else:
        print("No record for this User")

# 3. Read any specific contact
def phonebook_specread(name,spec_input):
    # to check if spec_input exist in database or not
    spec_query='SELECT * fROM phonebook WHERE name = %s'
    spec_value=(name,)
    cursor.execute(spec_query,spec_value)
    spec_rec=[]
    for rcd in cursor.fetchall():
        spec_rec.append(rcd[1])
    if spec_input in spec_rec:
        read_query="""SELECT * FROM phonebook WHERE name = %s AND phone_name= %s"""
        query_value=(name,spec_input)
        cursor.execute(read_query,query_value)
        for rec in cursor.fetchall():
          print(rec)
    else:
        print("This name does not exist in your phone Book")

# 4. Update any specific contact
def phonebook_conupdate(number,p_name,name):
    spec_query='SELECT * fROM phonebook WHERE name = %s'
    spec_value=(p_name,)
    cursor.execute(spec_query,spec_value)
    spec_rec=[]
    for rcd in cursor.fetchall():
        spec_rec.append(rcd[1])
    if p_name in spec_rec:
        update_query='UPDATE phonebook SET phone_number=%s WHERE phone_name=%s and name=%s'
        update_value=(number,p_name,name)
        cursor.execute(update_query,update_value)
        print("Record Updated Successfully")
    else:
        print("This person does not exist")

# 5. Delete any specific contact
def phonebook_specdelete(name,ph_name):
    try:
        spec_query='SELECT * fROM phonebook WHERE name = %s'
        spec_value=(ph_name,)
        cursor.execute(spec_query,spec_value)
        spec_rec=[]
        for rcd in cursor.fetchall():
            spec_rec.append(rcd[1])
        if ph_name in spec_rec:
            del_query='DELETE FROM phonebook where phone_name= %s and name=%s'
            del_value=(ph_name,name)
            cursor.execute(del_query,del_value)
            print("Contact deleted successfully")
        else:
            print("This person does not exist")
    except Exception as error:
        print(error)

# 6. Delete all contacts
def phonebook_delete(name):
    try:
        del_query='DELETE FROM phonebook where name=%s'
        del_value=(name,)
        cursor.execute(del_query,del_value)
        print("Contacts deleted successfully")
    except Exception as error:
        print(error)

# Registration function
def registration():
    name=input("Enter your Name : ")
    email=input("Enter your Email ID: ")
    password=gp.getpass(prompt="Enter your Password : ")
    fetch_script = 'SELECT * from userdata'
    cursor.execute(fetch_script)
    record_list=[]
    for  record in cursor.fetchall():
        record_list.append(record[0])
    if name in record_list:
            print("This record already Exist")
    else:
                insert_script= 'INSERT INTO userdata(name,email,password) VALUES(%s,%s,%s)'
                insert_value=(name,email,password)
                cursor.execute(insert_script,insert_value)
                print("Your registered Successfully !!")
                phone_in=input("Do you want to proceed for creating Digital Phonebook(Yes/No):")
                if phone_in.lower() == "yes" or phone_in.lower() == "y" :
                    phonebook_addcontacts(name)
                else:
                    exit()    






import getpass as gp
import psycopg2

## Connect to the DB
connection=None
cursor=None
try:
    connection = psycopg2.connect(
            host = "127.0.0.1",
            port = "5432",
            database = "",   # enter your db name
            user="postgres",
            password=""   #enter your db password

    )
    connection.autocommit = True # "autcommit" set to True, so you don't have to commit your queries.
    cursor = connection.cursor()
    create_db_query = f'''  CREATE TABLE IF NOT EXISTS userdata (
                            name varchar(40) NOT NULL PRIMARY KEY,
                            email varchar(70) NOT NULL,
                            password varchar(90) NOT NULL)'''
    cursor.execute(create_db_query)
    create_db_query2 = f'''  CREATE TABLE IF NOT EXISTS phonebook (
                            name varchar(40) NOT NULL,
                            FOREIGN KEY (name) REFERENCES userdata(name),
                            phone_name varchar(40) NOT NULL,
                            phone_number int NOT NULL,
                            password varchar(90) NOT NULL)'''
    cursor.execute(create_db_query2)
    reg_in=input("Are you registered user(yes/no)?: ")
    
    
    # 2. Login (If user is already registered)
    if reg_in.lower() == "yes" or reg_in.lower() == "y":
        # to verify if used exist in userdata table
        reg_select = 'SELECT * FROM userdata'
        cursor.execute(reg_select)
        reg_list=[]
        for db_name in cursor.fetchall():
            reg_list.append(db_name[0])
        reg_name=input("Enter your name : ")
        if reg_name in reg_list:            # if user exist then he can perform below operation
            print("1. Add contacts" , "\n",
                  "2. Read all contacts" ,"\n",
                  "3. Read any specific contact","\n",
                  "4. Update any specific contact","\n",
                  "5. Delete any specific contact","\n",
                  "6. Delete all contacts")
            action_input=int(input("Enter the Action Number: "))
            match action_input:
                case 1:
                    phonebook_addcontacts(reg_name)
                case 2:
                    phonebook_read(reg_name)
                case 3:
                    spec_input=input("Enter the name of person's contact to read : ")
                    phonebook_specread(reg_name,spec_input)
                case 4:
                    c_name=input("Enter the name of person's contact to update : ")
                    phone_nu=input("Enter the new contact Number: ")
                    phonebook_conupdate(phone_nu,c_name,reg_name)
                case 5:
                    ph_name=input("Enter the name of person's contact to delete : ")
                    phonebook_specdelete(reg_name,ph_name)
                case 6:
                     phonebook_delete(reg_name)

        else:
            print("You are not registered User")
            # if after saying registered user , you are not registered then register function getting called
            r_input=input("Do you want to register yourself(Yes/No) ? ")
            if r_input.lower() == "yes" or r_input.lower() == "y":
                registration()
            else:
                exit()

    # 1. Registration for new user
    elif reg_in.lower() == "no" or reg_in.lower() == "n":
        # name=input("Enter your Name : ")
        # email=input("Enter your Email ID: ")
        # password=gp.getpass(prompt="Enter your Password : ")
        # Registration function is getting called
        registration()
    else:
        print("Enter correct option")
except Exception as error:
    print(error)

finally:
    if connection is not None:
        connection.close()
    if cursor is not None:
        cursor.close()