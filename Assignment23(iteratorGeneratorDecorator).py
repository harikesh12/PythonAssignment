#1. Use iter and next method to access all the elements of a given set using while loop
from ast import IsNot
from asyncio.windows_events import NULL
from base64 import b16decode
from itertools import islice
from logging import exception
from operator import itemgetter
from queue import Empty
from re import A, I


s={'ram','shyam',5,'hari'}

it=iter(s)
while True:
    try:
        print(next(it))
    except:
        print("exception occured and handled")
        break

# 2. Create a generator to produce first n odd natural numbers

def oddNatural(n):
    yield 2*n-1

for k in range(1,int(input("enter the value of n: "))):
    it=iter(oddNatural(k))
    print(next(it))

#3. Create a generator to produce first n even natural numbers

def evenNatural(n):
    yield 2*n

for k in range(1,int(input("Enter the value of n : "))+1):
    it=iter(evenNatural(k))
    print(next(it)) 

#4. Create a generator to produce squares of first N natural numbers

def square(n):
    yield n*n

for k in range(int(input("Enter the value of n : "))):
    it=iter(square(k))
    print(next(it))

#5. Create a generator to produce first n terms of Fibonacci series
0 1 1 2 3 5 8

def fibonacci(n):
   a,b=0,1
   for _ in range(n):
    yield a
    a,b=b,a+b

n=int(input("Enter the value of n : "))
print(list(fibonacci(n)))

# 6. Create a generator to produce first n prime numbers

def primeNumber(n):
    k=2
    l=0
    while l<n:
        for j in range(2,k+1):
            if k%j==0:
                if k!=j:
                    k+=1
                    continue
                elif k==j:
                    yield k
                    k+=1
                    l+=1

print(list(primeNumber(5)))

# 7. Create an endless iterator using generator method to produce terms of Fibonacci series

from itertools import islice

def endlessFibonacci():
    a,b=0,1
    while True:
        yield a 
        a,b=b,a+b 

it=islice(endlessFibonacci(),10,15)
print(list(it))

# from itertools import islice
# for i in islice(range(20),5,10,2):
#     print(i)


# 8. Create an endless iterator using generator method to produce Prime numbers

from itertools import islice
def primeNumber():
    k=2
    l=0
    while True:
        for j in range(2,k+1):
            if k%j==0:
                if k!=j:
                    k+=1
                    continue
                elif k==j:
                    yield k
                    k+=1
                

prime=islice(primeNumber(),25,35)
print(list(prime))

# 9-Define a function which takes lengths of three sides of a triangle as arguments and
# display the perimeter or triangle. Define and apply a decorator which checks for the
# validity of the triangle on the basis of lengths of the side. This makes the perimeter to
# be displayed when the triangle can exist with the given lengths of the sides.

def decor_triangle(triangle_func):
    def triangle1(l,b,h):
        if l>2*b>2*h:     # just make this hypothetical condition that if this is going to be true then thats cant be triangle.
            pass
        else:
            triangle_func(l,b,h)
    return triangle1

@decor_triangle
def triangle(l,b,h):
    print(l+b+h)

triangle(45,21,10)

# 10. Define a function which calculates HCF of two numbers. Define and apply and decorator to check whether two given numbers are co-prime or not.

def decor_hcf(hcf1_func):
    def coprime(a,b):
            if hcf1_func(a,b) == 1:
                print("This is co prime number")
            else:
                print("This is not co prime number")
    return coprime

@decor_hcf
def hcf1(a,b):
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            pass
    print(i)
    return i

hcf1(3,6) 


