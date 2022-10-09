# 1-Write a recursive python function to print first N natural numbers.

def printN(n):
    if n>0:
        printN(n-1)
        print(n)

printN(6)

# 2. Write a recursive python function to print first N natural numbers in reverse order

def reversePrint(n):
    if n>0:
        print(n)
        reversePrint(n-1)

reversePrint(5)

# 3. Write a recursive python function to print first N odd natural numbers


def oddNumber(n):
    if n>=1:
        oddNumber(n-1)
        print(2*n-1)

oddNumber(5)

# 4. Write a recursive python function to print first N odd natural numbers in reverse order

def reverseOdd(n):
    if n>=1:
        print(2*n-1)
        reverseOdd(n-1)

reverseOdd(5)

# 5. Write a recursive python function to print first N even natural numbers.

def evenNatural(n):
    if n>=1:
        evenNatural(n-1)
        print(2*n)

evenNatural(5)

# 6. Write a recursive python function to print first N even natural numbers in reverse order.

def reverseEven(n):
    if n>=1:
        print(2*n)
        reverseEven(n-1)

reverseEven(5)

# 7. Write a recursive python function to print squares of first N natural numbers

def square(n):
    if n>0:
        square(n-1)
        print(n*n)

square(5)

# 8. Write a recursive python function to print cubes of first N natural numbers

def square(n):
    if n>0:
        square(n-1)
        print(n**3)

square(5)

# 9. Write a recursive python function to print first N multiples of a given number.

def multiple(n):
    if n>0:
        multiple(n-1)
        print(k*n)

k=int(input("Enter the number : "))
multiple(6)

# 10. Write a recursive python function to print a number in reverse order.

def reversePrint(n):
    if n>0:
        print(n,end=' ')
        reversePrint(n-1)

reversePrint(6)

