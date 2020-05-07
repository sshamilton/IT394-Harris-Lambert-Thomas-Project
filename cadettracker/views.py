from django.shortcuts import render, loader
from django.http import HttpResponse
from .models import Company, Location, Supply, Personnel, Regiment, CompanyHasSupply, RegHasSupply, Building, CompanyNeedsSupply


# Create your views here.

def index(request):
    Company_list = Company.objects.order_by('CompanyName')
    output = ', '.join([(str(c.CompanyName) + str(c.LocationID)) for c in Company_list])
    return HttpResponse(output)


#List cadets is first view
'''
def index(request):
    cadets = Cadet.objects.all()
    context = {'cadets': cadets}
    template = loader.get_template('cadettracker/index.html')
    return HttpResponse(template.render(context,request))
'''
