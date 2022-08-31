"""1-Write a python script to convert a number into str type. """

a=9
b=str(a)
print(type(b))

from re import M


"""2-Write a python script to print Unicode of the character ‘m’ """

print(ord("m"))

"""3-Write a python script to print character representation of a given unicode 100. """

print(chr(100))

"""4-Write a python script to print any number and its binary equivalent """

print(bin(100))  --to print binary

print(int(0b1100100))   tp covnert to number


"""5-Write a python script to print any number and its octal equivalent."""

print(oct(100))   # to convert to octal
print(int(0o144))  # to convvert from octal to binary 

"""6-Write a python script to print any number and its hexadecimal equivalent."""

print(hex(100))      # convert to hexadecimal
print(int(0x64))     # convert to int  

"""7-Write a python script to store binary number 1100101 in a variable and print it in
decimal format. """

a=0b1100101

print(int(a))


"""8. Write a python script to store a hexadecimal number 2F in a variable and print it in
octal format."""

a=0x2F
b=int(a)
print(b)
print(oct(b))



"""9. Write a python script to store an octal number 125 in a variable and print it in binary
format."""

a=0o125

print(bin(a)) 



"""10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and
display the result in binary format."""

a=int(0o25)
b=int(0x39)
c=a+b
print(bin(c))