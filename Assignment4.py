""" 1. Write a python script to take your name as input from the user and then print it. """
a = input("Enter your name : ")
print(a)

# 2. Write a python script to take input import numbers from the user. Input must be a number.

a = int(input("enter the number : "))
print(a)

#3. Write a python script which takes two numbers from the user, then calculate their sum and display the result.

a = int(input("enter the 1st number : "))
b = int(input("enter the 2nd number : "))
c=a+b
print(c)

#4. Write a python script which takes the radius from the user and display area of a circle.

r = int(input("enter the radius of circle : "))
area = 22.7 * r * r
print("Area of circle is : ", area)

#5. Write a python script to calculate the square of a number. Number is entered by the user.

a = int(input("enter the number : "))
square = a * a
print("Square of number will be : ", square)

#6. Write a python script to calculate the area of Triangle. Number is entered by the user.

a = int(input("enter the base of Triangle : "))
b = int(input("enter the height of Triangle : "))
area = 0.5 * a * b
print("Area of Triangle will be : ", area)

#7-Write a python script to calculate average of three numbers, entered by the user

a = int(input("enter the 1st number : "))
b = int(input("enter the 2nd number : "))
c = int(input("enter the 3rd number : "))
d=(a+b+c)/3
print("Average of number is ",d)

#8. Write a python script to calculate simple interest


P = int(input("enter the value of principle : "))
N = int(input("enter the Number of years : "))
r = int(input("enter the value of Interest : "))
s= (P*N*r)/100
print("Interest amount is :",s)

#9. Write a python script to calculate the volume of a cuboid.

l = int(input("enter the length of cuboid : "))
h = int(input("enter the height of cuboid : "))
b = int(input("enter the breadth of cuboid : "))
v= l*h*b
print("volume of cuboid is:",v)

#10. Write a python script to calculate area of a rectangle

l = int(input("enter the length of rectangle : "))
h = int(input("enter the breadth of rectangle : "))
area = l*h
print("Area of rectangle is : ",area)
