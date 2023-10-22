from celery import shared_task
from celery.utils.log import get_task_logger
from .scraping import process_url, get_instagram
import logging

logger = logging.getLogger("Celery")
    
logger = get_task_logger(__name__)    


@shared_task
def get_instagram_task(username):
    result = get_instagram(username)
    if result == 'User was not found':
        return result
    process_url(username)
    return result


@shared_task
def celery_tasks_posts(username):
    result = process_url(username)
    return result