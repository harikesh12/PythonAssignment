from ast import NotIn
from operator import contains
from typing import ChainMap
from unicodedata import name


#1. Write a python program to create and print a dictionary which stores your information. (name, age, gender .....)

d={'name':"ramesh",'age':"55",'gender':"male"}
print(d)

#or

d={}
name,age,gender=input("Enter first key name : "),input("Enter second key name : "),input("Enter third key name : ")
nam=input("enter the name : ")
ag=input("enter the age :")
gende = input("Enter the gender : ")
d[name]=nam
d[age]=ag
d[gender]=gende
print(d)

#2. Write a python program to access the items of a dictionary by referring to its key name.

d={'nam':"ramesh",'age':"55",'gender':"male"}
print(d['nam'])
print(d['age'])
print(d['gender'])
print(d.keys())


#3. Write a python program to get a list of the values from a dictionary.

d={'nam':"ramesh",'age':"55",'gender':"male"}
print(d.values())

#4. Write a python program to change the value of a specific item by referring to its key name.

d={'nam':"ramesh",'age':"55",'gender':"male"}
d['nam']='ram'
print(d)

#5. Write a python program to print all key names in the dictionary, one by one.

d={'nam':"ramesh",'age':"55",'gender':"male"}
print(d.keys())

#6. Write a python program to create a dictionary that contains three dictionaries. (nested)

d={'Dict1': {'age': 21, 'name': 'Bob'}, 'Dict2': {'age': 25, 'name': 'Cara'}}

d={}
d['dict1']={}
print("Adding values to Dict1 : ")
d['dict1']['name']='Bob'
d['dict1']['age']=21
print(d['dict1'])

print("Adding values to Dict1 : ")
d['dict2']={}
d['dict2']['name']='Ram'
d['dict2']['age']=24

print('Whole dictionary is : ')
print(d)

#or   Below is dynamic one
n=int(input("how many dictionaries you want to add : "))
d={}
for i in range(1,n+1):
    key=input("Enter the key name : ")
    d[key]={}
    d[key]['name']=input('enter the name : ')
    d[key]['age']=input('enter the age : ')
print(d)

#7. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={}

for d in (dict1,dict2):
    dict3.update(d)
print(dict3)

#8. Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.


list1=["name","age"]
list2=["hari","39"]
d={}
for k in list1:
    for n in list2:
        d[k]=n
        list2.remove(n)    # it will remove value n which is coming from list2 so in next iteration it wont be present
        break
print(d)

#or

list1=["name","age"]
list2=["hari","39"]
dict={list1[i]:list2[i] for i in range(len(list1))}  # dict comprehension and this can be used for precised coding 
print(dict)

#or
list1=["name","age"]
list2=["hari","39"]
print(dict(zip(list1,list2)))



#9. Write a python program to merge two python dictionaries into one dictionary.

dict1={"name":"hari","age":25}
dict2={"name":"ramesh","age":39}
#print({**dict1,**dict2})  #unpacking operator #or   
#print(dict(dict1,**dict2))  #unpacking second operator #or
dict3=dict1 | dict2
print(dict3)

#10. Write a python program to get the key of lowest value from the dictionary.
sample_dict = {'C': 92,'Java': 66,'Python': 85}

# m=min(sample_dict.values())

print({i for i in sample_dict if sample_dict[i]==min(sample_dict.values())})

#or
m=min(sample_dict.values())
for key,value in sample_dict.items():
    if value==m:
        print(key)

#or
l1=list(sample_dict.keys())
l2=list(sample_dict.values())
m=min(sample_dict.values())
position=l2.index(m)
print(l1[position])






