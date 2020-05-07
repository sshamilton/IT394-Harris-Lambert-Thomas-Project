from django.contrib import admin

# Register your models here.

from .models import Company, Location, Supply, Personnel, Regiment, CompanyHasSupply, RegHasSupply, Building, CompanyNeedsSupply, CompanyHasPersonnel

admin.site.register(Company)
admin.site.register(Location)
admin.site.register(Supply)
admin.site.register(Personnel)
admin.site.register(Regiment)
admin.site.register(CompanyHasSupply)
admin.site.register(CompanyNeedsSupply)
admin.site.register(RegHasSupply)
admin.site.register(Building)
admin.site.register(CompanyHasPersonnel)