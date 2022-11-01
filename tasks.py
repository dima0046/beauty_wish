from celery import Celery

celery_app = Celery('tasks', broker='redis://localhost')

@celery_app.task
def add(x, y):
    print(x + y)