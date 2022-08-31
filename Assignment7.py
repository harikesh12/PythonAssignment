1-Write a python script to take the month value in numeric format and display the
number of days in it.
a =  int(input("Enter the Month number : "))

match a:
    case 1:
        print("Number of Days is january is 31")
    case 2:
        print("Number of Days is february is 28")
    case 3:
        print("Number of Days is March is 31")
    case 4:
        print("Number of Days in April is 30")
    case 5:
        print("Number of Days in May is 31")
    case 6:
        print("Number of Days in June is 30")
    case 7:
        print("Number of Days in July is 31")
    case 8:
        print("Number of Days in August is 31")
    case 9:
        print("Number of Days in September is 30")
    case 10:
        print("Number of Days in october is 31")
    case 11:
        print("Number of Days in November is 30")
    case 12:
        print("Number of Days in December is 31")
    case _:
        print("You have entered wrong Month Number")

or

month = int(input("Enter the month number : "))
match month:
    case month if month in (1,3,5,7,8,10,12):
        print("Month has 31 days")
    case month if month in (4,6,9,11):
        print("Month has 30 days")
    case 2:
        print("Month has 28 ir 29 days")
    case _:
        print("Invalid Month number")
print()

2. Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division


a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
print("Select the option : ", "1-Addition","2-Subtraction","3-Multiplication","4-Divison",sep='\n')
operation = int(input("Enter the option : "))

match operation:
    case 1:
        print("Additon is ", a+b)
    case 2:
        print("Subtraction is ", a-b)
    case 3:
        print("Multiplication is ", a*b)
    case 4:
        print("Divison is ", a/b)
    case _:
        print("You have selected wrong operation")

print("hello","world",sep='\n')

3. Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.


a = int(input("enter the 1st side of triangle : "))
b = int(input("enter the 2nd side of triangle : "))
c = int(input("enter the 3rd side of triangle : "))
print("press the option what you want to check","1-Isosceles","2-Right Angle Triangle","3-Equilateral Triangle","4-Exit",sep='\n')
d= int(input("Enter the option : "))
match d:
    case 1:
        if a==b or b==c or a==c:
            print("Its Isosceles Triangle")
        else:
            print("not an isosceles")
    case 2:
        if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
            print("Its rigth angle triangle")
        else:
            print("not a right angle triangle  ")
    case 3:
        if a==b==c:
            print("Its equilateral triangle")
        else:
            print("Not an equilateral")
    case 4:
        exit()
    case _:
        print("Wrong option chosen")
print()


Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen.

a = int(input("Enter age of person:"))
match a:
    case a:
        if a<=10:
            print("Kids")
        elif a<=20:
            print("Teen")
        elif a<=40:
            print("Young")
        elif a<60:
            print("Experienced")
        elif a>=60:
            print("Senior Citizen")
    or

a = int(input("Enter age of person:"))
match a:
    case a if a<10:
        print("Kids")
    case a if a<=20:
        print("Teen")
    case a if a<=40:
        print("Young")
    case a if a<=60:
        print("Experienced")
    case a if a>=60:
        print("Senior Citizen")
print()


Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.

a = int(input("Enter the number : "))
match a:
    case a if a%2==0:
        print("Saurabh Shukla")
    case a if a%2!=0 and a<0:
        print("Prateek Jain")
    case a if a%2!=0 and a>0:
        print("Aditya Choudhary")

6-Write a python program to check whether a given string is a multiword string or single
word string using match case statement

a = input("Enter the String : ")
a.strip()    #it removes spaces which occur in start of word or end of word
match a:
    case a if ' ' in a:
        print("Multi word")
    case a if ' ' not in a:
        print("singleword") 
print()

7. Write a python program to check whether a given number is positive, negative or
zero using match case statement 

x=int(input("enter the number :"))
match a:
    case a if x>0:
        print("Positive number")
    case a if x<0:
        print("Negative Number")
    case a if x==0:
        print("Zero Number")
print()

8=Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement

x,y=input("enter the first string"),input("Enter the 2nd string")
if x==y:
    a="iden"
if x<y:
    a=1
if x>y:
    a=2
match a:
    case "iden":
        print("both strings are identical")
    case 1:
        print("First string comes before 2nd")
    case 2:
        print("second string come before first one")

    or
x,y=input("enter the first string"),input("Enter the 2nd string")
match (x,y):
    case (x,y) if x==y:
        print("Both strings are identical")
    case (x,y) if x>y:
        print("{} comes after {}".format(x,y))
    case (x,y) if x<y:
        print("{} comes after {}".format(y,x))
print()

9-Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year

x= int(input("Enter the year : "))
if x%4==0 and x%100!=0:
    a=1
elif x%400==0:
    a=2
elif x%4==0 and x%100==0 and x%400!=0:
    a=3
else:
    a=4
match a:
    case 1:
        print("Non century leap year")
    case 2:
        print("Century leap year")
    case 3:
        print("Non century non leap year")
    case 4:
        print("Century non leap year")

10. Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday

a=input("enter your favourite colour : ")
match a:
    case a if "yellow" in a:
        print("Monday")
    case a if "Blue" in a:
        print("Tuesday")
    case a if "Orange" in a:
        print("wednesday")
    case a if "white" in a:
        print("Thursday")
    case a if "black" in a:
        print("friday")
    case a if "red" in a:
        print("saturday")
    case _:
        print("sunday")
print()

    





print("positive" if int(input("enter the number :" ))>0 else "Negative")




