from django.shortcuts import render, loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Company, Location, Supply, Personnel, Regiment, CompanyHasSupply, RegHasSupply, Building, CompanyNeedsSupply
from .forms import modifyForm, requestForm, other_requestForm

# Create your views here.

def index(request):
    Company_list = Company.objects.order_by('CompanyName')
    Reg_List = Regiment.objects.order_by('RegNum')
    template = loader.get_template('cadettracker/index.html')
    context = {
        'Company_list': Company_list,
        'Reg_List': Reg_List,
    }
    return HttpResponse(template.render(context,
                                        request))

def company(request,company_id):
    Co = Company.objects.get(pk=company_id)
    #Reg = Company.objects.get('regiment')
    #import pdb
    #pdb.set_trace()
    template = loader.get_template('cadettracker/company.html')
    context = {
        'Co' : Co,
    }
    return HttpResponse(template.render(context,
                                        request))

def fulfillRequest(request, item_id):
    if request.method == "POST":
        form = requestForm(request.POST)
        item = CompanyNeedsSupply.objects.get(pk=item_id)
        # import pdb
        # pdb.set_trace()
        item.delete()
        return HttpResponseRedirect('/supply')

def reg(request, reg_id):
    regi = Regiment.objects.get(pk=reg_id)
    template = loader.get_template('cadettracker/regiment.html')
    context = {
        'regi': regi
    }
    return HttpResponse(template.render(context,
                                        request,
                                        ))


def requestsupplies(request, company_id):
    if request.method == 'POST':
        form = other_requestForm(request.POST)
        if form.is_valid():
            try:
                co = CompanyNeeds.objects.get(CompanyLabel=company_id,
                                                  Item=form.data['Item'],
                                                  Location=form.data['Location'])
            except Exception as e:
                print(e)
                form.save()
            else:
                co.NumRequested = int(form.data['NumRequested'])
                co.save()
            #except:
             #   pass
            # import pdb
            # pdb.set_trace()
            return HttpResponseRedirect('/supply')
    else:
        form = other_requestForm()
    return render(request, 'cadettracker/delete.html', {'form':form})


def modifysupplies(request, company_id):
    if request.method == 'POST':
        form = modifyForm(request.POST)
        if form.is_valid():
            try:
                co = CompanyHasSupply.objects.get(CompanyLabel=company_id,
                                                  Item=form.data['Item'],
                                                  Location=form.data['Location'])
            except Exception as e:
                print(e)
                form.save()
            else:
                co.NumAvailable += int(form.data['NumAvailable'])
                co.save()
            #except:
             #   pass
            return HttpResponseRedirect('/supply')
    else:
        form = modifyForm()
    return render(request, 'cadettracker/modify.html', {'form':form})
#List cadets is first view
'''
def index(request):
    cadets = Cadet.objects.all()
    context = {'cadets': cadets}
    template = loader.get_template('cadettracker/index.html')
    return HttpResponse(template.render(context,request))
'''
