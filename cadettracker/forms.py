from. models import Company, Location, Supply, Personnel, Regiment, CompanyHasSupply, RegHasSupply, Building, CompanyNeedsSupply
from django import forms

class modifyForm(forms.ModelForm):
    class Meta:
        model = CompanyHasSupply
        fields = '__all__'
