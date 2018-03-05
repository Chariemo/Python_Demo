# -*- coding: utf-8 -*-

# @author: chenjianlin
# @create: 2018-03-05 18:31

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 7890))

print(client.recv(1024).decode('utf-8'))

for data in [b'Charley', b'Tom', b'Kobe']:
    client.send(data)
    print(client.recv(1024).decode('utf-8'))

client.send(b'exit')
client.close()
