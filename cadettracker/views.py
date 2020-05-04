from django.shortcuts import render, loader
from django.http import HttpResponse
#from .models import Cadet

# Create your views here.

#List cadets is first view
'''
def index(request):
    cadets = Cadet.objects.all()
    context = {'cadets': cadets}
    template = loader.get_template('cadettracker/index.html')
    return HttpResponse(template.render(context,request))
'''
