# python 提供整数 浮点数 复数 3种数字类型

# 整数
# 十进制
# 二进制 0b101，0B101
# 八进制 0o711，0O711
# 十六进制 0xABC，0XABC
print(pow(2,5))
print("--------------------------------------------")

# 浮点数
import sys
print(sys.float_info)
print("--------------------------------------------")


# 复数
# python中，复数的虚数部分通过后缀J或者j来表示
z = 12+3j
print(z,z.real,z.imag)
print("--------------------------------------------")


# 数字类型的操作
# +,-,*,/,//,%,**
# //表示x与y的商向下取整
# %整除
# **表示x的y次幂
a = 10
b = 3
print(a+b)
print(a//b)
print(a/b)
print(a%b)
print(a**b)
print("--------------------------------------------")


# python的内置函数
# abs(x)        取绝对值
# divmod(x,y)   (x//y,x%y) 输出为二元组形式
# pow(x,y[,z])  x**y%z， z is optional
# round(x[,ndigits])    对x四舍五入 保留ndigits位小数，ndigits is optional
# max
# min

x = 10
y = 3
z = 5
print("a=",x,"b=",y,"c=",z)
print(divmod(x,y))
print(pow(x,y),pow(x,y,z))
print(round(x,5))
print("--------------------------------------------")


# math 模块的引用

