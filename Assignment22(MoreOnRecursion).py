from math import factorial
from symbol import factor


# 1. Write a recursive python function to calculate sum of first N natural numbers

def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)

print(sum(5))

# 2. Write a recursive python function to calculate sum of first N odd natural numbers

def sumOdd(n):
    if n==1:
        return 1
    else:
        return (2*n-1)+sumOdd(n-1)

print(sumOdd(3))

# 3. Write a recursive python function to calculate sum of first N even natural numbers

def sumEven(n):
    if n==1:
        return 1
    else:
        return (2*n)+sumEven(n-1)

print(sumEven(3))

# 4. Write a recursive python function to calculate sum of squares of first N natural numbers

def sumSquare(n):
    if n==1:
        return 1
    else:
        return (n**2)+sumSquare(n-1)

print(sumSquare(3))

# 5. Write a recursive python function to calculate sum of cubes of first N natural numbers

def sumCube(n):
    if n==1:
        return 1
    else:
        return (n**3)+sumCube(n-1)

print(sumCube(3))

# 6. Write a recursive python function to calculate the factorial of a number.

def Factorial(n):
    if n==0:
        return 1
    else:
        return n*Factorial(n-1)

print(Factorial(5))

# 7. Write a recursive python function to calculate sum of the digits of a given number

def sumDigit(n):
    if n==0:
        return 0
    else:
        return n%10 + sumDigit(int(n/10))

print(sumDigit(123))

# 8. Write a recursive python function to print binary of a given decimal number.

def decimalToBinary(n):
    if n==0:
        return 0
    else:
        decimalToBinary(n//2)
        print(n%2 , end='')
        
decimalToBinary(25)

# 9. Write a recursive python function to print octal of a given decimal number

def decimalToOctal(n):
    if n==0:
        return 0
    else:
        decimalToOctal(n//8)
        print(n%8 , end='')
        
decimalToOctal(25)

# 10. Write a recursive python function to find the Nth term of the Fibonacci series.

def Fibonacci(n):
    if n<0:
        print("Incorrect Input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(7))  # 0 1 1 2 3 5 8 13 21


