from celery import Celery
from random import randint
from socket import gethostname
import time
app = Celery('myapp', broker='pyamqp://admin:admin@192.168.144.99//', backend='rpc://')

@app.task
def add(x, y):
    time.sleep(1)
    return '{}: {}'.format(gethostname(), x + y)

if __name__ == '__main__':
    asyncs = []
    for i in range(0,100):
        a = [randint(0,100), randint(0,100)]
        asyncs += [[a[0], a[1], add.delay(*a)]]
    print('we haz asyncs ({})'.format(len(asyncs)))
    for rr in asyncs:
        print('add: {}, {} => {}'.format(rr[0], rr[1], rr[2].get()))

