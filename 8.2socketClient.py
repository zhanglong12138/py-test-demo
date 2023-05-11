import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8888
s.connect((host, port))
data = 'hi'
s.send(data.encode('utf-8'))
data = s.recv(1024)
print('Received data:', data.decode('utf-8'))
s.close()
