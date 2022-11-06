# 1. Write a python program to create a user class with 3 properties : name, age, email.

class user:
    pass

u1=user()
u1.name="Hari"
u1.age=25
u1.email="harikesh@gmail.com"

print(u1.name)
print(u1.age)
print(u1.email)

# or

class user:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email

u1=user("hari",15,"harikesh@gmail.com")
print(u1.name,u1.age,u1.email)

# or

class user:
    def __init__(self):
        self.name="Hari"
        self.age=15
        self.email="harikesh@gmail.com"

u1=user()
print(u1)
print(u1.name,u1.age,u1.email)

# 2. Write a python program to create a user class with a method to greet the user.

class user:
    def __init__(self):
        pass
    def salute(self):
        print("Hi there !!")

u1=user()
u1.salute() # calling with user object

user.salute()  # calling with class

# 3. Write a python program to create 2 objects of the user class and assign different values.

class user:
    def __init__(self,name,age):
        self.name=name  
        self.age=age  

u1=user("ram",34)
u2=user("shyam",45)

print("for first object: ",u1.age,u1.name)
print("for first object : ",u2.age,u2.name)

# 4. Write a python program to init deeault values for user object using __init__ method. 

class user:
    def __init__(self):
        self.name="Hari"
        self.age=15

u1=user()
print(u1.name,u1.age)

# 5. Write a python program to delete the age property of the user. 

class user:
    def __init__(self):
        self.name="Hari"
        self.age=15

u1=user()
u1.age=""
print("Name : ",u1.name,"Age : ",u1.age)

# 6. Write a python program to create 3 user objects and find the youngest of all.

class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def compare(self,f1,f2):
        if self.age > f1.age and self.age > f2.age:
            print("user 1 age is greater")
        elif f1.age > f2.age:
            print("user 2 age is greater")
        else:
            print("user 3 age is greater")
u1=user("hari",90)
u2=user("ram",45)
u3=user("ramesh",34)

u1.compare(u2,u3) # user.compare(u1,u2,u3)


# 7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
# hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the values).

class laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu 
        self.hdd=hdd

    def showConfig(self):
        print(self.brand,self.cpu,self.ram,self.hdd)
l1=laptop("lenovo","16gb","i5","250gb")
l1.showConfig()

# 8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted order based on the ram size.

class laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu 
        self.hdd=hdd

    def showConfig(self):
        print(self.brand,self.cpu,self.ram,self.hdd)

    def compare(self,l2,l3):
        if self.ram > l2.ram and self.ram > l3.ram:
            if l2.ram > l3.ram:
                print([l1.brand,l2.brand,l3.brand])
            else:
                print([l1.brand,l3.brand,l2.brand])
            
        elif l2.ram > l3.ram and l2.ram >l1.ram:
            if l3.ram > l1.ram:
                print([l2.brand,l3.brand,l1.brand])
            else:
                print([l2.brand,l1.brand,l3.brand])
        else:
            if l2.ram > l1.ram:
                print([l3.brand,l2.brand,l1.brand])
            else:
                print([l3.brand,l1.brand,l2.brand])

l1=laptop("lenovo","5gb","i5","250gb")
l2=laptop("hp","9gb","i5","250gb")
l3=laptop("dell","8gb","i5","250gb")
l1.showConfig()
l2.showConfig()
l3.showConfig()

l1.compare(l2,l3)

# 9. Write a python program to create a School class and 3 instance variables and 1 class variable.

class school:
    sch="kandivali"   # class variable
    def __init__(self):
        self.name="hari"   # Instance variable
        self.age=15
    
s1=school()
print(s1.name,s1.age, school.sch)

# 10. Define a class Employee with instance object variables empid, name, salary. Write
# __init__() method in the class to initialize instance object variables. Also define
# instance methods to input fields and display field values

class employee:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary

e1=employee("101","kar","5000")
print(e1.empid,e1.name,e1.salary)


# Just for practise

# class computer:
#     brand = "HP"    # Class variable
#     def __init__(self,a,b):
#         self.cpu=a    # self.cpu and self.ran is instance variable
#         self.ran=b

#     def show(self):
#         print(self.cpu,self.ran)


# com1=computer("i7","16gb")
# # com1.cpu="i7"

# com2=computer("i11","20gb")
# # com2.cpu="i11"

# # print(com1.cpu,com1.ran)
# # print(com2.cpu)

# # computer.show(com1)
# com1.show()
# # computer.show(com2)
# com2.show()
# print(computer.brand)