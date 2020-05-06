from django.contrib import admin

# Register your models here.

from .models import Company, Location, Supply, Personnel, Regiment, CompanyHasSupply, RegHasSupply

admin.site.register(Company)
admin.site.register(Location)
admin.site.register(Supply)
admin.site.register(Personnel)
admin.site.register(Regiment)
admin.site.register(CompanyHasSupply)
admin.site.register(RegHasSupply)