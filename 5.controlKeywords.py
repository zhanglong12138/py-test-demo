
#过程控制语句 关键词
print("---------------------------------")
# 数值类型
if 0:
    print("0 is true")
else:
    print("0 is false")

if 1:
    print("1 is true")
else:
    print("1 is false")

if -1:
    print("-1 is true")
else:
    print("-1 is false")

# 字符串类型
if "":
    print("empty string is true")
else:
    print("empty string is false")

if "non-empty":
    print("non-empty string is true")
else:
    print("non-empty string is false")

# 列表类型
if []:
    print("empty list is true")
else:
    print("empty list is false")

if [1, 2, 3]:
    print("non-empty list is true")
else:
    print("non-empty list is false")
print("---------------------------------")
#python 特有的elif 例如
a = 2
if a == 1:
    print("a is 1")
elif a == 2:
    print("a is 2")
else:
    print("a is not 1 or 2")
print("---------------------------------")
#python 中的的for 
#for可以用于遍历可迭代对象，如字符串、列表、元组、字典等。
# 可以对序列中的每个元素进行迭代操作。
list = [1,2,3,4]
for i in list:
    print(i)
print("---------------------------------")
#使用enumerate
for i, e in enumerate(list):
    print(i, e)
print("---------------------------------")
#python 特有的while 例如
i = 1
while i < 4:
    print(i)
    i += 1
print("---------------------------------")
#try except fininally使用例子
try:
    print(1 / 0)
except ZeroDivisionError:
    print("0不能作为除数")
print("---------------------------------")
#raise使用的例子
try:
    raise ZeroDivisionError("除数不能为0")
except ZeroDivisionError as e:
    print(e)
print("---------------------------------")
#except可以不指定类型
try:
    # some code that might raise an exception
    a = 1 / 0
except:
    print("An exception occurred")
print("---------------------------------")
#except可以捕获多个异常 
try:
    # some code that might raise an exception
    a = 1 / 0
except (ZeroDivisionError, NameError):
    print("An ZeroDivisionError or NameError exception occurred")
print("---------------------------------")
#with关键词 设置文件资源管理器索引
# with open('test.py', 'r') as f:
#     contents = f.read()
#     # print(contents)
with open('test', encoding='utf-8') as f:
    contents = f.read()
    print(contents)
print("---------------------------------")
#global关键字用于在函数或其他局部作用域中使用全局变量。
#但是如果不修改全局变量也可以不使用global关键字。
#如果要修改全局变量则必须使用global关键字声明。
#例如
a = 1
b = 1
def change():
    global a
    a = 2
    b = 2
change()
print(a,b)#2 1 a被修改了 b没有被修改
print("---------------------------------")
#nonlocal关键字用于在函数或其他作用域中使用外层(非全局)变量。
#例如
def outer():
    a = 1
    b = 1
    def inner():
        nonlocal a
        a = 2
        b = 2
    inner()
    print(a,b)#2 2 a被修改了 b没有被修改
outer()#2
print("---------------------------------")
#assert关键字用于判断一个表达式，在表达式条件为 false 的时候触发异常。
#assert expression [, arguments]
#例如
assert 1 == 1
# assert 1 == 2 #取消注释会报错
print("---------------------------------")
#yeild关键字用于生成器函数中，类似return关键字，不同之处在于yield返回的是一个生成器。
#生成器是一个特殊的迭代器，可以通过next()函数来迭代获取值。
#yield关键字可以在函数中多次使用，每次使用都会返回一个值。
#yield关键字可以返回任意类型的值，包括None。
#yield关键字可以返回任意个值，如果返回多个值，会返回一个元组。
#yield关键字可以接收调用者传递的值，通过send()函数传递。
#yield关键字可以在函数中接收调用者传递的异常，如果接收到异常，会触发StopIteration异常。
#例如
def generator():
    for i in range(4):
        yield i
g = generator()
print(g)#<generator object generator at 0x000001F4F4F4F0C8>
print(next(g))#0
print(next(g))#1
print(next(g))#2
print(next(g))#3
# print(next(g))#取消注释会报错
print("---------------------------------")
#send()函数用于向生成器函数传递值，与next()函数的区别在于send()函数可以传递值。
def generate_numbers():
    i = 0
    while True:
        value = yield i
        if value is not None:
            i = value
        else:
            i += 1

gen = generate_numbers()
print(next(gen))  # 输出 0
print(next(gen))  # 输出 1
print(gen.send(10))  # 输出 10
print(next(gen))  # 输出 11
# print(next(g))#取消注释会报错
print("---------------------------------")