from .celery import app as celery_app
from celery import shared_task


__all__ = ('celery_app',)

