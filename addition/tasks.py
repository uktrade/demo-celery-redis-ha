from celery import shared_task


@shared_task
def adding_task(a, b):
    return a + b
