from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Account, MyAccountManager
from .admin import UserCreationForm


class SignUp(generic.edit.CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)


class DetailView(generic.DetailView):
    model = Account
    template_name = 'account/account_detail.html'
    login_url = 'login/'

    def get(self, request):
        user = Account.objects.get(pk=request.user.id)
        return render(request, 'account/account_detail.html', {'user': user})


class EditAccountView(generic.UpdateView):
    model = Account
    template_name_suffix = '_edit'
    fields = ['first_name', 'last_name', 'email', 'address', 'mobile_nr']


class AccountDelete(generic.DetailView):
    model = Account
    success_url = reverse_lazy('signup')

    def post(self, request):
        pass
