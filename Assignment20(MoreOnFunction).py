# 1. Write a python program to create a function that takes a list and returns a new list  with the original list's unique elements.

def uniqueList(a):
    print(list(set(a)))   # Set stores only unique number so first make it set and then make again this as list
    
uniqueList([4,5,6,4,5,2])

#or

def uniqueList(a):
    newlist = []
    for k in a:
        if k not in newlist:
            newlist.append(k)
    print(newlist)

uniqueList([4,5,6,4,5,2])



# 2. Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.

def prime(a):    
    for k in range(2,a+1):
        if a%k==0 and k!=a:
            print("This is Not a prime number")
            break
    else:
        print("This is a prime number")

prime(24)
prime(7)


# 3. Write a python program to create a function that prints the even numbers from a given list.

Sample_List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def toFindEven(a):
    even_list=[]
    for k in a:
        if k%2==0:
            even_list.append(k)
    print(even_list)

toFindEven(Sample_List)        


# 4. Write a python program to create a function that checks whether a passed string is palindrome or not.

def palindrom(a):
    i=(len(a)-1)
    if len(a)%2!=0:
        for k in range(int((len(a)+1)/2)):
            if a[k]==a[i]:
                i-=1
                continue
            else:
                print("This is not a Palindrom String")
                break
        else:
            print("This is Palindrom String")  

palindrom("radar")

# 5. Write a python program to create a function to find the Min of three numbers.

def minimum(a,b,c):
    print("Minimum of three values is ", min(a,b,c))

minimum(10,20,30)

# 6. Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.

def squarelist(a):
    print([i*i for i in range(1,a+1)])

squarelist(30)

# 7. Write a python program to access a function inside a function.

def firstFunction(a):
    def add(b):
        nonlocal a
        a+=1
        return a+b
    return add

funct = firstFunction(4)
print(funct(4))

# 8. Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.

def function(a):
    u=0
    l=0
    for k in a:
        if 90 >= ord(k) >=65:
            u+=1

        elif 122 >= ord(k) >=97:
            l+=1
    return u,l

a,b=function("HarKEsh")

print("Upper case are :",a , "and", "Lower case are :",b)



         
# 9. Write a python program to create a function to check whether a string is a pangram or not.
#Pangram is string which cotains every letter of English Alphabet

def isPangram(a):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for k in alphabet:
        if k not in a.lower():
            return False
    return True
a ="the quick brown fox jumps over the lazy dog"

if isPangram(a)==True:
    print("This is Pangram")
else:
    print("This is not Pangram")




# 10. Write a python program to create a function to check whether a string is an anagram or not.

#Anagram : if a string is completely present in b string then it is called anagram. eg:- abcd   bcda

def function(a,b):
    for k in a:
        if k in b:
            continue
        else:
            print("This is not anagram")
            break
    else:
        print("This is anangram")

function("abcd","bda")
