# init a list
# 1
lst = ['hello','world',98]
print(lst)
for i in lst :
    print(i)

print('-------------------------')

# 2
lst2 = list(['hello','world','pyhton'])
print(lst2)
for i in lst2 :
    print(i+' ',end="")
print()

print('-------------------------')
# features:
# 1. ordered
# 2. one index mirrors one value
# 3. store different types of data
# 4. 动态分配内存


# list operation

# 1. lst.index(str[,a,b])
lst = ['hello','world',97,'hello']
index = lst.index('hello') 
print(index)
# index = lst.index('hahhaha')
# print(index)
index = lst.index('hello',1,4)
print(index)

