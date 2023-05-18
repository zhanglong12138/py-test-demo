#输出内容 数据类型
print('中文内容');

#
# Python是一种强类型语言，支持多种数据类型，常用的数据类型包括：
# 数字类型：包括整数(int)、浮点数(float)、复数(complex)等。
# 字符串类型：由一系列字符组成的序列，可以使用单引号、双引号或三引号来表示。
# 列表(list)类型：由一系列元素组成的可变序列，用方括号[]来表示。
# 元组(tuple)类型：由一系列元素组成的不可变序列，用圆括号()来表示。
# 字典(dict)类型：由键值对组成的无序集合，用花括号{}来表示。
# 集合(set)类型：由一组互不相同的元素组成的无序集合，用花括号{}或set()来表示。
# 布尔(bool)类型：只有两个值，True和False。
# Python还有一些其他的数据类型，如文件(file)类型、空(None)类型等，但它们不像上述数据类型那样常用。

#定义变量
a=1
print(a)
print(type(a))

#定义的变量可以重新赋值 而且类型会随之改变
a='hello'
print(a)
print(type(a))

#变量的类型是动态的 但可以使用 :type 来提示IDE
x:int = 666;
print(x)
print(type(x))

a=1
b=2.2
cc:complex = 4+5j #复数 注意这里是j不是i
c='hello'
d=True
e=[1,2,3]#数组list
f=(1,2,3)#元组tuple
g={'name':'张三','age':18}#字典类型dict
h={1,2,3}#集合set

print('---------------------------------')
print(a)
print(b)
print(c)
print(cc)
print(d)
print(e)
print(f)
print(g)
print(h)
print('---------------------------------')
g['age'] = a
print(g)
print(type(f))
print(type(g))
print('----------------调用元组成员-----------------')
print(f[1])#调用元组成员
print('----------------集合应用-----------------')
a = {1, 2, 3}
b = {2, 3, 4}

print(a | b)   # 输出：{1, 2, 3, 4}，并集
print(a & b)   # 输出：{2, 3}，交集
print(a - b)   # 输出：{1}，差集

print('---------------------------------')
#数据类型转换
#将数字类型转换为字符串类型
print(type(str(123)))
#将字符串类型转换为数字类型
print(type(int('123')))
