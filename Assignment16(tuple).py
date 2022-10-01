#1. Write a python script to store multiple items in a single variable ( Items are “Java” ,“Python”, “SQL”, “C” ) using tuple

from itertools import count
from numbers import Number
import numbers


item = ("Java","Python", "SQL", "C")
print(item)

# or
n = int(input("Enter how many items you want to enter : "))
count=1
a=[]
while count <= n:
    a.append(input("enter the word : "))
    count+=1
print(tuple(a))

#2-Write a python program to store only one item using tuple.

c=(10,)  # to store only one word comma has to be used after end of first element
print(c)

#3. Write a python program to reverse the tuple.

n=int(input("Enter the number of word you want : "))
count=1
a=[]
while count <= n:
    a.append(input("Enter the word :"))
    count+=1 
a.reverse()    # here it is going to alter list a and also it can not be assigned to any other variable keep
                     #this in mind.
print(tuple(a))

#or

n=int(input("Enter the number of word you want : "))
count=1
a=[]
while count <= n:
    a.append(input("Enter the word :"))
    count+=1 
b=reversed(a)   # here used reversed() and this can be assigned to some other variable
print(tuple(b))

#4. Write a python program to Swap two tuples in Python.

a=("a","b","c")
b=("d","e","f")

a,b=b,a

print("Now a is : ",a)
print("Now b is : ",b)

#5. Write a python program to check if all items in the tuple are the same.

a = ("a","b","a")
n=0
for i in a:
    if a[n]==i:
        continue
    else:
        print("All values of tuple is not equal")
        break 
else:
    print("All values of tuple is equal")    # this block will not execute if for loop ends with "break" keyword so when it is ending with contnue , else is running.

# 6. Write a python program to divide the tuple into four variables. tuple1=(100, 200, 300, 400)

tuple1=(100, 200, 300, 400)
a,b,c,d = tuple1

print("Unpacked values of tuple is",a,b,c,d)

#7-Write a python program to copy elements 4 and 5 from the following tuple into a new tuple. 

tuple1=(1,2,3,4,5,6)
tuple2=()
a=tuple1[3]
b=tuple1[4]
tuple2=a,b
print(tuple2)

#8. Write a python program to Sort a tuple of tuples by the second item. tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))

tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))  # 11 21 29 37 

print(tuple(sorted(list(tuple1),key= lambda x:x[1])))

#list=[]
#list2 = []
# for n in tuple1:
#     for i in n:
#         list.append(i)
# print(list)
# for i in list:
#     if i in tuple1:
#         list2.append(tuple1.index(i))
# print(list2)

#9. Write a python program to print the value 20 from given nested tuple
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
k=0
for n in tuple1:
    for i in n:
        if i==20:
            print(i)
            k+=1
print("Number of 20 is : ",k)

#or
tuple1[0]="python"
tuple1[1]=[10, 20, 30]
tuple1[2]=(2, 4, 16)

print(tuple1[1][1])


#10. Write a python program to change the first item (22) of a list within the following tuple to 222.
tuple1 = (11, [22, 33], 44, 55)

tuple1[1][0]=222
print(tuple1)
