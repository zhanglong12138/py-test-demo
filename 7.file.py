print('-------------------python中的文件处理相关------------------------')
# #python中的文件处理相关
# #文件的打开
# #file：文件的路径
# #mode：文件的打开模式
path = 'test'
file = open('test', encoding='utf-8')
contents = file.read()
print(contents)
file = open('test', encoding='utf-8')
contents = file.readline()
print(contents)
contents = file.readline()
print(contents)
file = open('test', encoding='utf-8')
contents = file.readlines()
print(contents)
file = open('test', encoding='utf-8')
for line in file:
    print(line)
file.close()
#定义一个读取文件全部内容的函数
def read_file(path):
    file = open(path, encoding='utf-8')
    return file.read()
    
print('-------------------python中的文件的写入------------------------')
# #python中的文件的写入
print(read_file(path))
file = open(path, encoding='utf-8', mode='w')
file.write('hello world\n')
file.write('hello world\n')
file.write('hello world\n')
file.close()
print('-------------------追加内容 a 覆盖为 w 创建为x 读取为r t为文本模式------------------------')
print(read_file(path))
file = open('test2', encoding='utf-8', mode='a')
file.write('hello world\n')
file.write('hello world\n')
file.write('hello world\n')
file.close()
print(read_file(path))
print('-------------------python中删除文件------------------------')
# #python中删除文件
import os
os.remove('test2')
print('-------------------python中创建删除文件夹------------------------')
# #python中创建删除文件夹
os.mkdir('test_dir')
os.rmdir('test_dir')
print('-------------------python中获取当前目录------------------------')
# #python中获取当前目录
print(os.getcwd())
print('-------------------python中获取目录列表------------------------')
# #python中获取目录列表
print(os.listdir())
# print('-------------------python中改变当前目录------------------------')
# # #python中改变当前目录
# # os.mkdir('test_dir2')
# # os.chdir('test_dir2')
# print(os.getcwd())
# print('-------------------python中重命名文件------------------------')
# # #python中重命名文件
# os.rename('test_dir2', 'test_dir3')
# os.rename('test copy', 'test copy2')
# print(os.listdir())
print('-------------------python中获取文件信息------------------------')
# #python中获取文件信息
print(os.stat('test'))
print('-------------------python中获取文件大小------------------------')
# #python中获取文件大小
print(os.stat('test').st_size)
print('-------------------python中获取文件权限------------------------')
# #python中获取文件权限
