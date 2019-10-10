from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.views import generic
from .models import Order
from account.models import Account
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

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.user_id = Account.pk
        form.save()
        return super().form_valid(form)
