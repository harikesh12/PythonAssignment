#1. Write a python program to create a simple function which prints “MySirG” .

from calendar import c
from re import T
from symbol import argument


def mysirfunction() :
    print("MySirG")

mysirfunction()

# 2. Write a python program to create a function which expects two arguments and print them in the function body.

def function1(a,b):
    print(a,b)

function1("ram","shyam")


# 3. Write a python program to create a function which expects an unknown number of arguments.

def f1(*t):     #--> this is called assignning tuple to function which can handle unknown number of argument
    print(*t)

f1(3,4)
f1(4,5,6)
f1(2,1,3,4,5)


# 4. Write a python program to create a function which expects key args arguments.

def f1(a,b,c):
    print(a,b,c)

f1(b=2,c=1,a=3)    #--> this is called keyword argument


# 5. Write a python program to create a function which expects a list as an argument.

def f1(a):
    print(a)

f1([1,3,4,5,6]) 

#or

def f1(*t):
    print(*t)

f1([1,3,4,5,6])  # list can be given by giving argument as tuple to function


# 6. Write a python program to create a function that finds a maximum of four numbers.

def maximum(a,b,c,d):
    print("Maximum Function is ",max(a,b,c,d))

maximum(3,4,5,6)

# 7. Write a python program to sum all the numbers in a list.

def summation(*t):
    print("Sum is ",sum(*t))

summation([3,4,5,6])


# 8. Write a python program to multiply all the numbers in a list.

def multiply(m):
    c=1
    for a in m:
        c=c*a
    print(c)
multiply([2,4,5,6])



# 9. Write a python program to create a function to check whether a number falls in a given range.

def function(a):
    for k in range(1,20):
        if k==a:
            print(a, "is in range")
            break

function(12)


# 10. Write a python program to create a function to check whether a given number is even or odd.

def toCheck(a):
    if a%2==0:
        print("Number is Even")
    else:
        print("Number is Odd")

toCheck(15)