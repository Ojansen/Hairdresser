from django.contrib import admin
from django import forms
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'is_admin', 'is_staff')
