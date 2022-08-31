from re import I


# 1. Write a python script to check whether a given number is positive or non-positive
x = int(input("Enter the number : "))
if x > 0 :
    print("Number is positive")
if x <= 0 :
    print("Number is non-positive")

    # or

print("positive") if int(input("enter value of x: ")) > 0 else print("Non positive")

# 2. Write a python script to check whether a given number is divisible by 5 or not

x = int(input("Enter the number : "))
if x%5 == 0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")

    #or

print("Number is divisible by 5 ") if int(input("enter the number: "))%5==0 else print("Number is not divisible by 5 ") 
 
 #or
 
print("Number is not divisible by 5" if int(input("enter the number:"))%5 else "Number is divisible by 5")

3. Write a python script to check whether a given number is even or odd
x = int(input("Enter the number : "))
if x%2 == 0:
    print("Number is even")
else:
    print("Number is odd")
#or

print( "even" if int(input("Enter the number : "))%2 == 0 else "odd" )

#4. Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.

x = int(input("Enter the 1st number : "))
y = int(input("Enter the 2nd number : "))

if x >= y:
    print("greatest number is", x)
else:
    print("greatest number is", y)

or 

a,b=int(input()),int(input())   
print(a if a>b else b)


# 5. Write a python script to print two given words in dictionary order

x = input("Enter the 1st word : ")
y = input("Enter the 2nd word : ")

if x < y:
    print(x,y)
else:
    print(y,x)

#or
x = input("Enter the 1st word : ")
y = input("Enter the 2nd word : ")

print((y,x) if x>y else (x,y)) 


# 6. Write a python script to check whether a given number is a three digit number or not.

x = input("Enter the number : ")

if len(x) == 3 :
    print("its a 3 digit number")
else:
    print("unknown digit number")

or

x = int(input("Enter the number : "))
if 99<x<1000:
    print("number is 3 digit")
else:
    print("unknown digit")


#7. Write a python script to check whether a given number is positive, negative or zero.

x=int(input("Enter the given number : "))
if x > 0:
    print("number is positive")
elif x<0:
    print("Number is negative")
else:
    print("Number is zero")

#8. Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots
ax2+bx+c=0

If b2 - 4ac = 0, then the equation has two equal roots.
If b2 - 4ac > 0, the equation has two real roots.
If b2 - 4ac < 0, the equation has two complex roots.

a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c :"))

d=b**2-4*a*c

if d == 0:
    print("Equation has 2 equal roots ")
elif d > 0:
    print("Equation has 2 different real roots")
elif d < 0:
    print("Equation has 2 different imaginary roots")


# 9. Write a python script to check whether a given year is a leap year or not.

a=int(input("enter the year name :"))
if a%4==0:
    if a%100 == 0:
        if a%400==0:
            print("its a leap year")
        else:
            print("Its a not a leap year")
    else:
        print("Its a leap year")

#or
x=int(input("enter the year name :"))

if x%400==0 or x%100!=0 and x%4==0:
    print("This is leap year")
else:
    print("it is not leap year")




# 10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.

a=int(input("enter the 1st number :"))
b=int(input("enter the 2nd number :"))
c=int(input("enter the 3rd number :"))

if a>=b>=c:
    print("Greatest number is ",a)
elif b>=c:
    print("Greatest number is ",b)
else:
    print("Greatest number is ",c)

# 11. Write a python script to take the month value in numeric format and display the
number of days in it.
a =  int(input("Enter the Month number : "))

if a == 1:
    print("Number of days in Jan is 31")
elif a == 2:
    print("Number of days in feb is 28")
elif a == 3:
    print("Number of days in March is 31")
elif a == 4:
    print("Number of days in April is 30")
elif a == 5:
    print("Number of days in May is 31")
elif a == 6:
    print("Number of days in Jun is 30")
elif a == 7:
    print("Number of days in Jul is 31")
elif a == 8:
    print("Number of days in Aug is 31")
elif a == 9:
    print("Number of days in Sep is 30")
elif a == 10:
    print("Number of days in oct is 31")
elif a == 11:
    print("Number of days in Nov is 30")
elif a == 12:
    print("Number of days in Dec is 31")
#or

a =  int(input("Enter the Month number : "))

if a in (1,3,5,7,8,10,12):
    print("This month has 31 days")
elif a in (4,6,9,11):
    print("This month has 30 days")
else:
    print("This month has 28 or 29 days ")



12. Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part


a =eval(input("Enter the complex number : "))
b= a.real
c=a.imag
if b > c:
    print("Real Part is greater")
else:
    print("Imaginary part is greater")

#or
a =eval(input("Enter the complex number : "))
print("real part is greater" if a.real > a.imag else "Imaginary part is greater")








s="1a2b3c4"



sum(int(e) for e in s)
    




l1 = [10,20,30]
i=-1
for a in l1:
    i+=1
    if a == 20:
        del l1[i]
        
print(l1)
