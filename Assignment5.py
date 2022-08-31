#1- Write a python script to remove the last digit from multiprocessing.connection import answer_challenge
from a given number. (for example, if
user enters 2534 then your output should be 253)
a= int(input("Enter the number :"))
b=a//10    # Floor division
print("New number is ",b)

#2. Write a python script to get the last digit from a given number. (for example, if user
enters 2089 then your output should be 9)

a= int(input("Enter the number :"))
b=a%10    # modulus
print("New number is ",b)

#3. Write a python script to swap data of two variables
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c=a
a=b
b=c
print("new value of a and b is ", a,b,sep=" ")

or
a,b = b,a    # another method

#4 - Write a python script to find x power y, where values of x and y are given by user

x = int(input("Enter value of x : "))
y = int(input("Enter value of y : "))

c=x**y

print("x power y is ", c)

#5-Write a python script which takes a three digit number from the user and displays
only its first digit.

x = int(input("Enter three digit number x : "))
y=x/100  # or directly use floor division //
print("1st digit of this number is ",int(y))


#6-Write a python script which takes a three digit number from the user and displays
only its middle digit.

x = int(input("Enter three digit number x : "))
a=x//10
b=a%10
print("Middle digit of number is ", b)

#7. Write a python script which takes a three digit number from the user and displays
#only its last digit.

x = int(input("Enter three digit number x : "))
a=x%10
print("last digit of number is ", a)

#8-Write a python script to use IN operator to display the data present in the list

a=[1,2,3,4]
b = 2 in a
print(b)

#9-Write a python script to use NOT IN operator to display the data not present in list

a=[2,4,6,5]
c = 4 not in a
print(c)

#10. Write a python script to use IS operator to display if both variables are the same
#object or not?

a=5
b=5
c=a is b
d=a is not b
print(c,d)


