#1、什么是元组 （tuple）
#
#tuple 和 List 非常类似，但是 tuple 一旦初始化就不能修改。 也就是说元组（tuple）是不可变的，那么不可变是指什么意思呢？
#
#元组（tuple） 不可变是指当你创建了 tuple 时候，它就不能改变了，也就是说它也没有 append()，insert() 这样的方法，但它也有获取某个索引值的方法，但是不能赋值。
#
#那么为什么要有 tuple 呢？
#
#那是因为 tuple 是不可变的，所以代码更安全。
#
#所以建议能用 tuple 代替 list 就尽量用 tuple 。

# init a tuple
print('---------------init---------------')
tpl1=('111','222','333')
tpl2='111','222','333'
print(tpl1)
print(tpl2)
# 元组中只包含一个元素时，需要在元素后面添加逗号
tpl3=(123)
tpl4=(123,)
# 如果不加逗号，创建出来的就不是 元组（tuple），而是指 123 这个数了。
print(tpl3)
print(tpl4)
print('---------------init---------------')




# 访问元组中的数据
print('---------------visit elem---------------')
tuple1=('两点水','twowter','liangdianshui',123,456)
tuple2='两点水','twowter','liangdianshui',123,456
print(tuple1[1])
print(tuple2[0])
print('---------------visit elem---------------')


# 修改元组
# 可能看到这个小标题有人会疑问，上面不是花了一大段来说 tuple 是不可变的吗？
# 这里怎么又来修改 tuple （元组） 了。
# 那是因为元组中的元素值是不允许修改的，
# 但我们可以对元组进行连接组合，还有通过修改其他列表的值从而影响 tuple 的值。
print('---------------revise elem---------------')
list1=[123,456]
tuple1=('两点水','twowater','liangdianshui',list1)
print(tuple1)
list1[0]=789
list1[1]=100
print(tuple1)
print('---------------revise elem---------------')


# tuple 元组中的元素值是不允许删除的，但我们可以使用 del 语句来删除整个元组
print('---------------delete tuple---------------')
tuple1=('两点水','twowter','liangdianshui',[123,456])
print(tuple1)
del tuple1
print(tuple1)
print('---------------delete tuple---------------')

