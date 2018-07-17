#!/usr/bin/env python

import sys
import time
from random import randint
from socket import gethostname
from celery import Celery

app = Celery('add2',
             broker='pyamqp://admin:admin@192.168.144.99//',
             backend='rpc://')

@app.task
def add(x, y):
    #time.sleep(1)
    return '{}: {}'.format(gethostname(), x + y)

if __name__ == '__main__':
    count = int(sys.argv[1])
    maxnum = int(sys.argv[2])
    asyncs = []

    for i in range(0,count):
        a = [randint(0,maxnum), randint(0,maxnum)]
        asyncs += [[a, add.delay(*a)]]
    print('we haz asyncs ({})'.format(len(asyncs)))

    for rr in asyncs:
        print('add: {} => {}'.format(rr[0], rr[1].get()))

