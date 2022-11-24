from celery import shared_task
from celery.signals import task_postrun
from celery.utils.log import get_task_logger
from django.core.management import call_command

import requests

logger = get_task_logger(__name__)


@shared_task
def get_data_task():
    url = 'http://universities.hipolabs.com/search'

    response = requests.get(url=url)

    logger.info(response.status_code)
