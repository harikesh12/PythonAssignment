n=int(input("Enter the value of n : "))
s=' '
while n>0:
    k=n%8
    s+=str(k)
    n=n//8
print(int(s[::-1]))