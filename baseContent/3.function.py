#函数相关
print('--------------------定义函数-----------------------')
def p(str:str):
    print(type);
    print(str);
p(123)
print('--------------------参数设置默认值 和 返回值-----------------------')
def add(a=1,b=2):
    return a+b
print(add())
print('--------------------回调函数 将函数作为参数传入其他函数-----------------------')
def apply_callback(callback_func, arg):
    callback_func(arg)

def callback(msg):
    print("Received message:", msg)

apply_callback(callback, "Hello")