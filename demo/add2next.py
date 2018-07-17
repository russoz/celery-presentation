#!/usr/bin/env python

import sys
import time
from random import randint
from socket import gethostname
from celery import Celery

app = Celery('add2next',
             broker='pyamqp://admin:admin@192.168.144.99//',
             backend='rpc://')

@app.task
def task1(x):
    return ['task 1 ({})'.format(gethostname()), x + 1]

@app.task
def task2(x, y):
    return x + ['task 2 ({})'.format(gethostname()), x[1] + y]

if __name__ == '__main__':
    count = int(sys.argv[1])
    maxnum = int(sys.argv[2])
    asyncs = []

    for i in range(0,count):
        a = randint(0,maxnum)
        chain = (task1.s(a) | task2.s(3))
        asyncs += [ [a, chain()] ]

    print('we haz asyncs ({})'.format(len(asyncs)))

    for rr in asyncs:
        print('chain: {} => {}'.format(rr[0], rr[1].get()))

