#操作字符串
print('-------------------------------------------')
#拼接字符串
print('拼接'+'字符内容')
print('-------------------------------------------')
#文字中插入其他变量 例如数子 方式类似C语言 采用%d 来替换变量
name = "张三"
age = 18
height = 1.75
str = "%s的年龄是%d，身高%fm"%(name,age,height);#这里浮点型 %f 的对应输出会补全浮点类型后面的位数 不理想
print(str)
#或 使用字符串的format函数
str = "{}的年龄是{}，身高{}m".format(name,age,height);
print(str)
#或 使用f-string 3.6版本后支持 语法更简洁
str = f"{name}的年龄是{age}，身高{height}m";
print(str)
print('-------------------------------------------')
#字符串按照字符拆分为字符串数组
print('字符,串按照字,符拆分'.split(','))
print('-------------------------------------------')
#字符串替换
string = "Hello, World!"
result = string.replace("World", "Python")
print(result) # 输出结果为 "Hello, Python!"
print('-------------------------------------------')
#字符串大小写转换
print('Hello'.upper())
print('Hello'.lower())
print('-------------------------------------------')
#获取特定字符索引位置
print('获取特定字符索引位置'.find('特'))
#获取特定字符最后出现的位置
print('获取特定字符最后出现的位置'.rfind('出'))
#获取字符串中所有特定字符出现的位置
#find rfind index可以接收第二个参数 表示该字符出现的顺序 利用第二个参数进行循环找出所有的字符位置组数
def getIndexArrFromStr(str,regStr):
    indexArr = []
    index = -1
    while True:
        try:
            index = str.index(regStr, index + 1)
            indexArr.append(index)
        except ValueError:
            break
    return indexArr

string = "Hello, World!"
char = "o"
indexArr = getIndexArrFromStr(string,char)
print(indexArr)
print('-------------------------------------------')
    
print('从一个字符串找到特定字符出现的位置的数组'.index('一'))
print('-------------------------------------------')
#判断字符串是否以特定字符开头
print('判断字符串是否以特定字符开头'.startswith('判'))
#判断字符串是否以特定字符结尾
print('判断字符串是否以特定字符结尾'.endswith('尾'))
print('-------------------------------------------')
#去除字符串两边的空格
print('去除字符串两边的空格   '.strip())
#去除字符串左边的空格
print('去除字符串左边的空格   '.lstrip())
#去除字符串右边的空格
print('去除字符串右边的空格   '.rstrip())
print('-------------------------------------------')
#判断字符串是否全是数字
print('判断字符串是否全是数字'.isdigit())
#判断字符串是否全是字母
print('判断字符串是否全是字母'.isalpha())
#判断字符串是否全是字母或数字
print('判断字符串是否全是字母或数字'.isalnum())
print('-------------------------------------------')
#字符串的长度
print('字符串的长度'.__len__())