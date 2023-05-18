#创建一个socket服务
import socket
#创建一个socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#获取本地主机名
s.bind(('127.0.0.1', 8888))
s.listen(5)
conn, addr = s.accept()
data = conn.recv(1024)
print('Received data:', data.decode('utf-8'))
conn.send("hello".encode('utf-8'))
