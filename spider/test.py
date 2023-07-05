import urllib.request
import urllib.parse

# response = urllib.request.urlopen('https://www.python.org')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))
# print(response.read().decode('utf-8'))

# data = bytes(urllib.parse.urlencode({'name': 'germey'}), encoding='utf-8')
# response = urllib.request.urlopen('https://httpbin.org/post', data)
# print(response.read().decode('utf-8'))


# import urllib.request
# response = urllib.request.urlopen('https://httpbin.org/get', timeout=0.1)
# print(response.read())


import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('https://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')



