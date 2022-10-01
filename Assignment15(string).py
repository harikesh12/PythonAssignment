#1. Write a python script to create a String in 3 different possible ways
#1
a=str(input("enter the word : "))
print(a,type(a))

#2
a="ram"

#3
a=['ramesh', 'eats', 'mango']
b=' '.join(a)
print(b, type(b))

#2. Write a python script to Get the characters from the start to position 5 (Given String “iNeuron” using the slice syntax)

s="iNeuron"
print(s[:5])

#3. Write a python script to Get the characters from position 2 to position 5 (Given String “Hello Learners” using the slice syntax)

s="Hello Learners"
print(s[1:5])

#4. Write a python script to demonstrate String Concatenation adding space in between ( Given Strings a=”Learning” b=”Python” )

a="Learning"
b="Python"
c=a+' '+b
print(c)

#5-Write a python script to get the count of total number of characters in String a=“iNeuron”

a="iNeuron"
print(len(a))

#or

a="ineuron"
i=0
for e in a:
    i+=1
print(i)


#6. Write a python script to reverse a String. (“iNeuron”)

s="iNeuron"
print(s[::-1])

#or

"""s="iNeuron"
l=len(s)
re=[]
for e in s:
    if l>=0:
        re.insert(l-1,e)
        l-=1
        print(l)
        print(re)
print(''.join(re))"""  #does not work

#7. Write a python script to determine whether a string contains a specific substring.

s="harikesh"
print(s.__contains__("ha"))

#8. Write a python script to check if a string contains only numbers.

s="harikesh"
print(s.isdigit())

#9. Write a python script to check if a string contains only characters of the alphabet.

s="harikesh"
print(s.isalpha())

#10. Write a python script to convert an integer to a string.

s=5
k=s.__str__()
print(type(k))

