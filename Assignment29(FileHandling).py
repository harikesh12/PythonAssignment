# 1. Write a Python script to print the following status of a file:
# a. Whether a file is read only
# b. Whether a file is closed or not
# c. Which file opening mode is used
# d. Name of the file

f=open('tempCodeRunnerFile.py','r')
print("Mode of file is : ",f.mode)   # tp check file opening mode
f.close()
print(f.closed)    # to check if file is closed or not.
print(f.name)    # to get name of file


# 2. Write a Python script to create a new file ‘myfile.txt’ and store user entered text.


f=open('myfile.txt','w')   # created new file with w mode
f.write(input("Enter the content of file : "))   # user entered data
f.close()
f=open('myfile.txt','r')    # opening new file with read mode
print(f.read())

# 3. Write a Python script to read the above created file ‘myfile.txt’ and display content on the console.

f=open('myfile.txt','w')   # created new file with w mode
f.write(input("Enter the content of file : "))   # user entered data
f=open('myfile.txt','r') 
print(f.read())   # reading this file
f.close()

# 4. Write a Python script to store a list of city names in a file ‘cities.txt’

f=open('cities.txt','w')   # created new file with w mode
f.write(input("Enter the cities Name : "))
f=open('cities.txt','r')
print(f.read())

# 5. Write a Python script to store a list of city names in a file ‘cities.txt’

f=open('cities.txt','a')   # created new file with w mode
f.write(input("Enter the cities Name : "))
f=open('cities.txt','r')
print(f.read())

# 6. Write a Python script to search whether a particular city is there in the file ‘cities.txt’ or not

with open('cities.txt','w') as f:
    for i in range(5):
        f.write(input("Enter the cities Name :"))
def search(filename,word):
    try:
        f=open(filename,'r')
        line_count=0
        for line in f.readlines():
            line_count+=1
            line_words=line.split(' ')
            word_number=0
            for lword in line_words:
                word_number+=1
                if word.lower()==lword.lower():
                    print("Line Number:",line_count,"Word count:", word_number)
                    continue
                if lword.lower().__contains__(word):
                    print("Contains : Line Number:",line_count,"Word count:", word_number)
        else:
            print("No word Found")
        f.close()
    except FileNotFoundError:
        print("File Not found")

search('cities.txt','mumbai')


# 7. Write a Python script to count the number of Python keywords occurring in a python source file.

f=open('Assignment29(FileHandling).py','r')
count=0
for line in f.readlines():
    line_words=line.split(' ')
    for word in line_words:
        if word.lower()=='Python'.lower():
            count+=1
print("Python word count is : ", count)

# 8. Write a Python script to create a copy of a file.

with open('cities.txt','r') as file1, open('myfile.txt','w') as file2:
    for line in file1:
        file2.writelines(line)   # to write all line

f=open('myfile.txt','r')
print(f.read())
f.close()

# 9. Write a Python script to store book data in a file. Book data is in the form of a
# dictionary in which book name is the key and price is its value. Use pickle to store
# data into a file (say bookfile)

import pickle
import os
book_data={'python':125,'java':225,"c":345,"c++":445}
f=open('bookfile.py','wb')
pickle.dump(book_data,f)
f.close()

f=open('bookfile.txt','r')
print(f.read())

# 10. Write a Python script to extract book data from a bookfile using pickle. Also print
# extracted book data.

import pickle
f=open('bookfile.py','rb')
s=pickle.load(f)
for key in s:
    print(s[key])
f.close()