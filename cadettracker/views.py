from django.shortcuts import render, loader
from django.http import HttpResponse
from .models import Company, Location, Supply, Personnel, Regiment, CompanyHasSupply, RegHasSupply, Building, CompanyNeedsSupply


# Create your views here.

def index(request):
    Company_list = Company.objects.order_by('CompanyName')
    #output = ', '.join([(str(c.CompanyName) + ": " + str(c.regiment) + "  " + str(c.LocationID))
                       # for c in Company_list])
    template = loader.get_template('cadettracker/index.html')
    context = {
        'Company_list': Company_list,
    }
    return HttpResponse(template.render(context,
                                        request))

def company(request,CompanyName):
    #items = Supply.objects.order_by('item')
    supplies = CompanyHasSupply.objects.order_by('CompanyLabel')
    template = loader.get_template('cadettracker/company.html')
    context = {
        'Supply List' : supplies,
    }
    return HttpResponse(template.render(context,
                                        request))

#List cadets is first view
'''
def index(request):
    cadets = Cadet.objects.all()
    context = {'cadets': cadets}
    template = loader.get_template('cadettracker/index.html')
    return HttpResponse(template.render(context,request))
'''
