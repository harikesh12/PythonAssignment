# 1. Write a python script to create a Profile class with 3 attributes (name, email, age).

class profile:
    def __init__(self):
        self.name="hari"
        self.email="hari@gmail.com"
        self.age=15

p1=profile()
print(p1.age,p1.email,p1.name)


# 2. Write a python script to update the above Profile class with encapsulation.

class profile:
    def __init__(self):
        self.name=None
        self.email=None
        self.age=None

    def get_profile(self):
        return self.name,self.age,self.email

    def set_profile(self,name,age,email):
        self.name=name 
        self.age=age 
        self.email=email

p1=profile()
p1.set_profile("hari",15,"hari@gmail.com")

print(p1.get_profile())
print(p1.age)

# 3. Write a python script to update 2nd Question, change email and age to __email and __age.

class profile:
    def __init__(self):
        self.name=None
        self.email=None
        self.age=None

    def get_profile(self):
        return self.name,self.__age,self.__email

    def set_profile(self,name,age,email):
        self.name=name 
        self.__age=age 
        self.__email=email

p1=profile()
p1.set_profile("hari",15,"hari@gmail.com")

print(p1.get_profile())
print(p1.age,p1.name)

# 4. Write a python script to update 2nd Question, add a class variable (platform) and create a classmethod to access it.

class profile:
    platform="xyz"
    def __init__(self):
        self.name=None
        self.email=None
        self.age=None

    def get_profile(self):
        return self.name,self.age,self.email

    def set_profile(self,name,age,email):
        self.name=name 
        self.age=age 
        self.email=email
    
    @classmethod
    def class_platform(cls):
        return cls.platform

p1=profile()
p1.set_profile("hari",15,"hari@gmail.com")
print(p1.get_profile())
print(p1.class_platform())   # class variable can be accessed via object 
print(profile.class_platform())  # class variable can be also accesssed via class 

# 5. Write a python script to create a Calculator class with 2 methods for adding and subtracting 2 values.

class calculator:
    def __init__(self):
        self.num1=None
        self.num2=None
    def set_values(self,num1,num2):
        self.__num1=num1
        self.__num2=num2
    def add(self):
        return self.__num1+self.__num2
    def sub(self):
        return self.__num1-self.__num2

c1=calculator()
c1.set_values(int(input("enter the num1 : ")),int(input("enter the num2 : ")))
print("Select from following option", "1-Addition", "2-Subtraction",sep="\n")
a=int(input("enter the Input here : "))

match a:
    case 1:
        print("Addition : ",c1.add())
    case 2:
        print("Subtraction is : ",c1.sub())
    case _:
        print("Invalid Input")  

# 6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication
# and division of 2 values and inherit it from the Calculator class.

class calculator:
    def __init__(self):
        self.num1=None
        self.num2=None
    def set_values(self,num1,num2):
        self.num1=num1
        self.num2=num2

class calculator2(calculator):
    def multiplication(self):
        return self.num1*self.num2
    def division(self):
        return self.num1/self.num2


c1=calculator2()
c1.set_values(int(input("enter the num1 : ")),int(input("enter the num2 : ")))
print(c1.multiplication())
print(c1.division())


# 7. Write a python script to create a Phone class with 2 methods to print the features
# (calling and sms).

class phone:
    def __init__(self):
        self.time=None
        self.callRate=None
        self.smsRate=None

    def set_sms(self,smsRate,time):
        self.smsRate=smsRate
        self.time=time

    def set_calling(self,callRate,time):
        self.callRate=callRate
        self.time=time

    def calling(self):
        print("SMS rate and time",self.callRate,self.time)
    
    def sms(self):
        print("Calling Rate and time",self.smsRate,self.time)

p1=phone()
p1.set_sms(5,10)
p1.set_calling(4,14)
p1.calling()
p1.sms()

# 8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and
# Phone Class.    

class calculator:
    def __init__(self):
        self.num1=None
        self.num2=None
    def set_values(self,num1,num2):
        self.num1=num1
        self.num2=num2

class calculator2(calculator):
    def multiplication(self):
        return self.num1*self.num2

class phone:
    def __init__(self):
        self.ctime=None
        self.callRate=None
        self.smsRate=None

    def set_sms(self,smsRate,ctime):
        self.smsRate=smsRate
        self.ctime=ctime

    def set_calling(self,callRate,ctime):
        self.callRate=callRate
        self.ctime=ctime

    def calling(self):
        print("SMS rate and time",self.callRate,self.ctime)
    
    def sms(self):
        print("Calling Rate and time",self.smsRate,self.ctime)

class smartPhone(calculator2,phone):
    def __init__(self):
        pass
    def callRate(self):
        self.set_values(p1.callRate,p1.ctime)
        print("Total call cost is :",self.multiplication())

    def smsRate(self):
        self.set_values(p1.smsRate,p1.ctime)
        print("Total SMS cost is : ",self.multiplication())



p1=phone()
p1.set_sms(5,10)
p1.set_calling(4,14)
p1.calling()
p1.sms()

s1=smartPhone()
s1.callRate()
s1.smsRate()


# 9. Write a python script to create an application like Truecaller where names and
# numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
# number and 2nd to add a new entry).


class Truecaller:
    def __init__(self):
        self.name=["ram","shyam","hari"]
        self.number=[987,765,435]

    def get_name(self,number):      # to get name of person
        for i in self.number:
            if i==number:
                k=self.number.index(number)
                print("Name of person is : ", self.name[k] )

    def add_newentry(self,name,number):
        if number in self.number:     # to check if number already exist or not
            print("This number alread exist")
        else:
            self.number.append(number)
            self.name.append(name)
            print("New Updated Name list is : ", self.name)
            print("New Updated Number list is : ", self.number)

t1=Truecaller()
t1.get_name(435)  # to get name of person via number

t1.add_newentry("ramesh",671)   # to add new entery in database



# 10. Write a python script to add the new method in SmartPhone class which accepts
# Truecaller object as a parameter and call the fetch method of Truecaller.

class Truecaller:
    def __init__(self):
        self.name=["ram","shyam","hari"]
        self.number=[987,765,435]

    def get_name(self,number):      # to get name of person
        for i in self.number:
            if i==number:
                k=self.number.index(number)
                print("Name of person is : ", self.name[k] )

    def add_newentry(self,name,number):
        if number in self.number:     # to check if number already exist or not
            print("This number alread exist")
        else:
            self.number.append(number)
            self.name.append(name)
            print("New Updated Name list is : ", self.name)
            print("New Updated Number list is : ", self.number)


class calculator:
    def __init__(self):
        self.num1=None
        self.num2=None
    def set_values(self,num1,num2):
        self.num1=num1
        self.num2=num2

class calculator2(calculator):
    def multiplication(self):
        return self.num1*self.num2

class phone:
    def __init__(self):
        self.ctime=None
        self.callRate=None
        self.smsRate=None

    def set_sms(self,smsRate,ctime):
        self.smsRate=smsRate
        self.ctime=ctime

    def set_calling(self,callRate,ctime):
        self.callRate=callRate
        self.ctime=ctime

    def calling(self):
        print("SMS rate and time",self.callRate,self.ctime)
    
    def sms(self):
        print("Calling Rate and time",self.smsRate,self.ctime)

class smartPhone(calculator2,phone,Truecaller):
    def __init__(self):
        pass
    def callRate(self):
        self.set_values(p1.callRate,p1.ctime)
        print("Total call cost is :",self.multiplication())

    def smsRate(self):
        self.set_values(p1.smsRate,p1.ctime)
        print("Total SMS cost is : ",self.multiplication())

    def calling_treucallingFetch(self):
        t1.get_name(987)     # to get name by person number


p1=phone()
p1.set_sms(5,10)
p1.set_calling(4,14)
p1.calling()
p1.sms()

t1=Truecaller()
s1=smartPhone()
# s1.callRate()
# s1.smsRate()
s1.calling_treucallingFetch()










class student:
    school ="ineuron"  #class variable
    def __init__(self):
        self.marks=34
        self.name="ghj"
    def show(self):   # Instance methods
        return self.marks
    @classmethod
    def sch(cls):    #class methods
        return cls.school

    @staticmethod
    def add(x,y):   # static method
        return x+y

s1=student()

print(s1.name)
print(s1.show())
print(student.sch())

print(s1.add(8,9))
print(student.add(45,59))