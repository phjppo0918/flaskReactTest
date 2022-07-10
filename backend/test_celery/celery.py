from __future__ import absolute_import
from celery import Celery
from time import sleep

app = Celery('test_Celery',
             broker='amqp://guest:guest@127.0.0.1:5672//')


@app.task
def test_hello():
    sleep(3)
    print('hello')
    return 'hello'
