# block io
import requests
html = requests.get('http://www.baidu.com').text
print(html)


import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'www.baidu.com'
client.connect((host, 80))  # block io
client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format('/', host).encode('utf8'))

data = b''
while 1:
    d = client.recv(1024)
    if d:
        data += d
    else:
        break
data = data.decode('utf8')
print(data)
