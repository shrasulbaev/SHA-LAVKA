from django.contrib import admin
from .models import User


@admin.register(User)
class Useradmin(admin.ModelAdmin):
    pass

