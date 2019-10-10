from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('new/', NewOrderView.as_view(), name="new_order"),
]