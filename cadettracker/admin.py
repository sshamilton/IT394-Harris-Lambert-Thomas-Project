from django.contrib import admin

# Register your models here.

from .models import Company, Location, Supply

#admin.site.register(Cadet)
admin.site.register(Company)
