# 1. Write a python program to store all the programming languages known to you using Set.

from ast import Delete
from os import remove


n=int(input("how many programming language do you want to store ? "))
count=1
s=set()
while count <=n:
    s.add(input("Enter the Name : "))
    count+=1
print(s)

#2. Write a python program to store your own information {name, age, gender, so on..}

s=set()
s.add(input("enter you name : "))
s.add(input("Enter your age : "))
s.add(input("Enter your gender : "))
print("set value is ", s)

#3. Write a python script to get the data type of a Set.

s={"Ram",25,5.6,5+6j}
print(type(s))

#4. Write a Python script to find if “Python” is present in the set this

set = {"Java","Python", "Django"}

for n in set:
    if n=="Python":
        print("python is present")
        break
else:
    print("Python is not present")

#5. Write a python program to add items from another set to the current set. this
set ={"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
s=set.union(secondset)
print(s)

#6. Write a python program to add elements of list to a set
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
thisset.update(mylist)
print(thisset)

#7. Write a python program to remove last item of the given set
thisset = {"Python", "Django", "JavaScript", "SQL"}
thisset.discard("SQL")
print(thisset)

#8. Write a python program to delete the set completely.

thisset = {"Python", "Django", "JavaScript", "SQL"}
thisset.clear()   # to clear set completly
print(thisset)  

#9. Write a python program to loop through the set and print values
thisset = {"Python", "Django", "JavaScript", "SQL"}

for n in thisset:
    print(n)

#10. Write a python program to find the maximum and minimum value in a set.

s={23,45,56,12,78}
print("Max is : ",max(s))
print("Min is :", min(s))


