# 1. Write a python script to create a ArithmeticError
a=1
b=0
c=a/b
print(c)


# 2. Write a python script to create a ValueError
a=int(input("enter the value :"))
print(a)

# 3. Write a python script to handle the ArithmeticError

a=1
b=0
try:
    c=a/b
    print(c)
except ZeroDivisionError:  # Arithmetic error 
    print("it can not be divided by Zero")
except Exception:
    print("Enter correct value")

# 4. Write a python script to handle a ValueError
try:
    a=int(input("enter the value :"))
    print(a)
except ValueError:
    print("You have entered wrong value ")

# 5. Write a python script to handle multiple Exception in one try

a=2
try:
    b=int(input("Enter the value of b : "))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("It can not be divided by Zero")
except ValueError:
    print("You have entered wrong value")
except Exception:
    print("Exception has been raised")

# 6. Write a python script to create a calculator with 4 basic operations, and handle a
# maximum number of exceptions.

try:
    a=int(input("Enter the value of a : "))
    b=int(input("Enter the value of b :"))
except ValueError:
    print("Please enter the Number")
else:
    print("Select Menu from below : \n 1- Addition \n 2- Subtraction \n 3- Multiplication \n 4- Division")
    try:                                            # to select right choice from given option
        operator=int(input("Enter option : "))
        if operator not in (1,2,3,4):
            raise Exception()                     
    except Exception:
        print("You have selected wrong choice , please select from 1,2,3,4")
    else:
        match operator:
            case 1:
                print("Addition is ",a+b)
            case 2:
                print("Subtraction is :",a-b)
            case 3:
                print("Multiplication is : ",a*b)
            case 4:
                try:                          # value of b can not be zero only for division so raised specifically for it.
                    if b==0:
                        raise ZeroDivisionError()
                    c=a/b
                    print("Division is : ",c)
                except ZeroDivisionError:
                    print("Value of b can not be Zero")
                
# 7. Write a python script to add a finally block for the above script

try:
    a=int(input("Enter the value of a : "))
    b=int(input("Enter the value of b :"))
except ValueError:
    print("Please enter the Number")
else:
    print("Addition is : ",a+b)
    print("Subtraction is : ",a-b)
    print("Multiplications is : ",a*b)
finally:
    try:
        if b==0:
            raise ZeroDivisionError()
        c=a/b
        print("divison is : ",c)
    except ZeroDivisionError:
        print("value of b can not be zero for Division")

# 8. Write a python script to implement try except and else block for division

# Ans Implemeted same in question 6.

# 9. Write a python script to raise a ValueError.

try:
    a=int(input("Enter the value  : "))
    if a==0:
        raise ValueError
        print(a)
except ValueError:
    print("value can not be Zero and string")

# 10. Write a python script to implemented a nested Try Except block

# Implemented in question 6

