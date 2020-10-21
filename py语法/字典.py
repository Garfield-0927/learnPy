# dict 相当于 java 中的map
# dict以键值对形式存储


# 1. 字典的创建
# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值(key=>value)对用冒号(:)分割
# 每个对之间用逗号(,)分割，整个字典包括在花括号({})中 
# dict = {key1 : value1, key2 : value2 }
# 注意：键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的。

print('--------------------------init dict--------------------------')
person={'name':'zjh', 'age':20, 'height':1.88}
print(person)
print('--------------------------init dict--------------------------')
print()
print()


print('--------------------------get Elem--------------------------')
person={'name':'zjh', 'age':20, 'height':1.88}
print(person['name'])
print('--------------------------get Elem--------------------------')
print()
print()


print('--------------------------revise Elem--------------------------')
person={'name':'zjh', 'age':20, 'height':1.88}
print(person)
# revise a value
person['name']='sc'
print(person)

# append a key-value
person['weight']=60
print(person)
print('--------------------------revise Elem--------------------------')
print()
print()


print('--------------------------delete dict/elem--------------------------')
person={'name':'zjh', 'age':20, 'height':1.88}
print(person)
# 通过 key 值，删除对应的元素
del person['height']
print(person)

# 删除字典中的所有元素
person.clear()
print(person)
print('--------------------------delete dict/elem--------------------------')
print()
print()


# 注意事项
# (1) dict （字典）是不允许一个键创建两次的
# 但是在创建 dict （字典）的时候如果出现了一个键值赋予了两次，
# 会以最后一次赋予的值为准
# 例子如下：
# dict1={'liangdianshui':'111111' ,'twowater':'222222' ,'两点水':'333333','twowater':'444444'}
# print(dict1)
# print(dict1['twowater'])

# (2) dict （字典）键必须不可变，可是键可以用数字，字符串或元组充当，但是就是不能使用列表
# (3) dict 内部存放的顺序和 key 放入的顺序是没有任何关系

# 和 list 比较，dict 有以下几个特点：
# 
# 查找和插入的速度极快，不会随着key的增加而变慢
# 
# 需要占用大量的内存，内存浪费多
# 
# 而list相反：
# 
# 查找和插入的时间随着元素的增加而增加
# 
# 占用空间小，浪费内存很少


# 字典的函数和方法
# len(dict)	            计算字典元素个数
# str(dict)	            输出字典可打印的字符串表示
# type(variable)	    返回输入的变量类型，如果变量是字典就返回字典类型
# dict.clear()	        删除字典内所有元素
# dict.copy()	        返回一个字典的浅复制
# dict.values()	        以列表返回字典中的所有值
# popitem()	            随机返回并删除字典中的一对键和值
# dict.items()	        以列表返回可遍历的(键, 值) 元组数组
