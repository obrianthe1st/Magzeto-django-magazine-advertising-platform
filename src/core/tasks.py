from celery import Celery

app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

@app.task
def add():
    for _ in range(1000):
        print(0)
    return "Done"