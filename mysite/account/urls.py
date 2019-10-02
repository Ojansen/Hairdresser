from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('detail/<user>', login_required(views.DetailView.as_view()), name="detail")
]
