from django.contrib import admin

# Register your models here.

from .models import Cadet, Company, Locations

admin.site.register(Cadet)
admin.site.register(Company)
