from django.urls import path
from . import views

urlpatterns = [
    path("api/", views.set_order, name="set_order")

]