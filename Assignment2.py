"""Write a python script to add comments and print “Learning Python” on screen."""

print("Learning Python")  # I am learning python

"""2-Write a python script to add multi line comments and print values of four variables,
each in a new line. Variable contains any values."""

a=1
b=2
c=3
d=4

print(a)
print(b)
print(c)
print(d)

"""3-Write a python script to print types of variables. Create 5 variables each of them
containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc) """

a=35
b=True
c="MySirG"
d=5.46
e=3+4j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


"""4-Write a python script to print the id of two variables containing the same integer
values. """

a=4
b=4

print(id(a))
print(id(b))

"""5-Create four variables in a Python script and assign values of different data types to
them. Write a Python script to print value, its type and id of each variable """

a=35
b=True
c="MySirG"
d=5.46
e=3+4j

print(type(a),id(a))
print(type(b),id(b))
print(type(c),id(c))
print(type(d),id(d))
print(type(e),id(e))

from ast import keyword


""" 6-Write a python script to print all the keywords
7-On Python shell use help() function and display the list of keywords """

help('keywords')

"""8-Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some
value to it. Write a python script to import A1 module in A0 and print value of the
variable created in A0.py """

A0.py   Assignment1
A1.py   Assignment2

import Assignment1
print(Assignment1.s)


"""  9-Name the keywords, used as data in the Python script. """

False
True
None 

"""Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM)  """

a="13-8-2022"
b="9:00 PM"

print(a,b) 

from datetime import datetime

dt = datetime.today()
print(dt)

d1 = dt.strftime("%d-%m-%Y and %I:%M %p")    # when we need 12 hour time we use I 
print(d1)

d2 = dt.strftime("%H:%M:%S")
print(d2)

d3 = dt.strftime("%B %d %Y")
print(d3)

d4 = dt.strftime("%d/%b/%Y")
print(d4)

d5 = dt.strftime("%d/%m/%Y")
print(d5)








