#类的使用
print('-------------------------------------------')
#定义一个类
class Person:
    #类的构造函数
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #类的方法
    def say(self):
        print('my name is %s,my age is %d'%(self.name,self.age))
#类的实例化
p = Person('zhangsan',18)
p.say()
print('-------------------------------------------')
#类的继承
class Student(Person):
    def __init__(self,name,age,grade):
        Person.__init__(self,name,age)
        self.grade = grade
    def say(self):
        print('my name is %s,my age is %d,my grade is %d'%(self.name,self.age,self.grade))
s = Student('lisi',20,3)
s.say()
print('-------------------------------------------')
#类的多态
class Animal:
    def __init__(self,name):
        self.name = name
    def say(self):
        print('my name is %s'%(self.name))
class Dog(Animal):
    def say(self):
        print('my name is %s,wang wang wang'%(self.name))
class Cat(Animal):
    def say(self):
        print('my name is %s,miao miao miao'%(self.name))
a = Animal('animal')
a.say()
d = Dog('dog')
d.say()
c = Cat('cat')
c.say()
print('--------------------类的私有属性和私有方法-----------------------')
#类的私有属性和私有方法
class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def say(self):
        print('my name is %s,my age is %d'%(self.name,self.__age))
    def __say(self):
        print('my name is %s,my age is %d'%(self.name,self.__age))
    def useSelfSay(self):
        self.__say()
p = Person('zhangsan',18)
p.say()
p.useSelfSay()
#p.__say()#私有方法不能被调用
print('---------------------类的静态方法@staticmethod----------------------')
#类的静态方法
class Person:
    hostName = 'none'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @staticmethod
    def sayHello():
        print('hello')
p = Person('zhangsan',18)
p.sayHello()
Person.sayHello()
print('---------------------类方法@classmethod----------------------')
#类方法 用classmethod修饰的方法
#类方法的第一个参数是类对象cls，通过cls引用的类对象的属性和方法
#类方法可以通过类对象和实例对象去调用
class Person:
    hostName = 'none'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def setHostName(cls,newHostName):
        cls.hostName = newHostName
        print('newHostName:%s'%(cls.hostName))
    @classmethod
    def getHostName(cls):
        print('hostName:%s'%(cls.hostName))
p = Person('zhangsan',18)
p2 = Person('lisi',25)
Person.getHostName()
p.setHostName('zhang')
Person.getHostName()
Person.setHostName('li')
Person.getHostName()
p2.setHostName('wang')
p2.getHostName()
print('-----------------类的特殊属性__dict__ 返回一个字典类型的数据 包含所有类的成员 包含私有变量--------------------------')
#类的特殊属性__dict__ 返回一个字典类型的数据 包含所有类的成员 包含私有变量
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__age = age
p = Person('zhangsan',18)
print(p.__dict__)
print('---------------------类的特殊方法__str__----------------------')
#类的特殊方法__str__
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return '描述对象的信息'
p = Person('zhangsan',18)
print(p)
print('-------------------------------------------')
#类的特殊方法__getitem__
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __getitem__(self, item):
        return self.__dict__[item]
p = Person('zhangsan',18)
print(p['name'])
print('-------------------------------------------')
#类的特殊方法__setitem__
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __setitem__(self, key, value):
        self.__dict__[key] = value
p = Person('zhangsan',18)
p['name'] = 'lisi'
print(p.name)
print('-------------------------------------------')
#类的特殊方法__delitem__
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __delitem__(self, key):
        del self.__dict__[key]
p = Person('zhangsan',18)
del p['name']
print(p.__dict__)
print('-------------------------------------------')
#类的特殊方法__len__
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __len__(self):
        # return len(self.__dict__)
        return self.age
p = Person('zhangsan',18)
print(len(p))
print('--------------------类的周期函数-----------------------')
#类的特殊方法__call__

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __call__(self, *args, **kwargs):
        print('call')
p = Person('zhangsan',18)
p()
print('-------------------------------------------')
#类的特殊方法__new__
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __new__(cls, *args, **kwargs):
        print('new')
        return object.__new__(cls)
p = Person('zhangsan',18)
print('-------------------------------------------')
#call和new的区别
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __call__(self, *args, **kwargs):
        print('call')
    def __new__(cls, *args, **kwargs):
        print('new')
        return object.__new__(cls)
p = Person('zhangsan',18)
p()
print('-------------------------------------------')
#类的特殊方法__del__
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __del__(self):
        print('del')
p = Person('zhangsan',18)
del p
print('----------------------__slots__ ---------------------')
#类的特殊方法__slots__ 
#因为实例可以动态创建成员 使用__slots_可以约束对象的成员列表 节省内存 
#如果不在列表中的成员不能被添加到对象中 并且会抛出异常 
class Person:
    __slots__ = ('name','age')
    def __init__(self,name,age):
        self.name = name
        self.age = age
p = Person('zhangsan',18)
#p.sex = 'male'#会抛出异常
print(p.name)
print(p.age)
print('-------------------类的特殊方法__eq__------------------------')
#类的特殊方法__eq__
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        return self.age == other.age
p1 = Person('zhangsan',18)
p2 = Person('lisi',18)
print(p1 == p2)
print('-------------------类的特殊方法__hash__------------------------')
#类的特殊方法__hash__
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __hash__(self):
        return 1
p1 = Person('zhangsan',18)
p2 = Person('lisi',18)
print(hash(p1))
print(hash(p2))
print('-------------------类的特殊方法__bool__------------------------')
#类的特殊方法__bool__
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __bool__(self):
        return self.age > 18
p1 = Person('zhangsan',18)
p2 = Person('lisi',19)
print(bool(p1))
print(bool(p2))
# print('-------------------类的特殊方法__format__------------------------')
# #类的特殊方法__format__
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __format__(self, format_spec):
#         return 'hello'
# p1 = Person('zhangsan',18)
# print(format(p1,''))
print('-------------------类的特殊方法__enter__和__exit__------------------------')
#类的特殊方法__enter__和__exit__ 读取资源和释放资源时使用
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __enter__(self):
        print('enter')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
p1 = Person('zhangsan',18)
with p1 as p:
    print(p)
print('-------------------类的特殊方法__getattribute__------------------------')
#类的特殊方法__getattribute__
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __getattribute__(self, item):
        print(item) 
p1 = Person('zhangsan',18)
print(p1.name)
print(p1.age)
print('-------------------类的特殊方法__getattr__------------------------')
#类的特殊方法__getattr__
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __getattr__(self, item):
        print(item) 
p1 = Person('zhangsan',18)
print(p1.name)
print(p1.age)
print('-------------------类的特殊方法__setattr__------------------------')
#类的特殊方法__setattr__
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __setattr__(self, key, value):
        print(key,value)
p1 = Person('zhangsan',18)
p1.name = 'lisi'
print('-------------------类的特殊方法__delattr__------------------------')
#类的特殊方法__delattr__
class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __delattr__(self, item):
        print(item)
p1 = Person('zhangsan',18)
del p1.name
print('-------------------类的特殊方法__get__------------------------')
#类的特殊方法__get__
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __get__(self, instance, owner):
        print(instance,owner)
class Student:
    p = Person('zhangsan',18)
s = Student()
s.p
print('-------------------类的特殊方法__set__------------------------')
#类的特殊方法__set__
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __set__(self, instance, value):
        print(instance,value)
class Student:
    p = Person('zhangsan',18)
s = Student()
s.p = 'lisi'
print('-------------------类的特殊方法__delete__------------------------')
#类的特殊方法__delete__
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __delete__(self, instance):
        print(instance)
class Student:
    p = Person('zhangsan',18)
s = Student()
del s.p



    


