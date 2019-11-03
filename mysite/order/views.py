from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.views import generic
from .models import Order
from profile.models import Profile
from hairdresser.models import Hairdresser, Hairstyle


class IndexView(generic.TemplateView):
    model = Order
    template_name = 'order/index.html'


class OrderCreateForm(forms.ModelForm):
    appointment_date = forms.SelectDateWidget()
    appointment_time = forms.SelectDateWidget()
    description = forms.Textarea()
    hairdresser_id = forms.Select()

    class Meta:
        model = Order
        fields = ['appointment_date', 'appointment_time', 'description', 'hairdresser_id']


class NewOrderView(generic.CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name_suffix = '_new'
    success_url = 'dashboard'
