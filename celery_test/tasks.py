import redis
from celery import Celery

app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/1')


@app.task
def add(x, y):
    return x + y


