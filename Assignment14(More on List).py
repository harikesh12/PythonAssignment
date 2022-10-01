from typing import List
#More on List

#1. Write a Python script to create a list of first N natural numbers.

print([x for x in range(1,int(input("enter the number: "))+1)])

#2. Write a Python script to create a list of first N odd natural numbers.

print([2*x+1 for x in range(int(input("Enter the number : ")))])

#3. Write a Python script to create a list of first N even natural numbers.

print([2*x+2 for x in range(int(input("Enter the number : ")))])

#4. Write a Python script to find the greatest number in a given list of numbers.

n=int(input("Enter the number of elements which you want to have : "))
number=[]
i=0
while i<n:
    number.append(int(input("Enter the numbers : ")))
    i+=1
print("Greatest number in list is", max(number))  # here directly I used max function to find greatest in list

#5. Write a Python script to find the smallest number in a given list of numbers.

n=int(input("Enter the number of elements which you want to have : "))
number=[]
i=0
while i<n:
    number.append(int(input("Enter the numbers : ")))
    i+=1
print("Smallest number in list is", min(number))

#6. Write a Python script to calculate the sum of elements in a given list of numbers.

number=eval(input("Enter the list: ")) # You can use above method as well to take number in list
print("Sum of list is", sum(number))

#7. Write a Python script to remove all non int values from a list.

values=eval(input("Enter the elements of list: "))
v=[]
for x in values:
    if type(x)==int:     #I just seleccted int type to append in list
        v.append(x)
print(v)

#8. Write a Python script to print distinct elements along with their frequencies of occurrence in the list.

values=eval(input("Enter the elements of list: "))  
v=[]
for x in values:
    if x not in v:       # here first I am checking if value is present in new list or not if not then adding that
        v.append(x)
        print("count of",x,"is",values.count(x))
print("distinct values list is ",v)

#9. Write a Python script to print indices of all occurrences of a given element in a given list.

values=eval(input("Enter the elements of list: "))
for x in values:
    print(x, "indices is ", values.index(x))    # this one is failing for duplicate values in list

#or

values=eval(input("Enter the elements of list: "))
i=0
for x in values:
    print(x ,"indices is", i)
    i+=1
    

#10. Write a python script to sort a list.

n=int(input("Enter the number of elements you want to have : "))
l=[]
i=0
while i<n:
    l.append(input("Enter values : "))
    i+=1
l.sort()   # sort function does not return anything it just modifies the existing list i.e. we can not directly print this list
print("Sorted list is", l)




