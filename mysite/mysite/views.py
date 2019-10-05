from django.shortcuts import render_to_response
from django.template import RequestContext

from account.models import Account
from order.models import Order
from hairdresser.models import Hairdresser
from django.shortcuts import render
from django.views import generic


def dashboard(request):
    user = Account.objects.get(pk=request.user.id)
    users = Account.objects.all()
    hairdressers = Hairdresser.objects.all()
    orders = Order.objects.filter(user_id=user.pk)

    return render(request, 'home.html', {'user': user, 'users': users, 'hairdressers': hairdressers, 'orders': orders})
