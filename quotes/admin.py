from django.contrib import admin
from .models import Anime, Character, Quote

# Register your models here.
admin.site.register([Anime, Character, Quote])