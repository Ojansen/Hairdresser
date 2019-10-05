from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Account, MyAccountManager
from .forms import *


class SignUp(generic.edit.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)


class DetailView(generic.DetailView):
    model = Account
    template_name = 'account/details.html'
    login_url = 'login/'

    def get(self, request):
        user = Account.objects.get(pk=request.user.id)
        return render(request, 'account/details.html', {'user': user})
