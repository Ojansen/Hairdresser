from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .models import Order


class IndexView(generic.TemplateView):
    model = Order
    template_name = 'order/index.html'
