from django.shortcuts import render
from django.views.generic import ListView
from .tasks import get_data_task

import logging

from .models import Order

logger = logging.getLogger(__name__)

Q_RESQUEST = 100

class OrderListView(ListView):
    model = Order

def get_data(request):

    for _ in range(0, Q_RESQUEST):
        get_data_task.delay()

    return render(request, 'orders/order_request.html', {})