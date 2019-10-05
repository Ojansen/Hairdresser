from django.contrib import admin
from .models import Hairstyle, Hairdresser

# Register your models here.
@admin.register(Hairdresser)
class HairdresserAdmin(admin.ModelAdmin):
    pass


@admin.register(Hairstyle)
class HairstyleAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'sex')
