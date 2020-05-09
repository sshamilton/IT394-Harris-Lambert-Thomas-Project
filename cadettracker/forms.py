from. models import Company, Location, Supply, Personnel, Regiment, CompanyHasSupply, RegHasSupply, Building, CompanyNeedsSupply
from django import forms

class modifyForm(forms.ModelForm):
    class Meta:
        model = CompanyHasSupply
        fields = "__all__"

class requestForm(forms.ModelForm):
    class Meta:
        model = CompanyNeedsSupply
        fields = "__all__"

class other_requestForm(forms.ModelForm):
    class Meta:
        model = CompanyNeedsSupply
        fields = "__all__"
