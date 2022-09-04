1. Write a python script to calculate sum of first N natural numbers

n=int(input("Enter the value of n : "))
sum=0
for i in range(n+1):
    sum+=i
print("Sum is : ", sum)

2. Write a python script to calculate sum of squares of first N natural numbers

n=int(input("Enter the value of n : "))
sum=0
for i in range(n+1):
    sum+=i*i
print("Sum is : ", sum)

3. Write a python script to calculate sum of cubes of first N natural numbers

n=int(input("Enter the value of n : "))
sum=0
for i in range(n+1):
    sum+=i**3
print("Sum is : ", sum)

4. Write a python script to calculate sum of first N odd natural 

n=int(input("Enter the value of n : "))
sum=0
for i in range(n):
    sum+=(2*i+1)
print("Sum is : ", sum)

5. Write a python script to calculate sum of first N even natural numbers

n=int(input("Enter the value of n : "))
sum=0
for i in range(n):
    sum+=(2*i+2)
print("Sum is : ", sum)

6. Write a python script to calculate factorial of a given number

n=int(input("Enter the value of n : "))
fact=1
for i in range(n,0,-1):
    fact*=i
print(fact)

7. Write a python script to count digits in a given number


n=int(input("Enter the value of n : "))
i=0
while n>9:
    if n//10>0:
        i+=1
        n=int(n/10)
print(i+1)

8. Write a python script to calculate sum of digits of a given number

n=int(input("Enter the value of n : "))
sum =0
if n>9:
 while n>9:
    s=n%10
    sum+=s
    n=n//10
 print(int(sum)+n)
else:
    print("its one digit number")

9. Write a python script to print binary equivalent of a given decimal number. (do not
use bin() method)

n=int(input("Enter the value of n : "))
s=' '
while n>0:
    k=n%2
    s=s+str(k)
    n=n//2
print('b'+s[::-1])


10. Write a python script to print the octal equivalent of a given decimal number. (do not
use oct() method)

n=int(input("Enter the value of n : "))
s=' '
while n>0:
    k=n%8
    s+=str(k)
    n=n//8
print(int(s[::-1]))






