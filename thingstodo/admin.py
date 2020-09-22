# todo/admin.py

from django.contrib import admin
from .models import Thingstodo  # add this


class ThingstodoAdmin(admin.ModelAdmin):  # add this
    list_display = ('title', 'description', 'completed')  # add this


# Register your models here.
admin.site.register(Thingstodo, ThingstodoAdmin)  # add this
