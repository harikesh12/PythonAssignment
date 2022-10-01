tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))  # 11 21 29 37 

print(tuple(sorted(list(tuple1),key= lambda x:x[1])))