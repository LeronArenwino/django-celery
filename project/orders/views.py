from django.shortcuts import render
from django.views.generic import ListView

import logging
import requests

from .models import Order

logger = logging.getLogger(__name__)

class OrderListView(ListView):
    model = Order

def get_data(request):

    url = 'http://universities.hipolabs.com/search'

    response = requests.get(url=url)
    data = response.json()
    print(data)

    return render(request, 'order_request.html', {'response': data})