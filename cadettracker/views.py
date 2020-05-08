from django.shortcuts import render, loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Company, Location, Supply, Personnel, Regiment, CompanyHasSupply, RegHasSupply, Building, CompanyNeedsSupply
from .forms import modifyForm

# Create your views here.

def index(request):
    Company_list = Company.objects.order_by('CompanyName')
    Reg_List = Regiment.objects.order_by('RegNum')
    #output = ', '.join([(str(c.CompanyName) + ": " + str(c.regiment) + "  " + str(c.LocationID))
                       # for c in Company_list])
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

def fulfillRequest(request, request_id):
    if request.method == "POST":
        form = requestForm(request.POST)
        Request = CompanyNeedsSupply.objects.get(pk=request_id)
         # = Reg.objects.get()
        Request.delete()
        form.save()
        # template = loader.get_template('cadettracker/regiment.html')
        return HttpResponseRedirect('/supply')
        # return render(request, 'cadettracker/delete.html')

def reg(request, reg_id):
    regi = Regiment.objects.get(pk=reg_id)
    #import pdb
    #pdb.set_trace()
    template = loader.get_template('cadettracker/regiment.html')
    context = {
        'regi': regi
    }
    return HttpResponse(template.render(context,
                                        request,
                                        ))




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
            import pdb
            pdb.set_trace()
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
