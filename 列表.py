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
print('-------------------------')


# 2. list.append
lang = ['C++','python']
lang.append('java')
print(lang)
print('-------------------------')

#3. delete Elem
del lang[1]
print(lang)
print('-------------------------')

# 4. count
lang.append('java')
print(lang)
print(lang.count('java'))
print(lang.count('C++'))
print(lang.count('python'))
print('-------------------------')

# 5.list.extend(seq) 
# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
lang.extend(['js','golang','hahaha'])
print(lang)
print('-------------------------')


# list.pop
# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
lang.pop()
print(lang)
print('-------------------------')


# list.reverse
# 反向列表中元素
print(lang)
lang.reverse()
print(lang)
print('-------------------------')

# list.remove(obj)
# 移除列表中的一个元素（参数是列表中元素），并且不返回任何值
lang.remove('golang')
print(lang)
print('-------------------------')


print('-------------------------')
print('-------------------------')

