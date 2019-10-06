from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('detail/', login_required(views.DetailView.as_view()), name="account_detail"),
    path('edit/<int:pk>', login_required(views.EditAccountView.as_view()), name="edit_account"),
    path('delete/<int:pk>', login_required(views.DetailView.as_view()), name="account_delete"),
]
