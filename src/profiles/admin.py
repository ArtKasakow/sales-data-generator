from profiles.models import Profile
from django.apps import config
from django.contrib import admin
from .models import Profile

# Register your models here.

admin.site.register(Profile)