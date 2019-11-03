from django.shortcuts import render_to_response
from django.template import RequestContext

from profile.models import Profile
from order.models import Order
from hairdresser.models import Hairdresser
from django.shortcuts import render
from django.views import generic


def dashboard(request):
    user = Profile.objects.get(pk=request.user.id)
    users = Profile.objects.all()
    hairdressers = Hairdresser.objects.all()
    orders = Order.objects.filter(user_id=user.pk)

    return render(request, 'home.html', {'user': user, 'users': users, 'hairdressers': hairdressers, 'orders': orders})
