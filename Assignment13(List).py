from tokenize import Number

#1. Write a python script to store multiple items in a single variable ( Items are “Java” ,“Python”, “SQL”, “C” ) using list

n = int(input("Enter the number of words yow want to have : "))
a=[]
counter= 1
while counter<=n:
    a.append(input("enter the word : "))
    counter+=1
print(a)

2. Write a python script to get the data type of a list.

a=["ram","shyam"]
print(type(a))

#3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])

mylist = ["Java", "C", "Python"]

for i in mylist:
    if mylist.index(i)==len(mylist)-1 :   #here first we will get index of element and then will compare with last index
        print(i)                               

#or  we can use pop function but drawback is it will remove last value from list

#4-Write a python script to Change the values "SQL" and "Reactnative" with the values
"NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative",
"Javascript", "Python"]

thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
a=thislist.index("SQL")
thislist[a]="NoSQL"

b=thislist.index("Reactnative")
thislist[b]="Flutter"

print(thislist)

#5. Write a python script to add an item to the end of the list (item “Python”. (mylist =
["Java", "SQL", "C", "Reactnative"]

mylist =["Java", "SQL", "C", "Reactnative"]
mylist.append("python")
print(mylist)

#6. Write a python program to append elements from another list to the current list.(
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
thirdlist=[]
thirdlist=firstlist+secondlist
print(thirdlist)

#7. Write a python program to Print all items by referring to their index number (thislist =
["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

thislist =["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
i=0
while i<len(thislist):
    print(thislist[i])
    i+=1

#8-Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL",
"C", "Reactjs", "Javascript", "Python"]

thislist = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]

a=sorted(thislist)
print(a)

#9. Write a Python script to create a list of city names taken from the user.

a=int(input("specify number of cities you want to have : "))
city=[]
i=0
while i<a:
    city.append(input("Enter cities name : "))
    i+=1
print(city)

#10. Write a Python script to create a list, where each element of the list is a digit of a given number.

a=int(input("specify numbers you want to enter : "))
number=[]
i=0
while i<a:
    number.append(input("Enter numbers : "))
    i+=1
print(number)
   

