from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'profile'
urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('detail/<str:user>', login_required(views.DetailView.as_view()), name="profile-detail"),
    path('edit/<int:pk>', login_required(views.EditAccountView.as_view()), name="profile-edit"),
    path('delete/<pk>', login_required(views.profile_delete), name="profile-delete"),
]
