from django.urls import path

from .views import OrderListView, get_data

app_name = "orders"

urlpatterns = [
    path("", OrderListView.as_view(), name="list"),
    path("request/", get_data, name="get_data")
]
