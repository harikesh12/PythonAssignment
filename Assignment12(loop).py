from calendar import c
from math import lcm
from signal import pthread_kill
from tkinter import Y


1. Write a python script to reverse a number.
 
n=int(input("Enter the number : "))
s=' '
while n>0:
    k=n%10
    s+=str(k)
    n=int(n/10)
print("Reverse number is ", int(s))

2. Write a python script to check whether a given number is Prime or not

n=int(input("Enter the number : "))
i=2
while i<=n:
    if n%i!=0:
        if n!=i:
            i+=1
    elif n==i:
        print("This is prime number")
        break
    elif n!=i:
        print("This is not prime number")
        break

3. Write a python script to print all Prime numbers under 100

for k in range(1,101):
    for i in range(2,k+1):
        if k%i!=0 and k!=i:
            continue
        elif k==i:
            print(k)
        else:
            break

4. Write a python script to print all Prime numbers between two given numbers (both
values inclusive)

a = int(input("Enter the value of a : "))  
b = int(input("Enter the value of b : "))  

for k in range(a,b+1):
    for i in range(2,k+1):
        if k%i!=0 and k!=i:
            continue
        elif k==i:
            print(k)
            break
        elif k!=i:
            break

5. Write a python script to find next prime number of a given number

a = int(input("Enter the number : "))
a+=1
b=1
while a>=1 and b==1:
    for k in range(2,a+1):
        if a%k!=0:
            continue
        elif a==k:
            print(a)
            b+=1
            break
        else:
            a+=1
            break

6. Write a python script to print first N prime numbers (#doubt#)

n = int(input("Enter the value of n : "))
#a=2
for i in range(2,10000):    # instead of 10000 there should be some variable which can increase itself
    for k in range(2,i+1):
        if i%k!=0 and n>=1:
            continue
        elif k==i and n>=1:
            print(i)
            #a+=1
            n-=1
            break
        else :
            #a+=1
            break


7-Write a python script to check whether a given pair of numbers are co-Prime
numbers or not.

a = int(input(" Enter the first number : "))
b = int(input(" Enter the Second number : "))


for i in range(1, a+1):
    if a%i==0 and b%i==0:
        hcf=i
if hcf == 1:
    print("Both pair are co prime number")
else:
    print("Both pair are not co prime number")



8. Write a python script to print first N terms of a Fibonacci series

n = int(input("Enter the value of n : "))

a,b=0,1
i=1
print("0")
while i<n:
    a,b=b,a+b
    i+=1
    print(a)

9-Write a python script to calculate LCM of two numbers


x = int(input(" Enter the first number : "))
y = int(input(" Enter the Second number : "))

if x>y:
    a=x
else :
    a=y

while True:
    if a%x==0 and a%y==0:
        print("lcm is ", a)
        break
    a+=1

10. Write a python script to calculate HCF of two numbers

x = int(input(" Enter the first number : "))
y = int(input(" Enter the Second number : "))

for i in range(1,x+1):
    if x%i==0 and y%i==0:
        hcf=i
print(hcf)