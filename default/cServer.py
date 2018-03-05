# -*- coding: utf-8 -*-

# @author: chenjianlin
# @create: 2018-03-05 16:51

import socket
import threading

import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 7890))
server.listen(5)
print('Waiting for connection')


def tcplink(sock, address):
    print("Accept new connection from %s: %s" % address)
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello, %s' % data.decode('utf-8')).encode('utf-8'))

    sock.close()
    print('Connection from %s: %s closed' % address)


while True:
    c, add = server.accept()
    t = threading.Thread(target=tcplink, args=(c, add))
    t.start()