# -*- coding: utf-8 -*-

# @author: chenjianlin
# @create: 2018-03-06 15:33


def consumer():
    r = ''

    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] consume %s ...' % n)
        r = '200 ok'


def produce(c):

    c.send(None)
    n = 0;

    while n < 5:
        n += 1
        print('[PRODUCER] produce %s ...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)

    c.close()


c = consumer()

produce(c)