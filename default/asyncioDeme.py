# -*- coding: utf-8 -*-

# @author: chenjianlin
# @create: 2018-03-06 15:54
import asyncio
import threading


# Demo 1

# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread)
#     yield from asyncio.sleep(1)
#     print('hello again! (%s)' % threading.currentThread)
#
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))


# Demo 2


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET /HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))

    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()