#1. Write a python script to print MySirG N times on the screen

n=int(input("enter the value of n: "))
i=1
while i<=n:
    print("MySirG",sep='\n')
    i+=1
print()

#or
n=int(input("enter the value of n: "))
while n:
    print("MySirG")
    n-=1

#2. Write a python script to print first N natural numbers

n=int(input("enter the value of n: "))
i=1
while i<=n:
    print(i,sep='\n')
    i+=1
print()

#3. Write a python script to print first N natural numbers in reverse order

n=int(input("enter the value of n: "))
i=0
while 0<=i<n:
    print(n-i)
    i+=1
print()

#4. Write a python script to print first N odd natural numbers

n=int(input("enter the value of n: "))
i=0
while i<n:
    print(2*i+1, sep='\n')
    i+=1
print()

#5. Write a python script to print first N odd natural numbers in reverse order
n=int(input("Enter the value of n: "))
i=n
while 0<i<=n:
    print(2*i-1)
    i-=1
print()

#6. Write a python script to print first N even natural numbers

n=int(input("Enter the value of n: "))
i=1
while i<=n:
    print(2*i)
    i+=1
print()

#7. Write a python script to print first N even natural numbers in reverse order

n=int(input("Enter the value of n: "))
i=n
while 0<i<=n:
    print(2*i)
    i-=1
print()

#8. Write a python script to print squares of first N natural numbers

n=int(input("Enter the value of n: "))
i=1
while i<=n:
    print(i*i)
    i+=1
print()


#9. Write a python script to print cubes of first N natural numbers

n=int(input("Enter the value of n: "))
i=1
while i<=n:
    print(i**3)
    i+=1
print()


#10. Write a python script to print first 10 multiples of N

n=int(input("Enter the value of n: "))
i=1
while i<=n:
    print(5*i)
    i+=1
print()